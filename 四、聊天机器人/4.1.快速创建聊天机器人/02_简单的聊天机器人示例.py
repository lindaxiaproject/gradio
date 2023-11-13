

'''
    (1)示例：回答“是”或“否”的聊天机器人
    编写一个响应Yes或No随机的聊天功能
'''

import random
import gradio as gr

def random_response(message, history):
    return random.choice(["Yes", "No"])

if __name__ == '__main__':
    gr.ChatInterface(random_response).launch()