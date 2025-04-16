# coding_tools.py

from smolagents import tool
import black
import pylint.lint

@tool
def code_suggester(code: str, problem: str) -> str:
    """
    Provides real-time code suggestions based on the provided code and problem description.

    Args:
        code (str): The Python code to analyze for improvements.
        problem (str): A description of the specific issue or area of improvement in the code.

    Returns:
        str: A suggestion for improving the provided code based on the described problem.
    """
    return f"Suggested improvement for {problem}:\n# Consider using list comprehensions here"

@tool
def code_debugger(error_message: str, code_snippet: str) -> str:
    """
    Analyzes error messages and provides debugging suggestions for the given code snippet.

    Args:
        error_message (str): The error message encountered during code execution.
        code_snippet (str): The Python code snippet to debug.

    Returns:
        str: Debugging suggestions based on an analysis of the provided code snippet.
    """
    pylint_results = pylint.lint.Run([code_snippet], do_exit=False)
    return f"Debugging suggestions:\n{pylint_results.linter.stats['by_msg']}"

@tool
def docstring_generator(code: str) -> str:
    """
    Generates Google-style docstrings for Python functions based on the provided code.

    Args:
        code (str): The Python function or class definition for which a docstring is needed.

    Returns:
        str: A generated docstring in Google-style format.
    """
    return "Generated docstring:\n\"\"\"Example function\nArgs:\n param: Example parameter\nReturns:\n Example return value\"\"\""

@tool
def code_formatter(code: str) -> str:
    """
    Formats Python code using the Black formatter to ensure consistent style and readability.

    Args:
        code (str): The Python code to format.

    Returns:
        str: The formatted Python code as a string.
    """
    return black.format_str(code, mode=black.FileMode())

