import streamlit as st  # Import Streamlit for creating web-based interactive applications.
from coding_agent import coding_agent  # Import the CodeAgent instance for executing coding tasks.
import os

# Load environment variables from the system (for Streamlit compatibility)
from dotenv import load_dotenv
load_dotenv()  # Load variables from .env file if present

# Debugging: Print the token to verify it's loaded
st.write(f"Token loaded: {os.getenv('HF_API_TOKEN') is not None}")

# Set up the Streamlit app interface
st.title("🤖 Python Coding Assistant")  # Display the app title.
st.caption("Powered by Hugging Face smolagents")  # Add a caption describing the app's underlying technology.

# Check if coding_agent is properly initialized
if coding_agent is None:
    st.error("""\n
    🔴 Agent initialization failed!\n
    Check terminal for error details.\n
    Common fixes:\n
    1. Install requirements: `pip install torch transformers`\n
    2. Restart the app\n
    """)  # Display an error message with troubleshooting steps if the agent is not initialized.
    st.stop()  # Stop further execution of the app.

# Input section for user-provided Python code
code_input = st.text_area("Enter your Python code:", height=200)  # Create a text area for users to input their Python code.

# Dropdown menu for selecting the task to perform on the code
task = st.selectbox(
    "Select task:",
    # these tasks are not exactly named as the CodeAgent variables in coding_agent.py
    # CodeAgent has NLP capabilities to match and keep user-friendly names
    ["Suggest Improvements", "Debug", "Generate Docs", "Format Code"]  # List of available tasks for the CodeAgent.
)

# Button to execute the selected task using the CodeAgent
if st.button("Execute"):  # When the "Execute" button is clicked:
    with st.spinner("Agent is working..."):  # Display a spinner while processing.
        try:
            # Run the selected task on the provided code using the CodeAgent
            response = coding_agent.run(f"{task} for this code: {code_input}")
            
            # Display the agent's response as formatted Python code
            st.code(response, language="python")
        except Exception as e:
            # Handle errors and display an error message if something goes wrong
            st.error(f"Agent error: {str(e)}")

