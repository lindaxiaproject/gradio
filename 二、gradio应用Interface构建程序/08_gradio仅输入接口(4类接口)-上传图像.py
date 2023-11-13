import random
import string
import gradio as gr

"""
    生成一个随机的文件名，保存至本地
"""
def save_image_random_name(image):
    random_string = ''.join(random.choices(string.ascii_letters, k=20)) + '.png'
    image.save("/Users/linhong/PycharmProjects/gradio/二、gradio应用Interface构建程序/image/" + random_string)
    # Saved image to ZHcoCmKDMCNdVyLKiwxP.png!
    print(f"Saved image to {random_string}!")

demo = gr.Interface(
    fn=save_image_random_name,
    inputs=gr.Image(type="pil"),
    outputs=None,
)


if __name__ == '__main__':
    demo.launch()
