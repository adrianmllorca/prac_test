import pandas as pd

df = pd.read_csv('Exam_Table.csv').dropna()

unique_sci_names = df['Scientific Name'].unique()

mean_est_size = df.groupby('Scientific Name')['Size Est (cm)'].mean()

output_df = pd.DataFrame({"Scientific Names" : unique_sci_names,
                          "Mean Est Size" : mean_est_size}
                          )
                          
output_df.to_csv('b4test.csv', index=False)