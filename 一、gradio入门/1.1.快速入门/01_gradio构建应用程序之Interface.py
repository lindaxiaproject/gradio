import gradio as gr


def greet(name):
    return "hello" + name + "!"

"""
核心Interface类使用三个必需参数进行初始化
    fn：包装 UI 的函数
    inputs：用于输入的组件（例如"text"、"image"或"audio"）
    outputs：用于输出的组件（例如"text"、"image"或"label"）
"""
demo = gr.Interface(
    fn=greet,
    # 自定义输入文本字段
    inputs=gr.Textbox(lines=2, placeholder="lindaxia study python！"),
    outputs="text")


if __name__ == '__main__':
    demo.launch()
