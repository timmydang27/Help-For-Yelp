#from distutils.command.build_ext import build_ext
import pandas as pd

business = pd.read_json('./yelp_academic_dataset_business.json', lines=True)
business = business[['business_id', 'name', 'city', 'state', 'stars', 'review_count', 'categories', 'is_open']]

business = business[(business['is_open']==1)]\
    .reset_index()
business = business[['business_id', 'name', 'city', 'state', 'stars', 'review_count', 'categories']]

business.to_csv('business.csv')