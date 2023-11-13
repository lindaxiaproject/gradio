"""
    Gradio 支持的另一种数据持久性类型是会话状态，其中数据在页面会话内的多个提交中持久存在。
    但是，数据不会在模型的不同用户之间共享。要将数据存储在会话状态中。
        1.将一个额外的参数传递到您的函数中，该参数代表接口的状态。
        2.在函数末尾，返回状态的更新值作为额外的返回值。
        3.创建时添加'state'输入和输出组件'state'Interface

    聊天机器人是一个需要会话状态的示例 -
        您希望访问用户之前提交的内容，但不能将聊天历史记录存储在全局变量中，因为这样聊天历史记录会在不同用户之间变得混乱。

"""

import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


def user(message, history):
    return "", history + [[message, None]]


def bot(history):
    user_message = history[-1][0]
    new_user_input_ids = tokenizer.encode(
        user_message + tokenizer.eos_token, return_tensors="pt"
    )

    # 将新的用户输入令牌附加到聊天历史
    bot_input_ids = torch.cat([torch.LongTensor([]), new_user_input_ids], dim=-1)

    # 生成响应
    response = model.generate(
        bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id
    ).tolist()

    # 将标记转换为文本，然后将响应拆分为行
    response = tokenizer.decode(response[0]).split("<|endoftext|>")
    response = [
        (response[i], response[i + 1]) for i in range(0, len(response) - 1, 2)
    ]  # 转换为列表的元组
    history[-1] = response[0]
    return history


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == '__main__':
    demo.launch()
