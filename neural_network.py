from keras.models import Model, Sequential
from keras.layers import Input, Convolution2D, MaxPooling2D, ZeroPadding2D, Conv2D, UpSampling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.models import load_model


def generate_autoencoder():

    # model = Sequential()
    #
    # model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(800, 578, 3)))
    # model.add(MaxPooling2D((2, 2)))
    # model.add(Convolution2D(16, 3, 3, activation='relu'))
    # model.add(MaxPooling2D((2, 2)))
    # model.add(Convolution2D(16, 3, 3, activation='relu'))
    # encoded = MaxPooling2D((2, 2));
    # model.add(encoded)
    #
    # model.add(Conv2D(16, (3, 3), activation='relu'))
    # model.add(UpSampling2D((2, 2)))
    # model.add(Conv2D(16, (3, 3), activation='relu'))
    # model.add(UpSampling2D((2, 2)))
    # model.add(Conv2D(32, (3, 3), activation='relu'))
    # model.add(UpSampling2D((2, 2)))
    # decoded = Conv2D(1, (3, 3), activation='sigmoid')
    # model.add(decoded)
    #
    # return model

    input_img = Input(shape=(800, 578, 3))  # adapt this if using `channels_first` image data format
    x = Dense()

    x = Conv2D(16, (3, 3), activation='relu', padding='same')(input_img)
    x = MaxPooling2D((2, 2), padding='same')(x)
    x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
    x = MaxPooling2D((2, 2), padding='same')(x)
    x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
    encoded = MaxPooling2D((2, 2), padding='same')(x)

    # at this point the representation is (4, 4, 8) i.e. 128-dimensional

    x = Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
    x = UpSampling2D((2, 2))(x)
    x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
    x = UpSampling2D((2, 2))(x)
    x = Conv2D(16, (3, 3), activation='relu')(x)
    x = UpSampling2D((2, 2))(x)
    decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)

    autoencoder = Model(input_img, decoded)
    autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

    return autoencoder