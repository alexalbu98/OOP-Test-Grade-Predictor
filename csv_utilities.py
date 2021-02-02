import csv


def write_to_csv(file, project, nr_of_lines, classes, interfaces, inheritance, polymorphism, grade):
    file = open(file, "a")
    writer = csv.writer(file, delimiter="\t")
    writer.writerow([project, nr_of_lines, classes, interfaces, inheritance, polymorphism, grade])
    file.close()
