"""
    Gradio 支持创建自定义进度条的功能
    为了启用此功能，只需向具有实例默认值的方法添加一个参数即可gr.Progress。
    然后，您可以通过直接使用 0 到 1 之间的浮点数调用此实例来更新进度级别，或者使用实例tqdm()的方法Progress来跟踪可迭代的进度.

"""
import gradio as gr
import time

''' 单词逆序输出 '''


def slowly_reverse(word, progress=gr.Progress()):
    progress(0, desc="Starting")
    time.sleep(1)
    progress(0.05)
    new_string = ""
    for letter in progress.tqdm(word, desc="Reversing"):
        time.sleep(0.25)
        new_string = letter + new_string
    return new_string


demo = gr.Interface(slowly_reverse, gr.Text(), gr.Text())


def same_auth(username, password):
    return username == password




if __name__ == '__main__':
    # show_error为True表示在控制台显示错误信息。
    # demo.launch(server_name='0.0.0.0', server_port=8080, show_error=True)
    ''' 在首次打开网页前，可以设置账户密码。比如auth参数为（账户，密码）的元组数据。这种模式下不能够使用queue函数。'''
    # demo.launch(auth=("admin", "pass1234"))
    '''
        如果想设置更为复杂的账户密码和密码提示，可以通过函数设置校验规则。
    '''
    demo.launch(auth=same_auth, auth_message="username and password must be the same")
