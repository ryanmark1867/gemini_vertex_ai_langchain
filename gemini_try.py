import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part, Image

project_id = "gemini-test-dec-2023b"
location = ""

def generate_text(project_id: str, location: str) -> str:
    # Initialize Vertex AI
    #vertexai.init(project=project_id, location=location)
    # Load the model
    multimodal_model = GenerativeModel("gemini-pro-vision")
    # Query the model
    response = multimodal_model.generate_content(
        [
            # Add an example image
            Part.from_uri(
                "gs://cloud-samples-data/ai-platform/flowers/daisy/10559679065_50d2b16f6d.jpg", mime_type="image/jpeg"
                #"gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"
            ),
            # Add an example query
            "what is shown in this image?",
        ]
    )
    print(response)
    return response.text

gemini_pro_vision_model = GenerativeModel("gemini-pro-vision")
image = Image.load_from_file("test_image_small.png")
#image = Part.from_uri("gs://cloud-samples-data/ai-platform/flowers/daisy/10559679065_50d2b16f6d.jpg", mime_type="image/jpeg")
model_response = gemini_pro_vision_model.generate_content([image,"what is in this image"])
print("model_response\n", model_response)
