import gradio as gr

def chatbot_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_new_tokens=50)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

gr.Interface(fn=chatbot_response, inputs="text", outputs="text").launch()
