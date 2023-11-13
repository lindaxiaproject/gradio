import gradio as gr

def greet(name):
    return "Hello " + name + "!"


with gr.Blocks() as demo:
    # 输入文本框
    name = gr.Textbox(label="姓名")
    # 输出文本框
    output = gr.Textbox(label="输出盒")
    # 按钮
    greet_btn = gr.Button("Greet")
    #  创建了greet_btn，然后click向该按钮添加了一个事件侦听器。
    # 事件侦听器定义应用程序内的数据流。在上面的示例中，侦听器将两个文本框连接在一起。
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

if __name__ == '__main__':
    demo.launch()