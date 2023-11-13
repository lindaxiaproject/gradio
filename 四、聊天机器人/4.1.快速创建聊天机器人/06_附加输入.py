

import gradio as gr
import time


"""
参数additional_inputs接受一个组件或组件列表。您可以直接传递组件实例
，或使用它们的字符串快捷方式（例如"textbox"代替gr.Textbox()）。
如果您传入组件实例，并且它们尚未渲染，那么组件将出现在gr.Accordion().
 您可以使用参数设置此手风琴的标签additional_inputs_accordion_name。
"""
def echo(message, history, system_prompt, tokens):
    response = f"System prompt: {system_prompt}\n Message: {message}."
    for i in range(min(len(response), int(tokens))):
        time.sleep(0.05)
        yield response[: i+1]

demo = gr.ChatInterface(echo,
                        additional_inputs=[
                            gr.Textbox("你是一个有用的AI", label="系统提示词"),
                            gr.Slider(10, 100)
                        ]
                       )

if __name__ == '__main__':
    demo.queue().launch()