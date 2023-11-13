from time import sleep

import gradio as gr
import numpy as np
from pydub import AudioSegment

"""
    Gradio 界面自动刷新或连续传输数据
        流式传输意味着数据不断发送到后端并且Interface函数不断重新运行
        
    网络摄像头的流图像的示例代码
"""

with gr.Blocks() as demo:
    input_audio = gr.Audio(label="Input Audio", type="filepath", format="mp3")
    with gr.Row():
        with gr.Column():
            stream_as_file_btn = gr.Button("Stream as File")
            format = gr.Radio(["wav", "mp3"], value="wav", label="Format")
            stream_as_file_output = gr.Audio(streaming=True)

            def stream_file(audio_file, format):
                audio = AudioSegment.from_file(audio_file)
                i = 0
                chunk_size = 1000
                while chunk_size * i < len(audio):
                    chunk = audio[chunk_size * i : chunk_size * (i + 1)]
                    i += 1
                    if chunk:
                        file = f"/tmp/{i}.{format}"
                        chunk.export(file, format=format)
                        yield file
                        sleep(0.5)

            stream_as_file_btn.click(
                stream_file, [input_audio, format], stream_as_file_output
            )

            gr.Examples(
                [["audio/cantina.wav", "wav"], ["audio/cantina.wav", "mp3"]],
                [input_audio, format],
                fn=stream_file,
                outputs=stream_as_file_output,
                cache_examples=True,
            )

        with gr.Column():
            stream_as_bytes_btn = gr.Button("Stream as Bytes")
            stream_as_bytes_output = gr.Audio(format="bytes", streaming=True)

            def stream_bytes(audio_file):
                chunk_size = 20_000
                with open(audio_file, "rb") as f:
                    while True:
                        chunk = f.read(chunk_size)
                        if chunk:
                            yield chunk
                            sleep(1)
                        else:
                            break
            stream_as_bytes_btn.click(stream_bytes, input_audio, stream_as_bytes_output)


if __name__ == '__main__':
    demo.queue().launch()