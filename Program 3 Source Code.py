import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow.keras import layers

congressional_tweet_train = pd.read_csv('congressional_tweet_training_data_v7.csv')
congressional_tweet_test = pd.read_csv('congressional_tweet_testing_data_v1.csv')
congressional_tweet_train.head()

congressional_tweet_features = congressional_tweet_train.copy()
congressional_tweet_labels = congressional_tweet_features.pop('party_id')

congressional_tweet_test_features = congressional_tweet_test.copy()
congressional_tweet_test_labels = congressional_tweet_test_features.pop('party_id')


normalize = layers.Normalization()

normalize.adapt(congressional_tweet_features)

features_val = congressional_tweet_features[-10000:]
labels_val = congressional_tweet_labels[-10000:]

congressional_tweet_features[:-10000]
congressional_tweet_labels[:-10000]
congressional_tweet_model = tf.keras.Sequential([
    normalize,
    layers.Dense(64, input_shape=(504,)),
    layers.Dense(64),
    layers.Dense(32, activation='sigmoid'),
    layers.Dense(2),
    layers.Dense(1)
])

congressional_tweet_model.compile(loss = tf.keras.losses.MeanSquaredError(),
                                  optimizer = tf.optimizers.SGD(),
                                  metrics=['acc'])

congressional_tweet_model.fit(congressional_tweet_features, congressional_tweet_labels, epochs=10)

results = congressional_tweet_model.evaluate(congressional_tweet_test_features, congressional_tweet_test_labels, batch_size=128)

print('test loss, test acc: ', results)

results = congressional_tweet_model.evaluate(features_val, labels_val, batch_size=128)
print('\nvalidation loss, validation acc:', results)