import pickle


def pickle_object(Object, file):
    filehandler = open(file, 'wb')
    pickle.dump(Object, filehandler)
    filehandler.close()


def unpickle_object(file):
    filehandler = open(file, 'rb')
    Object = pickle.load(filehandler)
    filehandler.close()
    return Object
