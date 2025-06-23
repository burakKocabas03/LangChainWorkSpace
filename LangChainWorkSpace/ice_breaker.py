from dotenv import load_dotenv
import os
from google.cloud import aiplatform
from langchain_google_vertexai import ChatVertexAI


# .env dosyasından ortam değişkenlerini yükle
load_dotenv()

# Vertex AI ortamını başlat (env'den değer alarak)
aiplatform.init(
    project=os.getenv("VERTEX_PROJECT"),
    location=os.getenv("VERTEX_LOCATION")
)

# Artık LLM kullanılabilir
llm = ChatVertexAI(
    model_name="gemini-2.5-flash",
    temperature=0.3
)

response = llm.invoke("Vertex AI nedir?")
print(response)