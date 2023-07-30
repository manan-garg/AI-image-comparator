import io
from PIL import Image
from IPython.display import Image as IPImage
import requests
import json
import gradio as gr 

model_id_list = ['stablediffusionapi/dreamshaper-v7', 'runwayml/stable-diffusion-v1-5', 'stabilityai/stable-diffusion-2-1', 'digiplay/DreamShaper_7', 'hakurei/waifu-diffusion']

#Text-to-image endpoint
def get_completion(inputs, model_id, hf_api_key, parameters=None):
    ENDPOINT_URL='https://api-inference.huggingface.co/models/{}'.format(model_id)
    headers = {
      "Authorization": f"Bearer {hf_api_key}",
      "Content-Type": "application/json"
    }   
    data = { "inputs": inputs }
    if parameters is not None:
        data.update({"parameters": parameters})
    response = requests.request("POST",
                                ENDPOINT_URL,
                                headers=headers,
                                data=json.dumps(data))
    if 'error' in str(response.content):
        return None
    else:
        return IPImage(response.content)

# A helper function to convert the bytes string into PIL image to send to API
def bytes_to_pil_image(img_bytes):
    byte_stream = io.BytesIO(img_bytes)
    pil_image = Image.open(byte_stream)
    return pil_image

def generate(hf_api_key, prompt):
    outputs = []
    for model_id in model_id_list:
        output = get_completion(prompt, model_id, hf_api_key)
        if output == None:
            outputs.append(output)
        else:
            pil_image = bytes_to_pil_image(output.data)  # Use the corrected function here
            outputs.append(pil_image)
    return outputs

with gr.Blocks() as demo:
    gr.Markdown("# AI Image Comparator")
    with gr.Row():
        hf_api_key = gr.Textbox(label="Hugging Face API Key")
    with gr.Row():
        with gr.Column(scale=4):
            prompt = gr.Textbox(label="Your prompt to generate image") #Give prompt some real estate
        with gr.Column(scale=1, min_width=50):
            btn = gr.Button("Submit") #Submit button side by side!
    with gr.Row():
        with gr.Column():
            output1 = gr.Image(label= model_id_list[0])
        with gr.Column():
            output2 = gr.Image(label= model_id_list[1])
    with gr.Row():
        with gr.Column():
            output3 = gr.Image(label= model_id_list[2])
        with gr.Column():
            output4 = gr.Image(label= model_id_list[3])
        with gr.Column():
            output5 = gr.Image(label= model_id_list[4])
    btn.click(fn=generate, inputs=[hf_api_key, prompt], outputs=[output1,output2,output3,output4,output5])
gr.close_all()
demo.launch()