import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from pickle_utils import pickle_object
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def get_data(data_file):
    """Extracts the labels and data from a csv file.\n
    :arg data_file: The csv file containing the dataset.
    :return: tuple containing the features and labels
    """
    df = pd.read_csv(data_file, delimiter="\t")
    features = df[["lines_of_code", "classes", "inheritance", "polymorphism"]]
    labels = df["grade"].tolist()
    features = np.asarray(features).astype("float32")
    labels = np.asarray(labels).astype("float32").reshape(len(labels), 1)
    return features, labels


def plot_data(file):
    df = pd.read_csv(file, delimiter="\t")
    X = df[["lines_of_code", "classes", "inheritance", "polymorphism"]]
    Y = df["grade"]

    pca = PCA(n_components=1)
    components = pca.fit_transform(X)

    plt.scatter(components, Y)
    plt.xlabel("Features")
    plt.ylabel("Grades")
    plt.show()


plot_data("data.csv")
features, labels = get_data("data.csv")

x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.1, shuffle=True)

k = 4  # split into 4 parts
num_val_samples = len(x_train) // k
all_rmse_scores = []
all_mae_scores = []

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

    lr = LinearRegression(normalize=True)
    lr.fit(partial_train_data, partial_train_targets)
    y_pred = lr.predict(x_val)
    rmse = mean_squared_error(y_val, y_pred, squared=False)
    mae = mean_absolute_error(y_val, y_pred)
    all_rmse_scores.append(rmse)
    all_mae_scores.append(mae)

rmse_mean = np.mean(all_rmse_scores)
mae_mean = np.mean(all_mae_scores)
print(f"The MAE score is {mae_mean} and the RMSE score is {rmse_mean} on the validation data.")

# test on the test set
model = LinearRegression(normalize=True)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
print(f"The test MAE is {mae} and test RMSE is {rmse}.")

# save the model
save = str(input("Do you want to save?"))
if save == "yes":
    print("Saving...")
    pickle_object(model, "model.obj")
