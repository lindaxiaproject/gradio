import gradio as gr

"""
    gr.on通过绑定到所有组件的更改事件来创建“实时”事件。如果不指定任何触发器，该函数将自动绑定所有输入组件的change事件。
"""
with gr.Blocks() as demo:
    with gr.Row():
        num1 = gr.Slider(1, 10)
        num2 = gr.Slider(1, 10)
        num3 = gr.Slider(1, 10)
    output = gr.Number(label="Sum")

    @gr.on(inputs=[num1, num2, num3], outputs=output)
    def sum(a, b, c):
        return a + b + c


if __name__ == '__main__':

    demo.launch()