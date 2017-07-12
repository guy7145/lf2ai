from VirtualPlayer import VirtualPlayer
from interface.ScreenHelper import ScreenHelper

sh = ScreenHelper()

vp = VirtualPlayer(7)
vp.focus()
vp.play()
# sh.show_image(vp.see())

#
# data_filename = "screenshots_as_np_arrays.npy"
#
# flags
# capture_mode = False
# train_autoencoder = False
# show_capture = False
#
# if capture_mode:
#     sh = ScreenHelper()
#     cp = DataFile()
#     countdown_limit = 10
#
#     sh.switch_focus()
#     for i in range (1, countdown_limit):
#         print("{}...".format(countdown_limit - i)) # print count down in a descending order
#
#     for i in range(1500):
#         x = sh.capture()
#         cp.add_item(x)
#         time.sleep(0.1)
#         print("captured {} screenshots".format(i + 1))
#     print("finished capturing")
#
#     print("saving data to {}...".format(data_filename))
#     data = cp.save(data_filename)
#     print("finished saving")
#
#     if show_capture:
#         print("showing capture:")
#         for arr in data:
#             ScreenHelper.show_image(arr)
#
# if train_autoencoder:
#
#     print("generating model...")
#     autoencoder = generate_autoencoder()
#
#     print("loading data...")
#     data = DataFile.load_data(data_filename)
#
#     if show_capture:
#         print("showing capture:")
#         for arr in data:
#             ScreenHelper.show_image(arr)
#
#     # y_train = x_train = data
#     datagen = ImageDataGenerator(rescale=1./255)
#     datagen.fit(data)
#
#     print("training model...")
#     autoencoder.fit_generator(datagen.flow(data, data, batch_size=32), epochs=10, steps_per_epoch=50)

print("goodbye")
