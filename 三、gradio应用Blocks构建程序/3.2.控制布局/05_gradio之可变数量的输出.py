import numpy as np
import gradio as gr


"""
通过以动态方式调整组件的可见性，可以使用支持可变数量输出的Gradio 创建演示。
    这是一个非常简单的示例，其中输出文本框的数量由输入滑块控制

"""

max_textboxes = 10

def variable_outputs(k):
    k = int(k)
    return [gr.Textbox(visible=True)]*k + [gr.Textbox(visible=False)]*(max_textboxes-k)

with gr.Blocks() as demo:
    s = gr.Slider(1, max_textboxes, value=max_textboxes, step=1, label="显示多少个文本框:")
    textboxes = []
    for i in range(max_textboxes):
        t = gr.Textbox(f"Textbox {i}")
        textboxes.append(t)

    s.change(variable_outputs, s, textboxes)

if __name__ == "__main__":
   demo.launch()
