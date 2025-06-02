import pandas as pd
from Cleaner.helper import static_process_dataframe, llm_process_rows
from langchain_core.prompts import ChatPromptTemplate
import os


def clean_dataset(df, llm_call):
    if llm_call == "static":
        cleaned_df = static_process_dataframe(df)
    else:
        prompt = ChatPromptTemplate.from_template("""
        You are a data cleaning assistant.

        Given the following dataset schema and sample rows, generate Python pandas code to:
        1. Clean the dataset using common best practices
        2. Rename columns to more meaningful names if needed
        3. Fix missing values, spelling issues, or inconsistent values
        4. Dont write any comments
        5. Add airline name column using the following airlineID mapping:
            airlie_id,airline_name
            1,American Airline
            2,Delta Air Lines
            3,United Airlines
            4,Southwest Airlines
            5,JetBlue Airways
            6,Alaska Airlines
            7,Spirit Airlines
            8,Frontier Airlines
            9,Hawaiian Airlines
            10,Allegiant Air
            11,SkyWest Airlines
            12,Air Canada
            13,British Airways
            14,Lufthansa
            15,Air France
            16,KLM Royal Dutch Airlines
            17,Qantas
            18,Emirates
            19,Singapore Airlines
            20,Cathay Pacific
                                                
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
        cleaned_df = llm_process_rows(prompt, df)
    
    cleaned_df.to_csv(os.path.join(os.getcwd(),"uploads\\uploaded_data.csv"))
    return cleaned_df
