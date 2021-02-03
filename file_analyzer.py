import re


def get_inheritance_number(file):
    """Finds all the uses of inheritance from a file.\n
    :arg file: The file to be analyzed.
    :return: Count of inheritance usage
    """
    regex = re.compile("class.*([^\\s]+).*:\\s*(virtual)?.*(public|private).*([^\\s]+)")
    file = open(file, mode="r", encoding="utf-8")
    content = file.read()
    nr_of_inheritances = len(regex.findall(content))
    file.close()
    return nr_of_inheritances


def get_class_number(file):
    """Finds all the classes from a file.\n
     :arg file: The file to be analyzed.
     :return: Count of classes
     """
    regex = re.compile("class")
    file = open(file, mode="r", encoding="utf-8")
    content = file.read()
    nr_of_classes = len(regex.findall(content))
    file.close()
    return nr_of_classes


def get_polymorphism_number(file):
    """Finds all the uses of polymorphism methods(operator overload, template, method override, virtual functions)
     from a file.\n
     :arg file: The file to be analyzed.
     :return: Count of polymorphism methods used
     """
    regex = re.compile("virtual.*([^\\s]+).*([^\\s]+)\\(.*\\)|override|template|operator")
    file = open(file, mode="r", encoding="utf-8")
    content = file.read()
    nr_of_poly = len(regex.findall(content))
    file.close()
    return nr_of_poly


def get_interfaces_number(file):
    """Finds all the interfaces specific methods from a file. Interface specific methods will have an =0 when declared\n
     :arg file: The file to be analyzed.
     :return: Count of interface methods
     """
    regex = re.compile("virtual.*=.*0;")
    file = open(file, mode="r", encoding="utf-8")
    content = file.read()
    nr_of_interfaces = len(regex.findall(content))
    file.close()
    return nr_of_interfaces


def get_code_lines_number(file):
    """Finds the number of code lines from a file.\n
     :arg file: The file to be analyzed.
     :return: The number of lines
     """
    file = open(file, mode="r", encoding="utf-8")
    empty_line_regex = re.compile(r'^\s*$')
    lines = file.readlines()
    count = 0
    for line in lines:
        if len(empty_line_regex.findall(line)) == 0:  # line is not empty
            count += 1
    file.close()
    return count
