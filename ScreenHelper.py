import win32gui
from PIL import ImageGrab
import numpy as np
import cv2
import time


class ScreenHelper(object):

    def __init__(self):
        self.WindowName = "Little Fighter 2"
        self.lf2wnd = win32gui.FindWindow(None, self.WindowName)
        self.lf2rect = win32gui.GetWindowRect(self.lf2wnd)
        self.captureFrame = (self.lf2rect[0], self.lf2rect[1], self.lf2rect[2], self.lf2rect[3])

    def switch_focus(self):
        win32gui.SetForegroundWindow(self.lf2wnd)

    def capture_screen(self):
        img = ImageGrab.grab(self.captureFrame)
        img_np = np.array(img) # shape = (578, 800, 3)
        return img_np

    @staticmethod
    def show_image(img_np):
        print("showing image of shape: ")
        print(img_np.shape)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2BGRA)
        cv2.imshow("test", frame)
        cv2.waitKey(0) # waits for the user to close the popup window