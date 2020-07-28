import sys  # sys нужен для передачи argv в QApplication

import design
import design

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, BatchNormalization, Activation
from keras.constraints import maxnorm
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import load_model
import tensorflow as tf

import matplotlib.pyplot as plt
import requests
import os
from PIL import Image
import numpy
from tensorflow.python.keras.preprocessing import image


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    img = 0

    def recognize(self):
        print("a")
        model = keras.models.load_model("cat_dog/cat_dog")
        print(self.img)
        a = image.load_img(self.img, target_size=(150, 150))

        plt.imshow(a)
        img_array = image.img_to_array(a)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255

        prediction = model.predict(img_array)

        print(prediction[0])

        if prediction[0] > 0.5:
            print("DOG")
            self.prediction.appendPlainText("Это сабака!")
        else:
            print("CAT")
            self.prediction.appendPlainText("Это кит!")

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '\', "Image files (*.jpg *.gif)")')
        imagePath = fname[0]

        pixmap = QPixmap(imagePath)
        self.label.setAlignment(Qt.AlignCenter)
        self.img = imagePath
        myScaledPixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatio)
        self.label.setPixmap(myScaledPixmap)
        self.btnRecognize.setEnabled(True)

        self.show()

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        super().__init__()
        self.setupUi(self)
        self.btnImgSelect.clicked.connect(self.getImage)
        self.btnRecognize.clicked.connect(self.recognize)


def main():
    design = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    design.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()
