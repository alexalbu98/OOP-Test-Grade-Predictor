import csv


def write_to_csv(file, project, nr_of_lines, classes, inheritance, polymorphism, grade):
    """Writes a line in the csv file containing the dataset"""
    file = open(file, "a")
    writer = csv.writer(file, delimiter="\t")
    writer.writerow([project, nr_of_lines, classes, inheritance, polymorphism, grade])
    file.close()
