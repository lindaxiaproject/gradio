import math
import gradio as gr
import plotly.express as px
import numpy as np

"""
every函数
    您可以使用事件侦听器的参数按固定计划运行事件。every这将在客户端连接打开时运行事件 秒数。
    如果连接关闭，则事件将在下一次迭代后停止运行。
    请注意，这没有考虑事件本身的运行时间。因此，运行时间为 1 秒的函数every=5实际上每 6 秒运行一次。
"""

plot_end = 2 * math.pi

def get_plot(period=1):
    global plot_end
    x = np.arange(plot_end - 2 * math.pi, plot_end, 0.02)
    y = np.sin(2 * math.pi * period * x)
    fig = px.line(x=x, y=y)
    plot_end += 2 * math.pi
    if plot_end > 1000:
        plot_end = 2 * math.pi
    return fig


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            gr.Markdown("更新滑块的值以自动更新绘图")
            period = gr.Slider(label="绘制周期", value=1, minimum=0, maximum=10, step=1)
            plot = gr.Plot(label="图表 (每半秒更新一次)")

    dep = demo.load(get_plot, None, plot, every=1)
    period.change(get_plot, period, plot, every=1, cancels=[dep])

demo.queue()
"""
    梯度/正弦曲线
"""
if __name__ == '__main__':
    demo.launch()

