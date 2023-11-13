"""
    事件侦听器有一个_js参数，可以将 Javascript 函数视为字符串，并将其视为 Python 事件侦听器函数。
    您可以同时传递 Javascript 函数和 Python 函数（在这种情况下首先运行 Javascript 函数）
    或仅传递 Javascript（并将 Python 设置为fn）None。看看下面的代码：

"""

import gradio as gr

blocks = gr.Blocks()

with blocks as demo:
    subject = gr.Textbox(placeholder="主题")
    verb = gr.Radio(["吃", "爱过", "讨厌的"]) # 单选框
    object = gr.Textbox(placeholder="对象")

    with gr.Row():
        btn = gr.Button("创造句子")
        reverse_btn = gr.Button("反转句")
        foo_bar_btn = gr.Button("追加 foo")
        reverse_then_to_the_server_btn = gr.Button(
            "反转句并发送到服务器"
        )

    def sentence_maker(w1, w2, w3):
        return f"{w1} {w2} {w3}"

    output1 = gr.Textbox(label="输出1")
    output2 = gr.Textbox(label="动词")
    output3 = gr.Textbox(label="动词颠倒")
    output4 = gr.Textbox(label="前端处理然后发送后端")

    btn.click(sentence_maker, [subject, verb, object], output1)
    reverse_btn.click(
        None, [subject, verb, object], output2, js="(s, v, o) => o + ' ' + v + ' ' + s"
    )
    verb.change(lambda x: x, verb, output3, js="(x) => [...x].reverse().join('')")
    foo_bar_btn.click(None, [], subject, js="(x) => x + ' foo'")

    reverse_then_to_the_server_btn.click(
        sentence_maker,
        [subject, verb, object],
        output4,
        js="(s, v, o) => [s, v, o].map(x => [...x].reverse().join(''))",
    )
if __name__ == '__main__':
    demo.launch()