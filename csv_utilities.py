import csv
import pandas as pd


def write_to_csv(file, id, project, classes, interfaces, inheritance, polymorphism, diagram):
    file = open(file, "a")
    writer = csv.writer(file, delimiter="\t")
    writer.writerow([id, project, classes, interfaces, inheritance, polymorphism, diagram])
    file.close()


def read_from_csv(file):
    df = pd.read_csv(file, delimiter="\t")
    return df
