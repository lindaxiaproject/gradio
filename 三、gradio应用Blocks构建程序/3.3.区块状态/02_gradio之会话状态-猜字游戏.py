"""
    Gradio 支持会话状态，其中数据在页面会话内的多个提交中持续存在，在 Blocks 应用程序中也是如此。
        重申一下，会话数据不会在模型的不同用户之间共享。要将数据存储在会话状态中，您需要做三件事：

        （1）创建一个gr.State()对象。如果此有状态对象有默认值，请将其传递到构造函数中。
        （2）在事件监听器中，将State对象作为输入和输出。
        （3）在事件监听函数中，将变量添加到输入参数和返回值中。
"""
import gradio as gr
secret_word = "gradio"

'''

    我们将使用过的字母存储在used_letters_var. 在 的构造函数中State，我们将 this 的初始值设置为[]，一个空列表。
        1.在 中，我们在输入和输出中都btn.click()引用了。used_letters_var
        2.在 中guess_letter，我们将 this 的值传递给State，used_letters然后State在 return 语句中返回 this 的更新值。
        3.对于更复杂的应用程序，您可能会在单个 Blocks 应用程序中使用许多状态变量来存储会话状态。
'''
with gr.Blocks() as demo:
    used_letters_var = gr.State([])
    with gr.Row() as row:
        with gr.Column():
            input_letter = gr.Textbox(label="请您输入字母")
            btn = gr.Button("猜字母")
        with gr.Column():
            hangman = gr.Textbox(
                label="猜字游戏",
                value="_"*len(secret_word)
            )
            used_letters_box = gr.Textbox(label="使用过的字母：")

    def guess_letter(letter, used_letters):
        used_letters.append(letter)
        answer = "".join([
            (letter if letter in used_letters else "_")
            for letter in secret_word
        ])
        return {
            used_letters_var: used_letters,
            used_letters_box: ", ".join(used_letters),
            hangman: answer
        }
    btn.click(
        guess_letter,
        [input_letter, used_letters_var],
        [used_letters_var, used_letters_box, hangman]
        )

if __name__ == '__main__':
    demo.launch()