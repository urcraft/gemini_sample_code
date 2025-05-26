import gradio as gr
from google import genai
from google.genai import types
import os
import tempfile

# Initialize the Gemini client
api_key = os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

def analyze_csv(csv_file, prompt):
    # Read the uploaded file
    if hasattr(csv_file, 'name'):
        with open(csv_file.name, 'rb') as f:
            csv_data = f.read()
    else:
        return "Please upload a CSV file"
    
    # Generate content with code execution enabled
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            types.Part.from_bytes(data=csv_data, mime_type="text/csv"),
            prompt,
        ],
        config=types.GenerateContentConfig(
            tools=[types.Tool(code_execution=types.ToolCodeExecution)]
        ),
    )
      # Process the response parts
    output = []
    for part in response.candidates[0].content.parts:
        if part.text is not None:
            output.append(f"### Analysis:\n{part.text}")
            
        if part.executable_code is not None:
            output.append(f"\n### Generated Code:\n```python\n{part.executable_code.code}\n```")
            
        if part.code_execution_result is not None:
            output.append(f"\n### Execution Result:\n```\n{part.code_execution_result.output}\n```")
    
    return "\n".join(output)

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# CSV Analysis with Gemini AI")
    
    with gr.Row():
        with gr.Column():
            file_input = gr.File(
                label="Upload CSV File",
                file_types=[".csv"]
            )
            prompt_input = gr.Textbox(
                label="Enter your analysis prompt",
                #placeholder="""Analyze this CSV data and calculate the average age of passengers. Generate and run Python code to: 
                #1. Read the CSV data using pandas
                #2. Calculate and return the mean age, excluding any null values
                #3. Round the result to 2 decimal places""",
                value="""Analyze this CSV data and calculate the average age of passengers. Generate and run Python code to: 
                1. Read the CSV data using pandas
                2. Calculate and return the mean age, excluding any null values
                3. Round the result to 2 decimal places""",
                lines=3
            )
            analyze_button = gr.Button("Analyze")
            
        with gr.Column():
            output_text = gr.Markdown(
                value="Results will appear here...",
                label="Analysis Results"
            )
    
    analyze_button.click(
        fn=analyze_csv,
        inputs=[file_input, prompt_input],
        outputs=[output_text]
    )

if __name__ == "__main__":
    demo.launch()