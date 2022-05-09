import pandas as pd
import csv
import ipdb

df = pd.read_csv('review.csv')

def weight(row):
    useful = row['useful']

    total = 0
    if float(useful) >= 0.75:
        total = 1
    elif float(useful) >= 0.50:
        total = .90
    elif float(useful) >= 0.25:
        total = .80
    else:
        total = .70
        


    return total



df['useful']=df.useful.rank(pct=True)
# df['fans']=df.fans.rank(pct=True)
# df['compliments']=df.compliments.rank(pct=True)
df['review_weight'] = df.apply(weight, axis=1)
drop_df = df.drop(['Unnamed: 0'], axis=1)

drop_df.to_csv('review_weight.csv')
#print(drop_df)