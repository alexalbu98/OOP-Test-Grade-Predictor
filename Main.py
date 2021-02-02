from file_analyzer import *
from csv_utilities import write_to_csv
import os
import re


def extract_project_data(project_folder, csv_file):
    file_regex = re.compile(".*(\\.cpp|\\.h)")
    nr_of_lines = 0
    classes = 0
    namespaces = 0
    inheritance = 0
    interfaces = 0
    poly = 0
    for root, subdirs, files in os.walk(project_folder):
        for file in files:
            if len(file_regex.findall(file)) != 0:  # file is a .cpp or .h file
                path = os.path.join(root, file)
                nr_of_lines += get_code_lines_number(path)
                classes += get_class_number(path)
                namespaces += get_namespace_number(path)
                inheritance += get_inheritance_number(path)
                interfaces += get_interfaces_number(path)
                poly += get_polymorphism_number(path)

    write_to_csv(csv_file, project_folder, nr_of_lines, classes, namespaces, interfaces, inheritance, poly)


def main():
    extract_project_data("tema2/student_4", "data.csv")


if __name__ == '__main__':
    main()
