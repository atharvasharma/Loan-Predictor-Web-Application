from __future__ import absolute_import, division, print_function

import pathlib
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)

datasets=pd.read_csv("cs-training.csv",index_col=0)
datasets=datasets.dropna()

datasets2=pd.read_csv("cs-test.csv",index_col=0)
datasets2=datasets2.dropna()
#print(datasets.isna().sum())
train_labels=datasets["SeriousDlqin2yrs"]
train_data=datasets.drop(['SeriousDlqin2yrs'],axis=1)

test_labels=datasets["SeriousDlqin2yrs"]
test_data=datasets.drop(['SeriousDlqin2yrs'],axis=1)
#print(train_labels)
train_stats = train_data.describe()
train_stats = train_stats.transpose()
print(train_stats)

def norm(x):
  	return (x - train_stats['mean']) / train_stats['std']
normed_train_data = norm(train_data)
normed_test_data = norm(test_data)

def build_model():
  model = keras.Sequential([
    layers.Dense(64, activation=tf.nn.relu, input_shape=[len(train_data.keys())]),
    layers.Dense(64, activation=tf.nn.relu),
    layers.Dense(1)
  ])

  optimizer = tf.train.RMSPropOptimizer(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['accuracy'])
  return model

model=build_model()

model.summary()

#example_batch = normed_train_data[:10]
#example_result = model.predict(example_batch)
#print(example_result)  
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create checkpoint callback
cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, 
                                                 save_weights_only=True,
                                                 verbose=1)

# Display training progress by printing a single dot for each completed epoch
model = build_model()

model.fit(train_data, train_labels,  epochs = 10, 
          validation_data = (test_data,test_labels),
          callbacks = [cp_callback])  # pass callback to training

model = build_model()

print(model.metrics_names)
loss, acc = model.evaluate(test_data, test_labels)
print("Untrained model, accuracy: {:5.2f}%".format(100*acc))

model.load_weights(checkpoint_path)
loss, acc = model.evaluate(test_data, test_labels)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))

checkpoint_path = "training_2/cp-{epoch:04d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(
    checkpoint_path, verbose=1, save_weights_only=True,
    # Save weights, every 5-epochs.
    period=5)

model = build_model()
model.fit(train_data, train_labels,
          epochs = 50,validation_data = (test_data,test_labels),
          callbacks = [cp_callback],
          verbose=0)

latest = tf.train.latest_checkpoint(checkpoint_dir)
print(latest)

model = build_model()
model.load_weights(latest)
loss, acc = model.evaluate(test_data, test_labels)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))

# Save the weights
model.save_weights('./checkpoints/my_checkpoint')

# Restore the weights
model = build_model()
model.load_weights('./checkpoints/my_checkpoint')

loss,acc = model.evaluate(test_data, test_labels)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))

model=build_model()
optimizer = tf.train.RMSPropOptimizer(0.001)

model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['accuracy'])
model.fit(train_data, train_labels, epochs=5)

# Save entire model to a HDF5 file
model.save('my_model.h5')

new_model = keras.models.load_model('my_model.h5')
new_model.summary()

loss, acc = new_model.evaluate(test_data, test_labels)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))

#model = build_model()

#model.fit(train_data, train_labels, epochs=5)
#saved_model_path = tf.contrib.saved_model.save_keras_model(model, "./saved_models")
#new_model = tf.contrib.saved_model.load_keras_model(saved_model_path)

#optimizer = tf.train.RMSPropOptimizer(0.001)

#new_model.compile(loss='mse', optimizer=optimizer, metrics=['accuracy'])

#loss, acc = new_model.evaluate(test_data, test_labels)
#print("Restored model, accuracy: {:5.2f}%".format(100*acc))