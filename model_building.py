import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras import models, layers
from keras.metrics import RootMeanSquaredError
import matplotlib.pyplot as plt


def build_model(input_shape):
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu',
                           input_shape=(input_shape,)))
    model.add(layers.Dense(54, activation='relu'))
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


def smooth_curve(points, factor=0.9):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:
            smoothed_points.append(point)
    return smoothed_points


features, labels = get_data("data.csv")

# split dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.1, shuffle=True)

# normalize features so that feature ranges are smaller

mean = x_train.mean(axis=0)
std = x_train.std(axis=0)

x_train -= mean
x_train /= std

x_test -= mean
x_test /= std

k = 4  # split into 4 parts
num_val_samples = len(x_train) // k
num_epochs = 500
all_scores = []  # all rmse scores
all_rmse_histories = []
shape = x_train.shape[-1]

# k_fold validation
for i in range(k):
    print("Processing fold #", i)
    x_val = x_train[i * num_val_samples:(i + 1) * num_val_samples]
    y_val = y_train[i * num_val_samples:(i + 1) * num_val_samples]

    partial_train_data = np.concatenate(
        [x_train[:i * num_val_samples],
         x_train[(i + 1) * num_val_samples:]],
        axis=0)

    partial_train_targets = np.concatenate(
        [y_train[:i * num_val_samples],
         y_train[(i + 1) * num_val_samples:]],
        axis=0)

    model = build_model(shape)
    history = model.fit(partial_train_data, partial_train_targets,
                        validation_data=(x_val, y_val),
                        epochs=num_epochs, batch_size=1, verbose=0)
    rmse_history = history.history['val_root_mean_squared_error']
    all_rmse_histories.append(rmse_history)

average_rmse_history = [
    np.mean([x[i] for x in all_rmse_histories]) for i in range(num_epochs)]

smooth_rmse_history = smooth_curve(average_rmse_history[10:])
plt.plot(range(1, len(smooth_rmse_history) + 1), smooth_rmse_history)
plt.xlabel('Epochs')
plt.ylabel('Validation RMSE')
plt.show()
