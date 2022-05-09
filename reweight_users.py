import pandas as pd
import csv
import ipdb

df = pd.read_csv('user.csv')

def weight(row):
    review = row['review_count']
    elite = row['elite']
    fans = row['fans']
    compliments = row['compliments']

    total = 0
    if float(review) >= 0.75:
        total += .5
    elif float(review) >= 0.5:
        total += .25
    elif float(review) >= 0.25:
        total += .125
    else:
        total += 0.0625

    if str(elite) == 'Yes':
        total += .5
    
    if float(fans) >= 0.75:
        total += .2
    elif float(fans) >= 0.5:
        total += .1
    elif float(fans) >= 0.25:
        total += .05
    else:
        total += 0.025

    if float(compliments) >= 0.75:
        total += .1
    elif float(compliments) >= 0.5:
        total += .05
    elif float(compliments) >= 0.25:
        total += 0.025
    else:
        total += 0.0125
    
    if total > 1:
        total = 1

    return total



df['review_count']=df.review_count.rank(pct=True)
df['fans']=df.fans.rank(pct=True)
df['compliments']=df.compliments.rank(pct=True)
df['user_weight'] = df.apply(weight, axis=1)
drop_df = df.drop(['Unnamed: 0', 'yelping_since'], axis=1)

drop_df.to_csv('reweight_2.csv')
#print(drop_df)



