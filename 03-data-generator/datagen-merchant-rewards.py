import pandas as pd
import random

merchant_ids = [i for i in range(1,100+1)]
reward_points = [random.randint(1,15)  for m in merchant_ids ]

# print (merchant_ids)
# print (reward_points)

df = pd.DataFrame({'merchant_id' : merchant_ids,   'reward_points' : reward_points})
print (df.to_markdown())
      
df.to_csv('reward-points.csv', index=False)
print (f'wrote to "reward-points.csv"')
