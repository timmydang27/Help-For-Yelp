import pandas as pd

review = pd.read_json('./yelp_academic_dataset_review.json', lines=True)
review = review[['review_id', 'user_id', 'business_id', 'stars', 'useful']]
business = pd.read_csv('./business.csv')
business = business[['business_id', 'state']]

review = pd.merge(left=review, right=business, on='business_id')
review = review[(review['state']=='CA')]\
    .reset_index()
review = review[['review_id', 'user_id', 'business_id', 'stars', 'useful']]
review.to_csv('review.csv')