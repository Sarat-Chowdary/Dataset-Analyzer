import os
import json
import pandas as pd
import traceback as tb

from langchain.agents import initialize_agent, Tool, AgentType
from langchain.prompts import PromptTemplate
from langchain.prompts import PromptTemplate

from tools.tools import execute_on_dataframe, retrieve_dataframe_meta
from llm.chat_agent import ChatLLM


execute_tool = Tool(
    name="execute_on_dataframe",
    func=execute_on_dataframe.run,  
    description=(
        "Executes python code on the loaded dataframe and returns results as JSON."
        "Input is a string containing Python code assigning the final output to 'result'."
    )
)

meta_data_tool = Tool(
    name="retrieve_dataframe_metadata",
    func=retrieve_dataframe_meta.run,  
    description=(
        """
        Retrieves metadata about the loaded DataFrame.

        Returns a JSON-serializable dictionary containing:
        - Number of rows and columns
        - List of column names
        - Data types for each column
        - Count of missing values per column

        Useful for quickly understanding the structure and quality of the dataset.
        """
    )
)

tools = [execute_tool, meta_data_tool]

prompt = PromptTemplate(
    input_variables=["input"],  
    template="""
You are a data analyst assistant with access to two tools:

1. `meta_data_tool` — Retrieves metadata about the dataset loaded as a pandas DataFrame named `df`.
2. `execute_tool` — Executes Python code on `df` and returns structured JSON results.

Your process:
- First, call the `meta_data_tool` to gather essential metadata about the DataFrame (e.g., columns, types, number of rows).
- Use the metadata and the user question below to generate Python code that answers the question by operating on `df`.
- Assign the final answer to a variable named `result`. This must be JSON-serializable (e.g., dict or list).
- Send this Python code to the `execute_tool` for execution.
- Finally, parse the output from `execute_tool` and provide the user with a clear, concise, human-readable answer to the question from the results.

User question:
{input}

Remember:
- Only output Python code when generating code for `execute_tool`.
- Use the metadata intelligently to write accurate code.
- Your final response to the user should be a plain-text answer based on the execution result.
"""
)

DataAnalystAgent = initialize_agent(
    tools,
    ChatLLM,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    prompt=prompt,
    handle_parsing_errors=True
)


if __name__ == "__main__":
    user_q = "What are the most frequently travelled flights?"
    output = DataAnalystAgent.run(user_q)
    print(output)
