# generates small amount of sample data

import pandas as pd
from datagen_helper import generate_pd_df

rows = 20
df_pd = generate_pd_df(rows)


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# print (df_pd.to_markdown()) # needs 'tabulate' package
print (df_pd)

df_pd.to_csv('transactions-small.csv', sep='|', index=False)
print (f'wrote {rows} rows to "transactions-small.csv"')