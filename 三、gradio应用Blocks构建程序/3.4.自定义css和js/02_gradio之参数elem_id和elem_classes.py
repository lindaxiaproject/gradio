"""
    elem_id将 HTML 元素添加id到任何组件，并elem_classes添加一个类或类列表
"""
import gradio as gr

css = """
#warning {background-color: #FFCCCB}
.feedback textarea {font-size: 24px !important}
"""

with gr.Blocks(css=css) as demo:
    box1 = gr.Textbox(value="Good Job", elem_classes="feedback")
    box2 = gr.Textbox(value="Failure", elem_id="warning", elem_classes="feedback")


if __name__ == '__main__':
    demo.launch()