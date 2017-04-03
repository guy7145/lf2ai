import numpy as np


class capture_dataset(object):

    def __init__(self):
        self.screenshots = []

    def add_screenshot(self, np_arr):
        self.screenshots.append(np_arr)

    def save(self, filename):
        array = np.asarray(self.screenshots)
        np.save(filename, array)
        return array

    @staticmethod
    def load_data(filename):
        return np.load(filename)