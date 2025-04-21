import pandas as pd

df = pd.read_csv('Exam_table.csv').dropna()

output_df = df[df.Interval == '30-0']

output_df.to_csv('b1test.csv', index=False)