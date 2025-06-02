import pandas as pd
from Cleaner.helper import static_process_dataframe, llm_process_rows
from langchain_core.prompts import ChatPromptTemplate



def clean_dataset(df, llm_call):
    if llm_call == "static":
        return static_process_dataframe(df)
    else:
        prompt = ChatPromptTemplate.from_template("""
        You are a data cleaning assistant.

        Given the following dataset schema and sample rows, generate Python pandas code to:
        1. Clean the dataset using common best practices
        2. Rename columns to more meaningful names if needed
        3. Fix missing values, spelling issues, or inconsistent values
        4. Dont write any comments
                                                
        Assume the dataset is in a pandas DataFrame named df. Provide code that operates directly on df without referring to other variables like sample_data
                                                
        Respond with only the cleaned Python code as a JSON object with a single key "code".
        The value should be a string containing the full code, with newlines and quotes properly escaped.                                      
                                                
        Respond with only the cleaned Python code, wrapped as a string in JSON like this:
        {{"code": "<your_code_here>"}}

        Schema:
        {schema}

        Sample:
        {sample}
        """)
        return llm_process_rows(prompt, df)
