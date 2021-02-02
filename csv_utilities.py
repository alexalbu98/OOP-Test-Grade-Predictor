import csv
import pandas as pd


def write_to_csv(file, project, nr_of_lines, classes, namespaces, interfaces, inheritance, polymorphism, grade):
    file = open(file, "a")
    writer = csv.writer(file, delimiter="\t")
    writer.writerow([project, nr_of_lines, classes, namespaces, interfaces, inheritance, polymorphism, grade])
    file.close()


def read_from_csv(file):
    df = pd.read_csv(file, delimiter="\t")
    return df
