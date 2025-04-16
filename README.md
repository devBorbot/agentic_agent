## Python Coding Assistant

This repository contains a Python-based coding assistant designed to enhance coding workflows. It leverages AI-powered tools for code suggestions, debugging, documentation generation, and formatting. The assistant can be used interactively via Jupyter notebooks or a Streamlit web interface.

---

### **Features**

- **Code Suggestions**: Provides improvements based on user-defined problems.
- **Debugging Assistance**: Analyzes error messages and suggests fixes.
- **Docstring Generation**: Creates Google-style docstrings for Python functions and classes.
- **Code Formatting**: Formats code using the Black formatter for consistent style.
- **Interactive Usage**:
    - Custom Jupyter magic commands for seamless integration.
    - Web interface powered by Streamlit for user-friendly interaction.

---

### **Files Overview**

#### **1. `coding_agent.py`**

- Initializes the AI model (`HfApiModel`) from Hugging Face.
- Sets up the `CodeAgent` with tools for code suggestions, debugging, docstring generation, and formatting.
- Tools:
    - `code_suggester`: Suggests improvements to provided code.
    - `code_debugger`: Debugs code snippets based on error messages.
    - `docstring_generator`: Generates docstrings for Python functions/classes.
    - `code_formatter`: Formats Python code using Black.


#### **2. `coding_tools.py`**

Contains tool definitions used by the `CodeAgent`:

- **`code_suggester()`**: Provides real-time code improvement suggestions.
- **`code_debugger()`**: Debugs Python code using Pylint analysis.
- **`docstring_generator()`**: Generates Google-style docstrings.
- **`code_formatter()`**: Formats code using the Black library.


#### **3. `jupyter_integration.py`**

Integrates the assistant into Jupyter notebooks via custom magic commands:

- **`init_jupyter()`**: Registers a `%agent` magic command for interacting with the assistant directly in notebooks.
    - *Line Magic*: `%agent &lt;input&gt;` executes tasks based on the input line.
    - *Cell Magic*: `%%agent &lt;input&gt;` processes both line and cell content.


#### **4. `app.py`**

Provides a web-based interface using Streamlit:

- Allows users to input Python code and select tasks (e.g., suggestions, debugging, docstring generation, formatting).
- Displays results interactively with error handling and troubleshooting tips.

---

### **Setup Instructions**

#### **1. Install Dependencies**

Run the following command to install required libraries:

```bash
pip install streamlit torch transformers smolagents black pylint
```


#### **2. Run the Streamlit App**

Start the web interface by running:

```bash
streamlit run app.py
```


#### **3. Use in Jupyter Notebooks**

To enable Jupyter integration:

1. Import and call `init_jupyter()` in your notebook:

```python
from jupyter_integration import init_jupyter
init_jupyter()
```

2. Use `%agent` or `%%agent` magic commands to interact with the assistant.

---

#### **4. Test Code**
1. Suggest Improvements: Improvements are only list comprehension...for now
```python
numbers = []
for i in range(10):
    numbers.append(i)
```

2. Debug
```python
print(x)
```

3. Generate Docs
```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

4. Format Code
```python
def add_numbers(a,b):return a+b
```

---

### **Troubleshooting**

If you encounter issues:

1. Ensure all dependencies are installed (`torch`, `transformers`, etc.).
2. Verify the Hugging Face authentication token is valid in `coding_agent.py`.
3. Restart the application or notebook after resolving errors.

---

## **License**

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). 

You are free to:
- Share: Copy and redistribute the material in any medium or format.
- Adapt: Remix, transform, and build upon the material.

Under the following terms:
- Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- NonCommercial: You may not use the material for commercial purposes.
- ShareAlike: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

For more details, visit [Creative Commons License](https://creativecommons.org/licenses/by-nc-sa/4.0/).


---

### **Acknowledgments**

Powered by Hugging Face's AI models and libraries like Streamlit, Black, and Pylint for enhanced coding workflows.

<div>⁂</div>

[^1]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/61731727/163f08c8-6f5d-48d5-8a0a-263936b22c61/jupyter_integration.py

[^2]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/61731727/2e618efa-4a05-4d5f-a840-2463de43ddcb/coding_tools.py

[^3]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/61731727/fc5ed63f-0a1e-44e4-bf9c-4326181e04a3/app.py

[^4]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/61731727/fd0a3226-69d5-4fbe-95b0-6d6601eafe09/coding_agent.py

