import numpy as np
import gradio as gr

"""
    在某些情况下，您可能需要在 UI 中实际渲染组件之前定义它们。例如，您可能想使用gr.Examples上面的相应gr.Textbox输入来显示示例部分。
    由于gr.Examples需要输入组件对象作为参数，因此您需要首先定义输入组件，然后在定义对象后渲染它gr.Examples。

"""

input_textbox = gr.Textbox()

with gr.Blocks() as demo:
    gr.Examples(["hello", "bonjour", "merhaba"], input_textbox)
    input_textbox.render()

if __name__ == "__main__":
   demo.launch()
