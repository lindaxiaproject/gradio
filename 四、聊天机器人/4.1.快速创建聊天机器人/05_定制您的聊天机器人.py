"""
    Gradio 的Interface类，它gr.ChatInterface包含许多相同的参数，我们可以定义聊天机器人的外观和感觉。
        title：使用和参数在聊天机器人上方添加标题和描述description。
        theme：分别使用和参数添加主题或自定义 css css。
        添加examples甚至启用cache_examples，让用户更容易试用。
        可以更改文本或禁用聊天机器人界面中显示的每个按钮：submit_btn、retry_btn、undo_btn、clear_btn。

"""

import gradio as gr

def yes_man(message, history):
    if message.endswith("?"):
        return "Yes"
    else:
        return "Ask me anything!"

demo =gr.ChatInterface(
    yes_man,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="问我一个Yes或No的问题", container=False, scale=7),
    title="定制聊天机器人",
    description="您可以问我任何问题～",
    theme="soft",
    examples=["Hello", "Am I cool?", "Are tomatoes vegetables?"],
    cache_examples=True,
    retry_btn=None,
    undo_btn="删除上一个对话",
    clear_btn="清除本次对话",
)

if __name__ == '__main__':
    demo.launch()