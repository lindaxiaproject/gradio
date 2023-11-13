import gradio as gr

import gradio as gr

def welcome(name):
    return f"Welcome to Gradio, {name}!"

"""
    函数不是通过单击触发，而是welcome通过在文本框中键入内容来触发inp。这是由于change()事件监听器造成的。
    不同的组件支持不同的事件监听器。
        例如，Video组件支持play()事件监听器，当用户按下播放按钮时触发
"""
with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Hello World!
    开始在下面输出以查看输出吧！
    """)
    inp = gr.Textbox(placeholder="你叫什么名字", label="请您输入触发的内容")
    out = gr.Textbox(label="change()事件监听，无需submit触发")
    inp.change(welcome, inp, out)

if __name__ == '__main__':
    demo.launch()