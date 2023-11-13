"""
    构造函数中有三个参数Interface来指定此内容的位置：

        title：接受文本并可以将其显示在界面的最顶部，并且也成为页面标题。
        description: 接受文本、Markdown 或 HTML 并将其放置在标题的正下方。
        article：它也接受文本、Markdown 或 HTML 并将其放置在界面下方。


    使用BlocksAPI，则可以使用gr.Markdown(...)或gr.HTML(...)组件在任何位置插入文本、Markdown 或 HTML，
        并在Component构造函数内添加描述性内容

        关键字参数是label=，它出现在 every 中Component。这会修改每个 顶部的标签文本Component
        gr.Number(label='Age', info='In years, must be greater than 0')
"""