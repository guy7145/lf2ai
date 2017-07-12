from random import shuffle
from time import sleep

from Lf2Helper import Lf2Helper
from interface.KeyboardHelper import KeyboardHelper
from interface.ScreenHelper import ScreenHelper
import numpy as np


class VirtualPlayer:

    lf2 = Lf2Helper()
    kh = KeyboardHelper()
    sh = ScreenHelper(lf2.frame_crop_size)
    ann = "none"
    possible_actions_dim = ""

    def __init__(self, possible_actions_dim):
        self.possible_actions_dim = possible_actions_dim
        return

    def focus(self):
        self.sh.switch_focus()
        return

    def see(self):
        img = self.sh.capture()
        return img

    def play(self):
        while True:
            actions = self.decide_action(self.evaluate_situation(self.see()))
            self.kh.press_keys(*actions) # extend to support different attacks and not just keys
            sleep(0.0001)
        return

    def learn(self):
        print("learn UNIMPLEMENTED")
        return

    def evaluate_situation(self, img):
        situation = self.lf2.analyze_situation(img)  # optimized screen image + enemies' HP and MP + player's HP and MP
        return situation

    def decide_action(self, situation):
        # actions = self.ann.predict(situation)   # separate image from other parameters
        # randomly choose 3 keys
        actions = np.zeros(self.possible_actions_dim)
        actions[0] = actions[1] = actions[2] = 1
        shuffle(actions)
        return self.lf2.get_keys_from_map(actions)
