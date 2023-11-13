import numpy as np
import gradio as gr

"""
该类gradio.Interface实际上可以处理 4 种不同类型的演示
    （1）标准演示：具有单独的输入和输出（例如图像分类器或语音到文本模型）
    （2）仅输出演示：不接受任何输入但产生输出（例如无条件图像生成模型）
    （3）仅输入演示：不产生任何输出，但接受某种输入（例如，保存上传到持久外部数据库的图像的演示）
    （4）统一演示：同时具有输入和输出组件，但输入和输出组件是相同的。这意味着产生的输出会覆盖输入（例如文本自动完成模型）
"""

'''
    要创建同时具有输入和输出组件的演示，您只需在中设置inputs和outputs参数的值Interface()。
    这是一个简单图像过滤器的示例演示：
'''
def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

demo = gr.Interface(sepia, gr.Image(), "image")

if __name__ == '__main__':
    demo.launch()
