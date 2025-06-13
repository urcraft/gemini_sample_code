import os
from google import genai
from google.genai import types

api_key = os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)
image_path = "./sample.jpg"
with open(image_path, "rb") as image_file:
    image_content = image_file.read()
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Describe this image in detail.", types.Part.from_bytes(data=image_content, mime_type="image/jpeg")]
)

print("Response using Part.from_bytes:\n", response.text)

