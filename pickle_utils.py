import pickle


def pickle_object(Object, file):
    """Save an object to a file.\n
    :arg Object: the object to be saved
    :arg file: the file where to save
    """
    filehandler = open(file, 'wb')
    pickle.dump(Object, filehandler)
    filehandler.close()


def unpickle_object(file):
    """Loads an object from a file.\n
    :arg file: the file where the object was saved
    :return: The object loaded from the file
    """
    filehandler = open(file, 'rb')
    Object = pickle.load(filehandler)
    filehandler.close()
    return Object
