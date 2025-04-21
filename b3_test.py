import pandas as pd

df = pd.read_csv('Exam_Table.csv').dropna()

unique_sci_names = df['Scientific Name'].unique()

output_df = pd.DataFrame({"Scientific Names" : unique_sci_names})

output_df.to_csv('b3test.csv', index=False)