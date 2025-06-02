from Cleaner.helper import static_process_dataframe, llm_process_rows
import pandas as pd
import os

df = pd.read_csv(os.path.join(os.getcwd(),"uploads\\uploaded_data.csv"))
# print(static_process_dataframe(df))
print(llm_process_rows(df.head(10)))
