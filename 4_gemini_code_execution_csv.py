from google import genai
from google.genai import types
import os
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.panel import Panel

console = Console()

# Initialize the Gemini client
api_key = os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

# Read the CSV file
with open("titanic.csv", "rb") as f:
    csv_data = f.read()

# Create the prompt to analyze average age
prompt = """Analyze this CSV data and calculate the average age of passengers. 
Generate and run Python code to:
1. Read the CSV data using pandas
2. Calculate and return the mean age, excluding any null values
3. Round the result to 2 decimal places"""

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

# Process and display the response parts
for part in response.candidates[0].content.parts:
    if part.text is not None:
        console.print(Markdown(part.text))

    if part.executable_code is not None:
        code = part.executable_code.code
        language = (
            "python"
            if "def " in code or "import " in code or "print(" in code
            else "text"
        )
        console.print(
            Panel(
                Syntax(code, language, theme="monokai", line_numbers=True),
                title="Code",
                border_style="blue",
            )
        )

    if part.code_execution_result is not None:
        console.print(
            Panel(
                part.code_execution_result.output,
                title="Output",
                border_style="green",
            )
        )

    if part.inline_data is not None:
        console.print(
            "[yellow]Image data available but cannot be displayed in terminal[/yellow]"
        )

    console.print("---")