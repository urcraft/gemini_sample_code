# Gemini AI Code Samples - Getting Started Guide

> **Inspiration:** This repository was inspired by [geminibyexample.com](https://geminibyexample.com/), which provides many more hands-on examples and annotated code for using Gemini models. You can refer to that site for additional useful examples and learning resources.

This repository contains Python code samples demonstrating how to use Google's Gemini AI API for various tasks including text generation, audio transcription, CSV analysis, and creating interactive web interfaces using Gradio (more to come).

## 📋 Prerequisites

Before running these code samples, you'll need:
1. Python installed on your computer
2. A Google API key for Gemini AI
3. Required Python packages installed

## 🐍 Step 1: Install Python

### Download and Install Python
1. Go to [python.org](https://www.python.org/downloads/)
2. Download the latest Python version (3.8 or higher recommended)
3. **IMPORTANT**: During installation, check the box "Add Python to PATH"
4. Complete the installation

### Verify Python Installation
Open Command Prompt (cmd) and run:
```cmd
python --version
```
You should see something like `Python 3.11.x` or similar.

## 🔑 Step 2: Get Your Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API Key" 
4. Create a new API key or use an existing one
5. **Important**: Keep this key safe and never share it publicly

## 💻 Step 3: Set Up Your Development Environment

### Create a Project Folder
Open Command Prompt and navigate to where you want to create your project:
```cmd
cd C:\Users\%USERNAME%\Documents
mkdir gemini_projects
cd gemini_projects
```

### Create a Virtual Environment
A virtual environment keeps your project dependencies separate from other Python projects:
```cmd
python -m venv gemini_env
```

### Activate the Virtual Environment
```cmd
gemini_env\Scripts\activate
```
You should see `(gemini_env)` at the beginning of your command prompt, indicating the virtual environment is active.

### Install Required Packages
With the virtual environment activated, install all required packages:
```cmd
pip install google-genai gradio pandas rich httpx
```

## 🔧 Step 4: Set Up Your API Key

You need to set your Gemini API key as an environment variable. Choose one of these methods:

### Method 1: Set for Current Session (Temporary)
In your activated command prompt:
```cmd
set GOOGLE_API_KEY=your_api_key_here
```
Replace `your_api_key_here` with your actual API key.

### Method 2: Set Permanently (Recommended)
1. Right-click "This PC" or "Computer" → Properties
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Under "User variables", click "New"
5. Variable name: `GOOGLE_API_KEY`
6. Variable value: Your actual API key (get it from https://aistudio.google.com)
7. Click OK and restart your command prompt

## 📁 Step 5: Get the Code Samples

You have several options to obtain the code samples and required files:

### Option 1: Download as ZIP (Easiest)
1. Go to the repository page on GitHub (or wherever the code is hosted).
2. Click the green **Code** button, then select **Download ZIP**.
3. Extract the ZIP file to your desired folder (e.g., `C:\Users\YourName\Documents\gemini_sample_code`).
4. Open Command Prompt or PowerShell and navigate to the extracted folder:
   ```powershell
   cd "C:\Users\YourName\Documents\gemini_sample_code"
   ```

### Option 2: Clone with Git (Recommended for Developers)
If you have Git installed:
1. Open Command Prompt or PowerShell.
2. Navigate to your projects directory:
   ```powershell
   cd "C:\Users\YourName\Documents"
   ```
3. Clone the repository:
   ```powershell
   git clone https://github.com/your-username/gemini_sample_code.git
   cd gemini_sample_code
   ```
   *(Replace the URL with the actual repository URL if different)*

### Option 3: Manual Copy
1. Create a new folder:
   ```powershell
   mkdir gemini_sample_code
   cd gemini_sample_code
   ```
2. Copy and paste the code from each `.py` file in this repository into new files with the same names in your folder.

### Ensure You Have the Sample Files

The following sample files are already included in this repository:
- `test.mp3` (for audio transcription)
- `titanic.csv` (for CSV analysis)

You do NOT need to download or create these files separately—they are provided for you. If you accidentally delete them, you can restore them by re-downloading or re-cloning the repository.

## 🚀 Step 6: Run the Code Samples

Make sure your virtual environment is activated (`(gemini_env)` should be visible in your prompt).

### Sample 1: Hello World
Basic text generation with Gemini:
```cmd
python 1_gemini_hello_world.py
```

### Sample 2: Audio Analysis
Transcribe an MP3 file (make sure `test.mp3` exists in the folder):
```cmd
python 2_gemini_upload_analyze_mp3.py
```

### Sample 3: CSV Analysis
Analyze a CSV file (make sure `titanic.csv` exists in the folder):
```cmd
python 3_gemini_analyse_csv.py
```

### Sample 4: CSV with Code Execution
Advanced CSV analysis with code execution:
```cmd
python 4_gemini_code_execution_csv.py
```

### Sample 5: Interactive Web Interface
Launch a web interface for CSV analysis:
```cmd
python 5_gemini_code_execution_csv_gradio.py
```
This will open a web browser with an interactive interface. You can upload CSV files and ask questions about them.

## 📋 Sample Files Needed

The required sample files (`test.mp3` and `titanic.csv`) are already included in this project repository. You do not need to download or create them separately.

## 🔧 Troubleshooting

### Common Issues and Solutions

**Error: "python is not recognized"**
- Make sure Python is added to your PATH during installation
- Try using `py` instead of `python`

**Error: "No module named 'google'"**
- Make sure your virtual environment is activated
- Run `pip install google-genai` again

**Error: "API key not found"**
- Make sure you've set the `GOOGLE_API_KEY` environment variable
- If using Method 1, set it again in your current session
- If using Method 2, restart your command prompt

**Error: "File not found"**
- Make sure the required files (`test.mp3`, `titanic.csv`) are in the same folder as the Python scripts

**Gradio app not opening**
- Check the terminal output for the local URL (usually `http://127.0.0.1:7860`)
- Try opening it manually in your web browser

## 🛑 When You're Done

### Deactivate Virtual Environment
When you're finished working on the project:
```cmd
deactivate
```

### Reactivating Later
To work on the project again:
```cmd
cd C:\Users\%USERNAME%\Documents\gemini_projects\gemini_sample_code
..\gemini_env\Scripts\activate
```

## 📚 What Each Sample Does

1. **Hello World** (`1_gemini_hello_world.py`): Basic text generation
2. **Audio Analysis** (`2_gemini_upload_analyze_mp3.py`): Transcribes audio files
3. **CSV Analysis** (`3_gemini_analyse_csv.py`): Analyzes and summarizes CSV data
4. **CSV with Code Execution** (`4_gemini_code_execution_csv.py`): Analyzes CSV data and executes Python code
5. **Interactive Web Interface** (`5_gemini_code_execution_csv_gradio.py`): Web interface for CSV analysis

## 💡 Tips for Beginners

- Always activate your virtual environment before running the code
- Keep your API key secret and never commit it to version control
- Start with the hello world example to make sure everything is working
- The Gradio interface (Sample 5) is great for non-programmers to interact with AI
- You can modify the prompts in the code to ask different questions
- If you use PowerShell, you can run the same commands as in Command Prompt, but use `./gemini_env/Scripts/Activate.ps1` to activate the virtual environment
- If you get permission errors in PowerShell, you may need to run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## 🆘 Getting Help

If you encounter issues:
1. Check that all requirements are installed correctly
2. Verify your API key is set up properly
3. Make sure required files are in the correct location
4. Check the terminal output for specific error messages
5. For more help, see the [official Google GenAI Python documentation](https://ai.google.dev/gemini-api/docs/quickstart?hl=en)

Happy coding with Gemini AI! 🤖✨
