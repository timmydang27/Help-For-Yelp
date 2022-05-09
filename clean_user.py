import pandas as pd
import csv
import ipdb


df = pd.read_json('../data/yelp_academic_dataset_user.json', lines=True)
filtered_df = df.drop(['name', 'useful', 'cool', 'funny', 'friends'], axis = 1)
filtered_df['compliments'] = filtered_df['compliment_hot'] + filtered_df['compliment_more'] + filtered_df['compliment_profile'] + filtered_df['compliment_cute'] + filtered_df['compliment_list'] + filtered_df['compliment_note'] + filtered_df['compliment_plain'] + filtered_df['compliment_funny'] + filtered_df['compliment_cool'] + filtered_df['compliment_writer'] + filtered_df['compliment_photos']
filtered_df.drop(filtered_df.iloc[:, 6:17], inplace = True, axis = 1)
filtered_df['elite'] = filtered_df['elite'].apply(lambda x: "Yes" if len(x) else "No")
filtered_df.to_csv('user.csv')