from keyboard import PressKey
from keyboard import ReleaseKey
# from ScreenHelper import ScreenHelper
# from createDataset import capture_dataset
# from neural_network import *
import time

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


# game constrols
key_up = VK_i
key_down = VK_k
key_left = VK_j
key_right = VK_l
key_attack = VK_8
key_jump = VK_9
key_guard = VK_o


def kick_jump_right():
    PressKey(key_right)
    PressKey(key_jump)
    PressKey(key_attack)
    time.sleep(1)
    ReleaseKey(key_right)
    ReleaseKey(key_jump)
    ReleaseKey(key_attack)
    time.sleep(1)


def kick_jump_left():
    PressKey(key_left)
    PressKey(key_jump)
    PressKey(key_attack)
    time.sleep(1)
    ReleaseKey(key_left)
    ReleaseKey(key_jump)
    ReleaseKey(key_attack)
    time.sleep(1)


def explode():
    PressKey(key_guard)
    PressKey(key_jump)
    PressKey(key_up)
    time.sleep(1)
    ReleaseKey(key_guard)
    ReleaseKey(key_jump)
    ReleaseKey(key_up)
    time.sleep(1)


data_filename = "C:\_Guy\Private\Workspace\Python\lf2AI\screenshots_as_np_arrays.npy"

# flags
capture_mode = False
train_autoencoder = False
show_capture = False


if capture_mode:
    sh = ScreenHelper()
    cp = capture_dataset()
    countdown_limit = 10

    sh.switch_focus()
    for i in range (1, countdown_limit):
        print("{}...".format(countdown_limit - i)) # print count down in a descending order
        time.sleep(1)

    for i in range(1500):
        x = sh.capture_screen()
        cp.add_screenshot(x)
        time.sleep(0.1)
        print("captured {} screenshots".format(i + 1))
    print("finished capturing")

    print("saving data to {}...".format(data_filename))
    data = cp.save(data_filename)
    print("finished saving")

    if show_capture:
        print("showing capture:")
        for arr in data:
            ScreenHelper.show_image(arr)

if train_autoencoder:
    print("loading data...")
    data = capture_dataset.load_data(data_filename)

    if show_capture:
        print("showing capture:")
        for arr in data:
            ScreenHelper.show_image(arr)

    # y_train = x_train = data
    datagen = ImageDataGenerator(rescale=1./255)
    datagen.fit(data)

    print("generating model...")
    autoencoder = generate_autoencoder()
    print("training model...")
    autoencoder.fit_generator(datagen.flow(data, data, batch_size=32), samples_per_epoch=50, epochs=10)

print("goodbye")
time.sleep(5)
for i in range(0, 99):
    for j in range(0, 4):
        time.sleep(2)
        explode()
    kick_jump_right()
    kick_jump_left()