import os
from google import genai
from google.genai import types
import httpx

api_key = os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

with open("titanic.csv", "rb") as f:
    csv_data = f.read()
csv_prompt = "Analyze this data and tell me about the contents. Summarize the data."
csv_response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        types.Part.from_bytes(data=csv_data, mime_type="text/csv"),
        csv_prompt,
    ],
)
print("\nCSV Analysis Result:\n", csv_response.text)
