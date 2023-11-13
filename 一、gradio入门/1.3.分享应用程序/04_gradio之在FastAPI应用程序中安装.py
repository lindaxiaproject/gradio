from fastapi import  FastAPI
import gradio as gr

CUSTOM_PATH = "/test_gradio"

# 创建 fastapi 对象
app = FastAPI()


# 定义路由 ---- 访问根路径返回指定内容
@app.get("/")
def read_main():
    return {"msg": "林大侠是最棒的！"}

io = gr.Interface(lambda x:"Hello," + x + "!", "textbox","textbox")
app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)


"""
    cd /Users/linhong/PycharmProjects/gradio/1.3.分享应用程序
    
    (venv) (base) linhong@linhong-mbp 1.3.分享应用程序 % uvicorn 04_gradio之在FastAPI应用程序中安装:app
    INFO:     Started server process [37576]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    
    
    http://127.0.0.1:8000/test_gradio/

"""
# 启动项目
# uvicorn 04_gradio之在FastAPI应用程序中安装:app

# 带Debug模式启动命令 ： uvicorn 01hello_world:app --reload
