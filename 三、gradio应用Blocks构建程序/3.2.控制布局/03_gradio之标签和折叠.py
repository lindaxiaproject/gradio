import numpy as np
import gradio as gr

# 翻转文本
def flip_text(x):
    return x[::-1]

# 翻转图片
def flip_image(x):
    return np.fliplr(x)


with gr.Blocks() as demo:
    gr.Markdown("使用此演示翻转文本或图像文本！")
    with gr.Tab("翻转文本"):
        text_input = gr.Textbox()
        text_output = gr.Textbox()
        text_button = gr.Button("翻动按钮")
    with gr.Tab("图像文本"):
        with gr.Row():
            image_input = gr.Image()
            image_output = gr.Image()
        image_button = gr.Button("翻动按钮")

    with gr.Accordion("开放更多功能"):
        gr.Markdown("敬请期待....")

    text_button.click(flip_text, inputs=text_input, outputs=text_output)
    image_button.click(flip_image, inputs=image_input, outputs=image_output)

if __name__ == '__main__':
    demo.launch()