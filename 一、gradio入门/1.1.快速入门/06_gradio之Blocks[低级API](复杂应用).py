import gradio as gr
import numpy as np


def flip_text(x):
    return x[::-1]


def flip_image(x):
    return np.fliplr(x)


with gr.Blocks() as demo:
    gr.Markdown("使用此演示反转文本或图像文件！")
    with gr.Tab("翻转文本"):
        text_input = gr.Textbox(label="输入文本框（文本）")
        text_output = gr.Textbox(label="输出文本框（文本）")
        text_button = gr.Button("翻转1")

    with gr.Tab("翻转图像"):
        with gr.Row():
            image_input = gr.Image()
            image_output = gr.Image()
        image_button = gr.Button("翻转2")

    with gr.Accordion("开放更多！"):
        gr.Markdown("林大侠学习Gradio!")

    # click向该按钮添加了一个事件侦听器
    text_button.click(flip_text, inputs=text_input, outputs=text_output)
    image_button.click(flip_image, inputs=image_input, outputs=image_output)

if __name__ == '__main__':
    demo.launch()
