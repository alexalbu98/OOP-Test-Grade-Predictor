import re


def get_inheritance_number(file):
    regex = re.compile("class.*([^\\s]+).*:\\s*(virtual)?.*(public|private).*([^\\s]+)")
    file = open(file, mode="r")
    content = file.read()
    nr_of_inheritances = len(regex.findall(content))
    file.close()
    return nr_of_inheritances


def get_class_number(file):
    regex = re.compile("class")
    file = open(file, mode="r")
    content = file.read()
    nr_of_classes = len(regex.findall(content))
    file.close()
    return nr_of_classes


def get_polymorphism_number(file):
    regex = re.compile("virtual.*([^\\s]+).*([^\\s]+)\\(.*\\)|override|template|operator")
    file = open(file, mode="r")
    content = file.read()
    nr_of_poly = len(regex.findall(content))
    file.close()
    return nr_of_poly


def get_namespace_number(file):
    regex = re.compile("namespace")
    file = open(file, mode="r")
    content = file.read()
    nr_of_namespaces = len(regex.findall(content))
    file.close()
    return nr_of_namespaces


def get_interfaces_number(file):
    regex = re.compile("virtual.*=.*0;")
    file = open(file, mode="r")
    content = file.read()
    nr_of_interfaces = len(regex.findall(content))
    file.close()
    return nr_of_interfaces


def get_code_lines_number(file):
    file = open(file, mode="r")
    empty_line_regex = re.compile(r'^\s*$')
    lines = file.readlines()
    count = 0
    for line in lines:
        if len(empty_line_regex.findall(line)) == 0:  # line is not empty
            count += 1
    return count
