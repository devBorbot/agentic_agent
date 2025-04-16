# coding_agent.py

# Import necessary classes and tools from external libraries
from smolagents import CodeAgent, HfApiModel  # CodeAgent handles coding tasks and HfApiModel provides access to a specific AI model.
from coding_tools import code_suggester, code_debugger, docstring_generator, code_formatter  # Import tools for various coding functionalities.
import os

# Load environment variables from the system
from dotenv import load_dotenv
load_dotenv()  # Load variables from .env file if present

# Debugging: Print the token to verify it's loaded
print(f"Token loaded: {os.getenv('HF_API_TOKEN') is not None}")

token = os.getenv("HF_API_TOKEN")
if token is None or token == "":
    raise ValueError("HF_API_TOKEN environment variable is not set or empty.")

# Initialize the AI model using HfApiModel
# The model_id specifies the identifier for the model hosted on Hugging Face's API.
# The token is an authentication key required to access the model.
model = HfApiModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",  # Model ID for the Qwen2.5-Coder-32B-Instruct AI model.
    token=token  # Authentication token for accessing the Hugging Face API.
)

# Create an instance of CodeAgent to perform coding-related tasks
coding_agent = CodeAgent(
    tools=[code_suggester, code_debugger, docstring_generator, code_formatter],  # List of tools for enhancing coding workflows:
    # - code_suggester: Suggests improvements or additions to code.
    # - code_debugger: Identifies and resolves issues in code.
    # - docstring_generator: Generates documentation strings for functions and classes.
    # - code_formatter: Formats code according to style guidelines.
    model=model,  # Assign the initialized AI model to the agent.
    add_base_tools=True  # Include additional base tools provided by the CodeAgent class.
)

