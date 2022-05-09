import pandas as pd
import csv
import ipdb


def weight(row):
    star = row['stars']
    user = row['user_weight']
    review = row['review_weight']

    val = star * user * review
    

    return val

def calculate(row):
    user = row['user_weight']
    review = row['review_weight']

    val =  user * review
    
    return val

def average(row):
    num = row['new_weight']
    denom = row['denom']

    val =  num / denom
    
    return val


df_users = pd.read_csv('reweight_users.csv')
df_reviews = pd.read_csv('review_weight.csv')
df_business = pd.read_csv('business.csv')

df_ur = pd.merge(df_users, df_reviews, on="user_id")
filtered_df_ur =  df_ur.drop(['Unnamed: 0_x', 'review_count', 'elite', 'fans', 'useful', 'compliments', 'Unnamed: 0_y'], axis = 1)
filtered_df_ur['new_weight'] = filtered_df_ur.apply(weight, axis=1)
df_urb = pd.merge(filtered_df_ur, df_business, on="business_id")
filtered_df_urb =  df_urb.drop(['categories', 'city', 'state', 'Unnamed: 0', 'stars_x'], axis = 1)
new_df = filtered_df_urb.rename(columns={"average_stars": "user_average_stars", "stars_y": "business_average_stars"})
new_df['denom'] = new_df.apply(calculate, axis=1)
denom_df =new_df.groupby('name')['denom'].sum()
num_df =new_df.groupby('name')['new_weight'].sum()
merge_df = pd.merge(denom_df, num_df, on="name")
merge_df['average_stars'] = merge_df.apply(average, axis=1)
merge_df.to_csv('new_ratings.csv')
# print(new_df[['denom', 'new_weight']])
# print(new_df[['s_denom', 's_num']])
# new_df = new_df.groupby('name').mean()
# print(new_df.groupby('name')['denom'].sum())
#new_df.apply(average, axis=1)
#print(new_df[['name', 'new_average']])