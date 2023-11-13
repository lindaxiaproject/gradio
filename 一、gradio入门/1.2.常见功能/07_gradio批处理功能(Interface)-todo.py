"""
 Gradio 支持传递批处理函数的能力。批处理函数只是接受输入列表并返回预测列表的函数。

"""
import time
import gradio as gr


# 接受两个输入列表（一个单词列表和一个整数列表），并返回一个修剪单词列表作为输出
def trim_words(words, lens):
    trimmed_words = []
    time.sleep(5)
    for w, l in zip(words, lens):
        trimmed_words.append(w[:int(l)])
    return [trimmed_words]


demo = gr.Interface(trim_words, ["textbox", "number"],outputs=["text"],
                    batch=True, max_batch_size=16)
# 如果启用排队，Gradio 服务器可以自动批处理传入请求并并行处理它们，从而可能加快演示速度。
demo.queue()

if __name__ == '__main__':
    demo.launch()
