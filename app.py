import gradio as gr
from transformers import pipeline
pipe = pipeline('text2text-generation',model="facebook/m2m100_418M")

def generate_text(inp):
    output = pipe(inp,forced_bos_token_id =pipe.tokenizer.get_lang_id("ta"))
    
    return output[0]['generated_text']

output_text = gr.outputs.Textbox()
gr.Interface(generate_text,"textbox", output_text).launch()
