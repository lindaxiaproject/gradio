import gradio as gr

def greet(name):
    return "Hello " + name + "!"

"""
 充当事件侦听器输入的任何组件都是交互式的。但是，由于 Textbox output仅充当输出，
 因此 Gradio 确定不应将其设置为交互式。
 
 您可以覆盖默认行为并使用布尔interactive关键字参数直接配置组件的交互性。
"""
with gr.Blocks() as demo:
    # 输入文本框
    name = gr.Textbox(label="姓名")
    # 输出文本框
    output = gr.Textbox(label="输出盒", interactive=True)
    # 按钮
    greet_btn = gr.Button("Greet")
    #  创建了greet_btn，然后click向该按钮添加了一个事件侦听器。
    # 事件侦听器定义应用程序内的数据流。在上面的示例中，侦听器将两个文本框连接在一起。
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

if __name__ == '__main__':
    demo.launch()