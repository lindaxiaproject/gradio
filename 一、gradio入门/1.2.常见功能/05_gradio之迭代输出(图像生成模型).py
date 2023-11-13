import gradio as gr
import numpy as np
import time
"""

    某些场景流式传输一系列输出，而不是一次显示单个输出。
        例如，您可能有一个图像生成模型，并且希望显示每个步骤生成的图像，直至最终图像。
            或者您可能有一个聊天机器人，它一次一个字地传输其响应，而不是一次返回全部内容。

    向 Gradio 提供生成器函数而不是常规函数。在 Python 中创建生成器非常简单：
        return函数应该包含yield一系列值，而不是单个值。通常该yield语句被放入某种循环中。
"""

# 生成steps张图片，每隔1秒钟返回
def fake_diffusion(steps):
    for _ in range(steps):
        # 在迭代器中添加了 atime.sleep(1)以在步骤之间创建人工暂停，以便您能够观察迭代器的步骤
        time.sleep(1)
        image = np.random.random((600, 600, 3))
        yield image
    image = np.ones((1000,1000,3), np.uint8)
    image[:] = [255, 124, 0]
    yield image

# 设置滑窗，最小值为1，最大值为10，初始值为3，每次改动增减1位
demo = gr.Interface(fake_diffusion, inputs= gr.Slider(1, 10 , 3), outputs="image")

# 生成器必须要queue函数
demo.queue()
demo.launch()