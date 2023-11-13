import gradio as gr


"""
    Gradio 界面自动刷新或连续传输数据
    通过live=True在界面中进行设置，使界面自动刷新。现在，一旦用户输入发生变化，界面就会重新计算。
"""

def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2

demo = gr.Interface(
    calculator,
    [
        "number",
        gr.Radio(["add", "subtract", "multiply", "divide"]),
        "number"
    ],
    "number",
    live=True,
)
if __name__ == '__main__':
    demo.launch()