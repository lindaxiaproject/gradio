"""

    渐变主题是自定义应用程序外观的最简单方法,请将theme=kwarg 传递给Blocks构造函数。例如：
    with gr.Blocks(theme=gr.themes.Glass()):
    ...

    Gradio 应用程序的基类是gradio-container，因此这里有一个更改 Gradio 应用程序背景颜色的示例：
    with gr.Blocks(css=".gradio-container {background-color: red}") as demo:
    ...

    在 css 中引用外部文件，请在文件路径（可以是相对路径或绝对路径）前面加上"file="，例如：
    with gr.Blocks(css=".gradio-container {background: url('file=clouds.jpg')}") as demo:
    ...

"""