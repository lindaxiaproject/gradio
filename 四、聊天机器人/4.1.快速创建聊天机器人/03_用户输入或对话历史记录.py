

import random
import gradio as gr

"""
    展示了如何合并用户的输入和历史记录
"""
def alternatingly_agree(message, history):
    if len(history) % 2 == 0:
        return f"Yes, I do think that '{message}'"
    else:
        return "I don't think so"

if __name__ == '__main__':
    gr.ChatInterface(alternatingly_agree).launch()