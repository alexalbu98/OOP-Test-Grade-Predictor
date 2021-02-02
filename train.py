import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras import models, layers
from keras.metrics import RootMeanSquaredError


def build_model(input_shape):
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu',
                           input_shape=(input_shape,)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='adam', loss='mse', metrics=[RootMeanSquaredError()])

    return model


def get_data(data_file):
    features = []
    df = pd.read_csv(data_file, delimiter="\t")
    lines_of_code = df["lines_of_code"].tolist()
    classes = df["classes"].tolist()
    interfaces = df["interfaces"].tolist()
    inheritance = df["inheritance"].tolist()
    polymorphism = df["polymorphism"].tolist()
    labels = df["grade"].tolist()
    for i in range(len(df["project"].tolist())):
        feature = [lines_of_code[i], classes[i], interfaces[i], inheritance[i], polymorphism[i]]
        features.append(feature)
    features = np.asarray(features).astype("float32")
    labels = np.asarray(labels).astype("float32").reshape(len(labels), 1)
    return features, labels


features, labels = get_data("data.csv")

# split dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, shuffle=True)

# normalize features so that feature ranges are smaller

mean = x_train.mean(axis=0)
std = x_train.std(axis=0)

x_train -= mean
x_train /= std

x_test -= mean
x_test /= std

shape = x_train.shape[-1]

model = build_model(shape)
model.fit(x_train, y_train,
          epochs=50, batch_size=1)

test_mse_score, test_rmse_score = model.evaluate(x_test, y_test)

print(test_rmse_score)
