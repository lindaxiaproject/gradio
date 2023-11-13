"""
  全局状态
    函数可能会使用在单个函数调用之外持续存在的数据。如果所有函数调用和所有用户都可以访问数据，则可以在函数调用外部创建一个变量并在函数内部访问它。
    例如，您可以在函数外部加载一个大型模型并在函数内部使用它，这样每次函数调用都不需要重新加载模型。

"""
import gradio as gr
# scores数组在所有用户之间共享
scores = []

def track_score(score):
    scores.append(score)
    top_scores = sorted(scores, reverse=True)[:3]
    return top_scores

demo = gr.Interface(
    track_score,
    gr.Number(label="Score"),
    gr.JSON(label="Top Scores")
)

if __name__ == '__main__':
    demo.launch()