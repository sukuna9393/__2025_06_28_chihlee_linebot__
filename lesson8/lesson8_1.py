import gradio as gr

def greet(name, intensity):
    return  name + "您好" + "!" * int(intensity)

demo = gr.Interface(    
    inputs=["text", "slider"],
    outputs=["text"],
    fn=greet
)

demo.launch(share=True)
