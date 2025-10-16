import gradio as gr
from transformers import pipeline

generator = pipeline("text-generation", model="codellama/CodeLlama-13b-Instruct-hf")

def build(prompt):
    result = generator(f"Generate full HTML, CSS, JS and Supabase Edge Functions code for: {prompt}", max_new_tokens=1500)
    return result[0]["generated_text"]

gr.Interface(fn=build, inputs="text", outputs="text", title="Cuddleia Builder").launch()
