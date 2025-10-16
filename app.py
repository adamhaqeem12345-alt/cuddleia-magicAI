import gradio as gr
from transformers import pipeline

generator = pipeline("text-generation", model="codellama/CodeLlama-7b-Instruct-hf")

def build(prompt):
    result = generator(f"Generate HTML, CSS, JS, and Supabase Edge Function for: {prompt}", max_new_tokens=700)
    return result[0]["generated_text"]

gr.Interface(fn=build, inputs="text", outputs="text", title="Cuddleia Builder").launch()
