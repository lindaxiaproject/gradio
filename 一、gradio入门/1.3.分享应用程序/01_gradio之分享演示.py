import gradio as gr
"""
    share=True通过在方法中进行设置，可以轻松公开共享 Gradio 演示launch()

"""
def test(name):
    return "hello" + name + "!"

demo = gr.Interface(
    fn=test,
    # 自定义输入文本字段
    inputs=gr.Textbox(lines=2, placeholder="lindaxia study python！"),
    outputs="text")

# def same_auth(username, password):
#     return username == password
# demo.launch(auth=same_auth)





if __name__ == '__main__':
    # Running on local URL:  http://127.0.0.1:7862
    ''' This share link expires in 72 hours. '''
    demo.launch(share=True)