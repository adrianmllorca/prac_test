import pandas as pd

df = pd.read_csv('Exam_Table.csv').dropna()

ave_count = df.loc[df['Scientific Name'] == "Pomacentrus adelus", ['Count']].mean()

output_df = pd.DataFrame({"Scientific Names" : "Pomacentrus adelus",
                          "Average Count" : ave_count}
)

output_df.to_csv('b5test.csv', index=False)