import gradio as gr
from transformers import pipeline

"""
    目前事件侦听器都有一个输入组件。如果您希望多个输入组件将数据传递给函数，则函数如何接受输入组件值有两种选择：
        1.作为参数列表，或者
        2.作为单个值字典，由组件键入
        
"""

with gr.Blocks() as demo:
    a = gr.Number(label="a")
    b = gr.Number(label="b")
    with gr.Row():
        add_btn = gr.Button("Add")
        sub_btn = gr.Button("Subtract")
    c = gr.Number(label="sum")

    def add(num1, num2):
        return num1 + num2
    add_btn.click(add, inputs=[a, b], outputs=c)

    def sub(data):
        return data[a] - data[b]
    sub_btn.click(sub, inputs={a, b}, outputs=c)
'''

    add()将sub()和a作为b输入。但是，这些侦听器之间的语法不同。

        对于add_btn侦听器，我们将输入作为列表传递。该函数add()将每个输入作为参数。值a映射到参数num1，而值b映射到参数num2。
        对于sub_btn侦听器，我们将输入作为一组传递（注意大括号！）。该函数sub()采用单个字典参数data，其中键是输入组件，值是这些组件的值。
'''
if __name__ == '__main__':
    demo.launch()