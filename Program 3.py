import pandas as pd
import numpy as np

np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
from tensorflow.keras import layers

congressional_tweet_train = pd.read_csv('congressional_tweet_training_data_v6.csv')

congressional_tweet_train.head()

congressional_tweet_features = congressional_tweet_train.copy()
congressional_tweet_labels = congressional_tweet_features.pop('party_id')


congressional_tweet_features = np.array(congressional_tweet_features)

normalize = layers.Normalization()

normalize.adapt(congressional_tweet_features)

congressional_tweet_model = tf.keras.Sequential([
    normalize,
    layers.Dense(64),
    layers.Dense(1)
])

congressional_tweet_model.compile(loss = tf.keras.losses.MeanSquaredError(),
                                  optimizer = tf.optimizers.Adam())

congressional_tweet_model.fit(congressional_tweet_features, congressional_tweet_labels, epochs=10)