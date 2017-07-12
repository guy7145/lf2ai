import time
import numpy as np

from interface.keyboard import PressKey, ReleaseKey

# numbers
VK_0 = 0x30
VK_1 = 0x31
VK_2 = 0x32
VK_3 = 0x33
VK_4 = 0x34
VK_5 = 0x35
VK_6 = 0x36
VK_7 = 0x37
VK_8 = 0x38
VK_9 = 0x39
# letters
VK_a = 0x41
VK_b = 0x42
VK_c = 0x43
VK_d = 0x44
VK_e = 0x45
VK_f = 0x46
VK_g = 0x47
VK_h = 0x48
VK_i = 0x49
VK_j = 0x4A
VK_k = 0x4B
VK_l = 0x4C
VK_m = 0x4D
VK_n = 0x4E
VK_o = 0x4F
VK_p = 0x50
VK_q = 0x51
VK_r = 0x52
VK_s = 0x53
VK_t = 0x54
VK_u = 0x55
VK_v = 0x56
VK_w = 0x57
VK_x = 0x58
VK_y = 0x59
VK_z = 0x5A

class KeyboardHelper:

    # def kick_jump_right(self):
    #     self.press_keys(self.key_right, self.key_jump, self.key_attack)
    #
    # def kick_jump_left(self):
    #     self.press_keys(self.key_left, self.key_jump, self.key_attack)

    @staticmethod
    def press_keys(*keys):

        for key in keys:
            PressKey(key)

        time.sleep(0.1)

        for key in keys:
            ReleaseKey(key)

        return
