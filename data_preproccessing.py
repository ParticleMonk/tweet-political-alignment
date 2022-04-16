import numpy as np
import pandas as pd
import csv


dataset = pd.read_csv('congressional_tweet_training_data.csv')

print(dataset)

del dataset["full_text"]

print(dataset)

columnSeriesObj = dataset["hashtags"]

hashtag_list = []

#columnSeriesObj is the list of values delimited by whitespace
for tweet in columnSeriesObj:
    temp_list = []
    temp_list.append(tweet.split)
    for item in temp_list:
        #if item is in list increment its count
        if item in hashtag_list:
            hashtag_list[hashtag_list.index(item)][1] += 1

            #add to hashtag list if not there
        if item not in hashtag_list:
            hashtag_list.append([item, 1])

print(hashtag_list[1])


