import numpy as np
import gradio as gr

"""
    上传图片后，输入深褐色的图片
"""
def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

# shape设置输入图像大小
demo = gr.Interface(sepia, gr.Image(), "image")
"""
    Gradio 支持多种类型的组件，例如Image、DataFrame、Video或Label。
    Image组件作为输入时，函数将接收形状为的NumPy 数组(height, width, 3)，
        其中最后一个维度表示 RGB 值。我们也将以 NumPy 数组的形式返回图像。
"""
if __name__ == '__main__':
        demo.launch()
