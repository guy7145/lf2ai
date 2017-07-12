import win32gui
from PIL import ImageGrab, Image
import numpy as np
import cv2
import time


class ScreenHelper(object):

    def __init__(self, margin={"left": 0, "right": 0, "top": 0, "bottom": 0}):
        self.WindowName = "Little Fighter 2"
        self.lf2wnd = win32gui.FindWindow(None, self.WindowName)
        self.lf2rect = win32gui.GetWindowRect(self.lf2wnd)
        self.captureFrame = (self.lf2rect[0] + margin["left"],
                             self.lf2rect[1] + margin["top"],
                             self.lf2rect[2] - margin["right"],
                             self.lf2rect[3] - margin["bottom"])

    def switch_focus(self):
        win32gui.SetForegroundWindow(self.lf2wnd)

    def capture(self):
        img = ImageGrab.grab(self.captureFrame)
        img_np = np.array(img) # shape = (578, 800, 3)
        # self.captures.append(img_np)
        # self.captures.append(img)
        return img_np

    def cast_to_np(self):
        self.captures = [np(capt) for capt in self.captures]
        return self.captures

    @staticmethod
    def show_image(img_np):
        print("showing image of shape: ")
        print(img_np.shape)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        print(frame.shape)
        cv2.imshow("test", frame)
        cv2.waitKey(0) # waits for the user to close the popup window