import gradio as gr
"""
   输出
    gr.Error("custom message") 显示错误消息
    gr.Warning("message")
    gr.Info("message")

"""

def start_process(name, success):
    gr.Info("Starting process")
    if name is None:
        gr.Warning("Name is empty")
    if success == False:
        raise gr.Error("Process failed")