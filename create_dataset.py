from file_analyzer import *
from csv_utilities import write_to_csv
import os
import re


def extract_project_data(project_folder):
    """Extracts the features of a project from a project directory.\n
    :arg project_folder: The project directory.
    :return: List containing features
    """
    file_regex = re.compile(".*(\\.cpp|\\.h)$")
    nr_of_lines = 0
    classes = 0
    inheritance = 0
    poly = 0
    for root, subdirs, files in os.walk(project_folder):
        for file in files:
            if len(file_regex.findall(file)) != 0:  # file is a .cpp or .h file
                path = os.path.join(root, file)
                nr_of_lines += get_code_lines_number(path)
                classes += get_class_number(path)
                inheritance += get_inheritance_number(path)
                poly += get_polymorphism_number(path)

    return [project_folder, nr_of_lines, classes, inheritance, poly]


def get_grades(grades_file):
    """Extracts the grades for each project.\n
    :arg grades_file: File containing the grades
    :return: A dictionary containing the project name and grade
    """
    grades = {}
    file = open(grades_file, mode="r")
    lines = file.readlines()
    for line in lines:
        tokens = line.split('\t')
        grade = tokens[-1].split("\n")[-2]
        if grade == "NaN":
            grade = 0
        else:
            grade = float(grade)
        student = tokens[0]
        grades[student] = grade

    return grades


def create_dataset(projects_folder, grade_list, csv_file):
    """Creates a dataset from a directory containing all the projects."""
    grades = get_grades(grade_list)
    for root, subdirs, files in os.walk(projects_folder):
        for subdir in subdirs:
            try:
                grade = grades[subdir]
                if grade == 0:  # all projects must be annotated
                    continue
                project_folder = os.path.join(root, subdir)
                data = extract_project_data(project_folder)
                data.append(grade)
                write_to_csv(csv_file, subdir, data[1], data[2], data[3], data[4], data[5])
            except:
                print(f"Error analyzing {subdir}")
        break


if __name__ == '__main__':
    create_dataset("train", "labels.txt", "data.csv")
