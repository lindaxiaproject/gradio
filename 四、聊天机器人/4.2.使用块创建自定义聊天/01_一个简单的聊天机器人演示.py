

import gradio as gr
import random
import time
"""
    三个 Gradio 组件：
        A Chatbot，其值存储对话的整个历史记录，作为用户和机器人之间的响应对列表。
        用户可以在Textbox其中键入消息，然后按 Enter/提交以触发聊天机器人响应
        ClearButton用于清除文本框和整个聊天机器人历史记录的按钮
"""
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    '''
    respond()它接收聊天机器人的整个历史记录，附加一条随机消息，等待 1 秒，然后返回更新的聊天历史记录。
    该respond()函数返回时还会清除文本框。
    '''
    def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))
        time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()