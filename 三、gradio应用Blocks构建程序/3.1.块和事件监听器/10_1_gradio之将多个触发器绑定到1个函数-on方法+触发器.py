import gradio as gr

"""
    允许用户单击提交按钮，或按 Enter 键提交表单。您可以使用该gr.on方法并将触发器列表传递给trigger.
"""
with gr.Blocks() as demo:
    name = gr.Textbox(label="请输入您的姓名")
    output = gr.Textbox(label="输出信息")
    greet_btn = gr.Button("提交")

    def greet(name):
        return "Hello " + name + "!"

    gr.on(
        triggers=[name.submit, greet_btn.click],
        fn=greet,
        inputs=name,
        outputs=output,
    )


if __name__ == '__main__':

    demo.launch()