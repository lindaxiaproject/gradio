import gradio as gr
from transformers import pipeline

"""
    每个 return 语句返回分别对应于food_box和 的两个值status_box。
"""
with gr.Blocks() as demo:
    food_box = gr.Number(value=10, label="Food Count")
    status_box = gr.Textbox()


    def eat(food):
        if food > 0:
            return {food_box: food - 1, status_box: "食物还有剩余"}
        else:
            return {food_box: 0, status_box: "食物光光了，饿～"}


    gr.Button("EAT").click(
        fn=eat,
        inputs=food_box,
        outputs=[food_box, status_box]
    )

if __name__ == '__main__':
    demo.launch()
