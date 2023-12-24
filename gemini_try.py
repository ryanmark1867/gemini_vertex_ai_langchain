import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part, Image



gemini_pro_vision_model = GenerativeModel("gemini-pro-vision")
image = Image.load_from_file("test_image_small.png")
model_response = gemini_pro_vision_model.generate_content([image,"what is in this image"])
print("model_response\n", model_response)
