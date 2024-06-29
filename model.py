from transformers import StableDiffusionPipeline
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the pre-trained Stable Diffusion model from Hugging Face
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to(device)


prompt = "A futuristic cityscape at sunset"
image = pipe(prompt).images[0]

image.save("generated_image.png")


image.show()
