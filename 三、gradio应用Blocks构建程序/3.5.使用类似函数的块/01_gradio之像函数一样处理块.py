import gradio as gr

from transformers import pipeline

"""
    将英语文本翻译为德语文本
"""
pipe = pipeline("translation", model="t5-base")
def translate(text):
    return pipe(text)[0]["translation_text"]

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            english = gr.Textbox(label="英语文本")
            translate_btn = gr.Button(value="翻译")
        with gr.Column():
            german = gr.Textbox(label="德语文本")

    translate_btn.click(translate, inputs=english, outputs=german, api_name="translate-to-german")
    examples = gr.Examples(examples=["I went to the supermarket yesterday.", "Helen is a good swimmer."],
                           inputs=[english])

if __name__ == '__main__':
    demo.launch()