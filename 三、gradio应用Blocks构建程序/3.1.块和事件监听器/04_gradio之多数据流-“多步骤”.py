import gradio as gr
from transformers import pipeline

"""
    这是一个“多步骤”演示的示例，其中一个模型（语音到文本模型）的输出被输入到下一个模型（情感分类器）。
"""

asr = pipeline("automatic-speech-recognition", "facebook/wav2vec2-base-960h")
classifier = pipeline("text-classification")

def speech_to_text(speech):
    text = asr(speech)["text"]
    return text

def text_to_sentiment(text):
    return classifier(text)[0]["label"]

demo = gr.Blocks()

with demo:
    audio_file = gr.Audio(type="filepath")
    text = gr.Textbox()
    label = gr.Label()

    b1 = gr.Button("识别语音")
    b2 = gr.Button("情绪分类")

    b1.click(speech_to_text, inputs=audio_file, outputs=text)
    b2.click(text_to_sentiment, inputs=text, outputs=label)

if __name__ == '__main__':
    demo.launch()