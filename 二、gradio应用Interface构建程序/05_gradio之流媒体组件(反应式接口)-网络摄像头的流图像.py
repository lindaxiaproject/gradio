import gradio as gr
import numpy as np


"""
    Gradio 界面自动刷新或连续传输数据
        流式传输意味着数据不断发送到后端并且Interface函数不断重新运行
        
    网络摄像头的流图像的示例代码
"""

def flip(im):
    return np.flipud(im)

demo = gr.Interface(
    flip,
    gr.Image(sources=["webcam"], streaming=True),
    "image",
    live=True
)

if __name__ == '__main__':
    demo.launch()