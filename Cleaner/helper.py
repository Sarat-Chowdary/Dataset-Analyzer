import pandas as pd
import numpy as np
from llm.chat_agent import ChatLLM
from langchain_core.output_parsers import JsonOutputParser

def static_process_dataframe(df: pd.DataFrame) -> pd.DataFrame:

    df = df.drop_duplicates()

    df.columns = df.columns.str.lower().str.replace(" ", "_")
    str_cols = df.select_dtypes(include='object').columns
    df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

    df.replace(['N/A', 'na', 'n.a.', '', 'none', 'null', 'NULL'], np.nan, inplace=True)

    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna(df[col].mode(dropna=True)[0])  
        else:
            df[col] = df[col].fillna(df[col].median())
    
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    df = df.convert_dtypes()
    return df

def llm_process_rows(prompt: str, df: pd.DataFrame) -> pd.DataFrame:
    schema = df.dtypes.apply(str).to_dict()
    sample = df.head(5).to_dict(orient="records")
    
    parser = JsonOutputParser()
    chain = prompt | ChatLLM | parser
    response = chain.invoke({
        "schema": schema,
        "sample": sample
    })

    code = response["code"]
    print("Suggested cleaning code:\n")
    print(code)

    scope = {"df": df.copy(), "pd": pd}
    exec(code, scope)

    cleaned_df = scope.get("df")
    return cleaned_df