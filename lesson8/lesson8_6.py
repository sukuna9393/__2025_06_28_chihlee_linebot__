import gradio as gr

#建立gradio Blocks架構
with gr.Blocks() as demo:
   gr.Markdown("## 公司內部機器人")
   #建立輸入框
   input_text = gr.Textbox(label="請輸入訊息", placeholder="請輸入問題", submit_btn=True)

demo.launch()