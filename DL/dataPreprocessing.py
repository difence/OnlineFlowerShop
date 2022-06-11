import os
import random

import cv2
import numpy as np


def ImgToNumpy(image, theory=cv2.COLOR_BGR2RGB, size=None):
    image = cv2.imread(image)
    if size:
        image = cv2.resize(image, size)
    image = cv2.cvtColor(image, theory)
    return image


def getDict2Label():
    dic = {'daisy': 0, 'dandelion': 1, 'roses': 2, 'sunflowers': 3, 'tulips': 4}
    return dic


def getDict2Name():
    res = getDict2Label()
    res = {v: k for k, v in res.items()}
    return res


def readData(path="", size=(128, 128), rand=0.3):
    if path == "":
        raise ValueError("清输入正确的路径地址")

    dic = {'daisy': 0, 'dandelion': 1, 'roses': 2, 'sunflowers': 3, 'tulips': 4}

    x_train = []
    y_train = []
    x_test = []
    y_test = []

    data = []

    for i in os.listdir(path):
        for j in os.listdir(f'{path}/{i}/'):
            p = f'{path}/{i}/{j}'
            data.append([ImgToNumpy(p, size=size), dic[i]])

    data = np.array(data)
    np.random.shuffle(data)

    for i in data:
        x = i[0]
        y = i[1]
        if random.random() < rand:
            x_test.append(x)
            y_test.append(y)
        else:
            x_train.append(x)
            y_train.append(y)

    x_train = np.array(x_train) / 255.0
    y_train = np.array(y_train)
    x_test = np.array(x_test) / 255.0
    y_test = np.array(y_test)

    return (x_train, y_train), (x_test, y_test)
