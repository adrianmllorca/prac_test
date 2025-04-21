import pandas as pd

df = pd.read_csv('Exam_Table.csv').dropna()

output_df = df[df["Genus"].str.startswith("St")]

output_df.to_csv('b2test.csv', index=False)