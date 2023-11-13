"""
    应用预计流量很大，请使用该queue()方法来控制处理速率。这会将调用排队，以便一次仅处理一定数量的请求。
        队列使用 websockets，这也可以防止网络超时，因此如果函数的推理时间很长（> 1 分钟），则应该使用队列。

    与Interface
        demo = gr.Interface(...).queue()
        demo.launch()

    与Blocks：
        with gr.Blocks() as demo:
        #...
        demo.queue()
        demo.launch()

    控制一次处理的请求数量
    
    with gr.Blocks() as demo:
        btn = gr.Button("Run")
        btn.click(..., concurrency_limit=2)

"""