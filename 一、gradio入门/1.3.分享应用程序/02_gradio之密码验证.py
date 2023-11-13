import gradio as gr

def test(name):
    return "hello" + name + "!"

demo = gr.Interface(
    fn=test,
    inputs=gr.Textbox(lines=2, placeholder="lindaxia study python！"),
    outputs="text")


if __name__ == '__main__':
    demo.launch(auth=("lindaxia", "lindaxia"))