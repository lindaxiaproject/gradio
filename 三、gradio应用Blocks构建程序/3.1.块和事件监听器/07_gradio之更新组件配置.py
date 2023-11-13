import gradio as gr
from transformers import pipeline

"""
    事件监听函数的返回值通常是相应输出组件的更新值。有时我们也想更新组件的配置，例如可见性。
    在本例中，我们返回一个新组件，设置我们想要更改的属性。
    
    通过新gr.Textbox()方法配置文本框本身。该value=参数仍可用于更新组件配置的值

"""

def change_textbox(choice):
    if choice == "短的":
        # 返回的文本框宽度为2，可见，具体的值"继续努力！"
        return gr.Textbox(lines=2, visible=True, value="继续努力！")
    elif choice == "长的":
        return gr.Textbox(lines=8, visible=True, value="你是学霸！")
    else:
        return gr.Textbox(visible=False)


with gr.Blocks() as demo:
    radio = gr.Radio(
        ["短的", "长的", "未知"], label="你想写什么样的论文?"
    )
    text = gr.Textbox(lines=2, interactive=True, show_copy_button=True)
    radio.change(fn=change_textbox, inputs=radio, outputs=text)


if __name__ == '__main__':
    demo.launch()
