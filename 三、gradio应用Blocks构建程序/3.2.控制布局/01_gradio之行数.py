"""
    默认情况下，块中的组件垂直排列。让我们看看如何重新排列组件。在底层，这种布局结构使用了Web 开发的 Flexbox 模型。

    flexbox，被设计为一维布局模型【CSS】
        https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox



"""
import gradio as gr

#  子句中的元素with gr.Row将全部水平显示。例如，要并排显示两个按钮：
with gr.Blocks() as demo:
    # 一行有两个按钮
    with gr.Row():
        btn1 = gr.Button("Button 1")
        btn2 = gr.Button("Button 2")

# 要使 Row 中的每个元素具有相同的高度，请使用equal_height该方法的参数style。
with gr.Blocks() as demo2:
    with gr.Row(equal_height=True):
        textbox = gr.Textbox()
        btn2 = gr.Button("Button 2")


# 行中元素的宽度可以通过每个组件中存在的scale和参数的组合来控制。min_width

# scale是一个整数，定义元素如何占用 Row 中的空间。如果比例设置为0，元素将不会扩展以占用空间。如果将比例设置为1或更大，
# 则元素会很好地扩展。一行中的多个元素将根据其比例按比例扩展。下面，btn1将膨胀两倍btn2，而btn0根本不膨胀


with gr.Blocks() as demo3:
    with gr.Row():
        btn0 = gr.Button("Button 0", scale=0)
        btn1 = gr.Button("Button 1", scale=1)
        btn2 = gr.Button("Button 2", scale=2)
if __name__ == '__main__':
    # demo.launch()
    # demo2.launch()
    demo3.launch()