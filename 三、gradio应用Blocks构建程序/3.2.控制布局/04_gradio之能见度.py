import numpy as np
import gradio as gr

"""
组件和布局元素都有一个visible可以初始设置和更新的参数。列上的设置gr.Column(visible=...)可用于显示或隐藏一组组件。
"""
with gr.Blocks() as demo:
    error_box = gr.Textbox(label="Error", visible=False)
    name_box = gr.Textbox(label="姓名")
    age_box = gr.Number(label="年龄", minimum=0, maximum=100)
    # 复选框
    symptoms_box = gr.CheckboxGroup(["咳嗽", "发烧", "流鼻涕"])
    submit_btn = gr.Button("Submit")

    with gr.Column(visible=False) as output_col:
        diagnosis_box = gr.Textbox(label="诊断")
        patient_summary_box = gr.Textbox(label="患者摘要")

    def submit(name, age, symptoms):
        if len(name) == 0:
            return {error_box: gr.Textbox(value="Enter name", visible=True)}
        return {
            output_col: gr.Column(visible=True),
            # symptoms 症状
            diagnosis_box: "新冠肺炎" if "咳嗽" in symptoms else "流感",
            patient_summary_box: f"{name}, {age} y/o",
        }

    submit_btn.click(
        submit,
        [name_box, age_box, symptoms_box],
        [error_box, diagnosis_box, patient_summary_box, output_col],
    )



if __name__ == '__main__':
    demo.launch()

