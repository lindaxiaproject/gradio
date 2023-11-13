
"""
    流式传输响应，这样用户就不必等待很长时间才能生成消息。
    其次，我们可以让用户消息立即出现在聊天历史记录中，同时生成聊天机器人的响应


    当用户提交消息时，我们现在将三个事件事件链接.then()在一起：

        第一种方法user()使用用户消息更新聊天机器人并清除输入字段。此方法还使输入字段成为非交互式，以便用户在聊天机器人响应时无法发送其他消息。因为我们希望这种情况立即发生，所以我们设置了queue=False，如果启用它，它将跳过任何队列。聊天机器人的历史记录附加有(user_message, None)，None表示机器人尚未响应。
        第二种方法，bot()使用机器人的响应更新聊天机器人历史记录。我们不创建新消息，而是None用机器人的响应替换之前创建的消息。最后，我们逐个字符地构建消息以及yield正在构建的中间输出。Gradio 会自动将带有该yield关键字的任何函数转换为流式输出接口。
        第三种方法使输入字段再次交互，以便用户可以向机器人发送另一条消息。

    当然，在实践中，您可以替换bot()为自己的更复杂的函数，该函数可能会调用预训练的模型或 API，以生成响应。
    最后，我们通过运行启用队列demo.queue()，这是流中间输出所必需的。您可以通过滚动到本页顶部的演示来尝试改进的聊天机器人。

"""

import gradio as gr
import random
import time

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")


    def user(user_message, history):
        return "", history + [[user_message, None]]


    def bot(history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        history[-1][1] = ""
        for character in bot_message:
            history[-1][1] += character
            time.sleep(0.05)
            yield history


    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

demo.queue()
if __name__ == '__main__':
    demo.launch()
