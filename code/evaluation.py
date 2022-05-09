import pandas as pd
from scipy.stats import ttest_ind

ratings = pd.read_csv('new_ratings.csv')
business = pd.read_csv('business.csv')
length = len(ratings.index)

ratings['average_stars'] = ratings['average_stars'].round(1)
ratings = pd.merge(left=ratings, right=business, on='name')
ratings = ratings.sort_values(by=['average_stars', 'review_count', 'name'], ascending=False)\
    .reset_index()
ratings = ratings[['name', 'average_stars', 'stars', 'city', 'review_count']]

#sample = ratings.sample(n=5)

print(ttest_ind(ratings['average_stars'], ratings['stars'], equal_var=False))

ratings.to_csv('top_ratings_list.csv')
#sample.to_csv('top_ratings_sample.csv')