import numpy as np
import pandas as pd
import csv
import math


dataset = pd.read_csv('congressional_tweet_training_data_v5.csv')


'''cond = dataset['party_id'] == "R"

dataset.loc[cond,'party_id'] = 1
cond = dataset['party_id'] == "D"
dataset.loc[cond,'party_id'] = 0
dataset.to_csv('congressional_tweet_training_data_v3.csv')
'''
hashtag_shortlist = pd.read_csv('column_list.csv')
#print(dataset)

hashtags = hashtag_shortlist['hashtag']


for column in dataset:
    if column not in hashtags.values:
        del dataset[column]

dataset.to_csv('congressional_tweet_training_data_v6.csv', index=False)

'''
for hashtag in hashtags.values:
    dataset[hashtag] = [0] * 592803
    dataset = dataset.copy()
del dataset["full_text"]

dataset.to_csv('congressional_tweet_training_data_v2.csv', index=False)
'''
'''
#print(dataset)

columnSeriesObj = dataset["year"]
#print(dataset['hashtags'].value_counts())
#hashtag_list = []
row_count = 0
copy_count = 0
#columnSeriesObj is the list of values delimited by whitespace

for tweet in columnSeriesObj.values:
    if math.isnan(tweet):
        dataset.at[row_count, 'year'] = 0
        copy_count += 1
    if copy_count > 4000:
        dataset = dataset.copy()
        copy_count = 0
    #print(copy_count)
    row_count += 1

dataset.to_csv('congressional_tweet_training_data_v5.csv', index=False)
'''
'''
for tweet in columnSeriesObj.values:
    temp_list = []
    #print(tweet)
    temp_list.append(tweet.split())
   #print(temp_list)
    for item in temp_list:
        #if item is in list increment its count
        temp_item = ''
        temp_item = item[0].lower()
        if any(temp_item in sublist for sublist in hashtags.values):
            dataset.at[row_count, temp_item] = 1
            copy_count += 1
    if copy_count > 4000:
        dataset = dataset.copy()
        copy_count = 0
    #print(copy_count)
    row_count += 1


del dataset['hashtags']
dataset.to_csv('congressional_tweet_training_data_v4.csv', index=False)
'''
'''
print(len(hashtag_list))

hashtag_list.sort(key = lambda x: x[1], reverse = True)

hashtag_df = pd.DataFrame(hashtag_list[:500], columns=['hashtag', 'count])'])

hashtag_df.to_csv('hashtag_shortlist', index=False)
'''



