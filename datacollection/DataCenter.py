from macpath import join

import pyHook
import pythoncom

from datacollection.DataFile import DataFile
from interface.KeyboardHelper import KeyboardHelper
from interface.ScreenHelper import ScreenHelper


class DataCenter:
    dataset_path = "D:\\_Guy\\lf2ai\\dataset\\"
    data_filename_format = "data_{}.lf2capture"
    kh = KeyboardHelper()
    sh = ScreenHelper()
    hm = pyHook.HookManager()
    files = list()
    current_file = DataFile()
    batch_size = 0

    def __init__(self):
        return

    def start_collecting(self, batch_size=100):
        self.sh.switch_focus()
        self.hm.KeyDown = self.capture
        self.batch_size = batch_size

        self.hm.HookKeyboard()
        pythoncom.PumpMessages()
        return

    def capture(self, key_event):
        if self.current_file.add_item([self.sh.capture(), self.kh.capture(key_event)]) >= self.batch_size:
            file_index = len(self.files)
            self.files.append(self.current_file)
            print("saving file {}...".format(file_index))
            self.current_file.save(self.dataset_path + self.data_filename_format.format(file_index))
            print("finished saving.")
            self.current_file = DataFile()
        return True
