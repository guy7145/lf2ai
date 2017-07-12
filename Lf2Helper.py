import interface.KeyboardHelper as kh


class Lf2Helper:
    frame_crop_size = {"left": 2, "right": 2, "top": 30, "bottom": 40}

    # game controls
    key_up = kh.VK_w
    key_down = kh.VK_s
    key_left = kh.VK_a
    key_right = kh.VK_d
    key_attack = kh.VK_i
    key_jump = kh.VK_o
    key_guard = kh.VK_p

    num_of_keys = 7

    keys = [key_up, key_down, key_left, key_right, key_attack, key_jump, key_guard]

    def __init__(self):

        return

    @staticmethod
    def analyze_situation(img):
        print("margin_img naive")
        result = img
        return result

    @staticmethod
    def get_player_health(img):
        print("get_player_health unimplemented")
        return 100

    def get_keys_from_map(self, key_map):
        chosen_keys = list()
        for key, m in zip(self.keys, key_map):
            if m == 1:
                chosen_keys.append(key)
        return chosen_keys
