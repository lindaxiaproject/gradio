import gradio as gr
import random



"""
    Gradio 包含一个高级类,gr.ChatInterface它与 类似gr.Interface，但专门为聊天机器人UI设计。
        该类gr.ChatInterface还包装了一个函数，但该函数必须具有特定的签名。
        该函数应采用两个参数：message然后history（参数可以命名为任何名称，但必须按此顺序）

    message: astr代表用户的输入
    history:list表示list截至该点的对话。每个内部列表由两个str代表一对：[user input, bot response]。
    
    报错：AttributeError: module 'backend_interagg' has no attribute 'FigureCanvas'
    pip uninstall matplotlib
    pip install matplotlib==3.5.0

"""
def random_reponse(message, history):
    return random.choice(["Yes","No"])

demo =gr.ChatInterface(random_reponse)

if __name__ == '__main__':
    demo.launch()