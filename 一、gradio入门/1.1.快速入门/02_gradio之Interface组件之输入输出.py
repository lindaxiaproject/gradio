import gradio as gr


def greet(name, is_morning, temperature):
    solutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{solutation}{name}.It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)

demo = gr.Interface(
        fn=greet,
        inputs=["text", "checkbox", gr.Slider(0, 100)],
        outputs=["text", "number"])

if __name__ == '__main__':
        demo.launch()
