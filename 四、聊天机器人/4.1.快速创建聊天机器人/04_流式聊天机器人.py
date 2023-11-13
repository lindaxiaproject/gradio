

import time
import gradio as gr

"""
    用来yield生成一系列响应，最终将得到一个流式聊天机器人
    
    我们已经启用了队列，这是使用生成器函数所必需的。当响应流式传输时，“提交”按钮变成“停止”按钮，可用于停止生成器功能。
    您可以使用参数自定义“停止”按钮的外观和行为stop_btn。
"""
def slow_echo(message, history):
    for i in range(len(message)):
        time.sleep(0.3)
        yield "您发送的消息: " + message[: i+1]

if __name__ == '__main__':
    gr.ChatInterface(slow_echo).queue().launch()