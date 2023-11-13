import gradio as gr

"""
    向Interface构造函数的关键字参数提供嵌套列表。examples=外部列表中的每个子列表代表一个数据样本，
        子列表中的每个元素代表每个输入组件的输入。每个组件的示例数据的格式在文档中指定。
"""


def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise gr.Error("被除数不能为0！")
        return num1 / num2


demo = gr.Interface(
    calculator,
    [
        "number",
        gr.Radio(["add", "subtract", "multiply", "divide"]),
        "number"
    ],
    "number",
    examples=[
        [45, "add", 3],
        [3.14, "divide", 2],
        [144, "multiply", 2.5],
        [0, "divide", 1.2],

    ],
    # 设置网页标题
    title= "玩具计算器",
    #  左上角的描述文字
    description = "这是一个示例玩具计算器demo",
    # 左下角的文字
    article = "Check out the examples"
)

if __name__ == '__main__':
    demo.launch()
