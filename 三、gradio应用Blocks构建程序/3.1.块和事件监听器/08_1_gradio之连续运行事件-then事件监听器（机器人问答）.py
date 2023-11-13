import gradio as gr
import random
import time


"""
    使用then事件侦听器的方法连续运行事件。这将在前一个事件运行完成后运行一个事件。
        这对于运行分多个步骤更新组件的事件非常有用。
        
    事件侦听器的方法.then()会执行后续事件，无论前一个事件是否引发任何错误。
    如果您只想在前一个事件执行成功后才运行后续事件，请使用该.success()方法，该方法采用与 相同的参数.then()
"""

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("清除上面问答信息")

    def user(user_message, history):
        return "", history + [[user_message, None]]


    def bot(history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        time.sleep(2)
        history[-1][1] = bot_message
        return history


    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

demo.queue()
if __name__ == '__main__':
    demo.launch()


if __name__ == '__main__':
    demo.launch()
