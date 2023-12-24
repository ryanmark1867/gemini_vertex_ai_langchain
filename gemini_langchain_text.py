# adapted from from https://python.langchain.com/docs/integrations/llms/google_vertex_ai_palm#multimodality
from langchain.llms import VertexAI
from langchain.schema.messages import HumanMessage

#llm = ChatVertexAI(model_name="gemini-pro-vision")
llm = VertexAI(model_name="gemini-pro-vision")
#llm = GeminiProLLM()

image_message = {
    "type": "image_url",
    "image_url": {"url": "test_image_small.png"},
}
text_message = {
    "type": "text",
    "text": "What is shown in this image?",
}
message = HumanMessage(content=[text_message, image_message])

output = llm(message)
print(output.content)