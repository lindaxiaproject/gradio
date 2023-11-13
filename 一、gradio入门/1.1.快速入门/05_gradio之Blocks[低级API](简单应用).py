import gradio as gr
"""
    Gradio 提供了两种构建应用程序的方法：
        1. Interface和ChatInterface，它们为创建demo提供了高级抽象。
        2.Blocks,一种低级的API（定制化）
            用于设计具有更灵活的布局和数据流的 Web 应用程序
            块允许您执行诸如提供多个数据流和演示、控制组件在页面上显示的位置、处理复杂数据流（例如输出可以用作其他函数的输入）以及根据用户交互更新组件的属性/可见性等操作
            仍然都是Python。

    
"""

def greet(name):
    return  "hello " + name + " Nice！"

'''          
     Blocks是由一个子句组成的with，并且在该子句内创建的任何组件都会自动添加到应用程序中   
     组件按照创建的顺序垂直显示在应用程序中。 
     创建了A Button，然后click向该按钮添加了一个事件侦听器。   
'''
with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet.btn = gr.Button("Greet")
    greet.btn.click(fn = greet, inputs=name, outputs=output, api_name="greet")

if __name__ == '__main__':
    demo.launch()