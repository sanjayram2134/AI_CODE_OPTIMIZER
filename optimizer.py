import os
from dotenv import load_dotenv

from groq import Groq
from prompt_generator import generate_prompt

load_dotenv()

# Initialize the Groq client
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=api_key)

def optimize_code(code_snippet):
    """
    Uses Groq API and LLaMA3 model to optimize the provided code.
    """
    try:
        # Create the prompt
        prompt = generate_prompt(code_snippet)
        
        # Send request to Groq API
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
            stream=False,
        )
        
        # Extract and return the model's response
        if chat_completion.choices:
            return chat_completion.choices[0].message.content
        else:
            return "No suggestions were provided. Try rephrasing the code."
    except Exception as e:
        return f"An error occurred: {e}"
