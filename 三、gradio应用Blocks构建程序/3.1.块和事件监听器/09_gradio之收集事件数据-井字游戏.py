"""
    将关联的事件数据类作为类型提示添加到事件侦听器函数中的参数来收集有关事件的特定数据


    例如，事件数据.select()可以通过参数进行类型提示gradio.SelectData。
当用户选择触发组件的某些部分时会触发该事件，并且事件数据包括有关用户具体选择的内容的信息。
如果用户选择 a 中的特定单词Textbox、a 中的特定图像Gallery或 a 中的特定单元格DataFrame，则事件数据参数将包含有关特定选择的信息。
"""

import gradio as gr

with gr.Blocks() as demo:
    turn = gr.Textbox("X", interactive=False, label="Turn")
    board = gr.Dataframe(value=[["", "", ""]] * 3, interactive=False, type="array")

    def place(board, turn, evt: gr.SelectData):
        if evt.value:
            return board, turn
        board[evt.index[0]][evt.index[1]] = turn
        turn = "O" if turn == "X" else "X"
        return board, turn

    board.select(place, [board, turn], [board, turn], show_progress="hidden")

if __name__ == '__main__':

    demo.launch()