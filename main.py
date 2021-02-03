from pickle_utils import unpickle_object
from create_dataset import extract_project_data
import numpy as np
import os


def analyze_project(project_folder):
    """Extracts the features of a project"""
    data = extract_project_data(project_folder)
    data = np.asarray(data[1:]).astype("float32")
    return data.reshape(1, -1)


def grade_projects(projects_folder, model):
    """Grades all the projects from a projects directory using a machine learning model"""
    grades = {}
    for root, subdirs, files in os.walk(projects_folder):
        for project in subdirs:
            try:
                path = os.path.join(root, project)
                data = analyze_project(path)
                grade = model.predict(data)
                grades[project] = float(grade[0])
            except:
                print(f"Failed to grade project {project}")
        break
    return grades


def print_grades(grades):
    place = 1
    for key in grades:
        print(f"Project {key} is on place {place} with grade {grades[key]}.")
        place += 1


if __name__ == '__main__':
    model = unpickle_object("model.obj")
    grades = grade_projects("test", model)
    # sort the grades in revers
    sorted_grades = {key: val for key, val in sorted(grades.items(), key=lambda ele: ele[1], reverse=True)}
    print_grades(sorted_grades)
