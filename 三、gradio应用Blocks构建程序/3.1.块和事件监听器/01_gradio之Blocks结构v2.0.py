import gradio as gr
"""
    用装饰器附加事件侦听器 - 跳过参数并直接fn分配inputs 、outputs
"""
with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")

    @greet_btn.click(inputs=name, outputs=output)
    def greet(name):
        return "Hello " + name + "!"

if __name__ == '__main__':
    demo.launch()