import numpy as np


class DataFile(object):

    data = list()

    def __init__(self):

        return

    def add_item(self, item):
        self.data.append(item)
        return len(self.data)

    def save(self, path):
        array = np.asarray(self.data)
        np.save(path, array)
        return array

    @staticmethod
    def load_data(path):
        return np.load(path)
