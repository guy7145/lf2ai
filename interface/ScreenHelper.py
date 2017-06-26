import win32gui
from PIL import ImageGrab
import numpy as np
import cv2
import time


class ScreenHelper(object):

    captures = list()

    def __init__(self):
        self.WindowName = "Little Fighter 2"
        self.lf2wnd = win32gui.FindWindow(None, self.WindowName)
        self.lf2rect = win32gui.GetWindowRect(self.lf2wnd)
        self.captureFrame = (self.lf2rect[0], self.lf2rect[1], self.lf2rect[2], self.lf2rect[3])

    def switch_focus(self):
        win32gui.SetForegroundWindow(self.lf2wnd)

    def capture(self):
        img = ImageGrab.grab(self.captureFrame)
        # img_np = np.array(img) # shape = (578, 800, 3)
        # self.captures.append(img_np)
        self.captures.append(img)
        return

    def cast_to_np(self):
        self.captures = [np(capt) for capt in self.captures]
        return self.captures

    @staticmethod
    def show_image(img_np):
        print("showing image of shape: ")
        print(img_np.shape)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2BGRA)
        cv2.imshow("test", frame)
        cv2.waitKey(0) # waits for the user to close the popup window