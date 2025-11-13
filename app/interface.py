"""
Empathetic Assistant – Mental Health Dialogue
---------------------------------------------
Launch the Gradio interface directly with:
    python app/interface.py
"""

import os
import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# === Paths (relative to project root) ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "notebooks", "distilgpt2-empathetic-finetuned-v2")

# === Load Fine-Tuned Dialogue Model (DistilGPT-2) ===
print(f"Loading dialogue model from: {MODEL_PATH}")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

# Ensure pad_token exists
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': tokenizer.eos_token})
    model.resize_token_embeddings(len(tokenizer))

# === Load Emotion Detection Model (DistilBERT) ===
print("Loading emotion classifier...")
emotion_model_name = "bhadresh-savani/distilbert-base-uncased-emotion"
emotion_analyzer = pipeline(
    "text-classification",
    model=emotion_model_name,
    tokenizer=emotion_model_name,
    return_all_scores=False
)

# === Response Generation Function ===
def generate_response(user_input, temperature, max_len):
    """Generate empathetic response + emotion detection."""
    if not user_input.strip():
        return "Veuillez écrire quelque chose pour commencer la conversation."

    # Emotion detection
    emotion_result = emotion_analyzer(user_input)[0]
    detected_emotion = emotion_result['label']

    # Generate empathetic response
    input_text = f"User: {user_input}\nAssistant:"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    output = model.generate(
        input_ids,
        max_length=int(max_len),
        temperature=float(temperature),
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95
    )

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    response = response.replace(input_text, "").strip()
    return f"{response}\n\n[Emotion détectée : {detected_emotion}]"

# === Gradio UI ===
def launch_app():
    with gr.Blocks(title="Empathetic Assistant — Mental Health Dialogue") as demo:
        gr.Markdown("##  Assistant Empathique — Bien-être et Dialogue")
        gr.Markdown(
            "Cet assistant utilise **DistilGPT-2** fine-tuné et **DistilBERT** pour détecter les émotions et générer des réponses bienveillantes."
        )

        with gr.Row():
            with gr.Column(scale=3):
                user_input = gr.Textbox(
                    label="Exprimez ce que vous ressentez",
                    placeholder="Exemple : I feel anxious about my future...",
                    lines=3
                )
                temperature = gr.Slider(0.5, 1.2, value=0.8, step=0.1, label="Créativité (temperature)")
                max_len = gr.Slider(50, 200, value=120, step=10, label="Longueur maximale de la réponse")
                submit_btn = gr.Button("Envoyer")

            with gr.Column(scale=2):
                output_box = gr.Textbox(label="Réponse de l'assistant", lines=6)

        submit_btn.click(generate_response, inputs=[user_input, temperature, max_len], outputs=output_box)

    demo.launch(server_name="0.0.0.0", server_port=7861, share=False)


# === Entry Point ===
if __name__ == "__main__":
    print(" Launching Gradio Interface...")
    launch_app()
