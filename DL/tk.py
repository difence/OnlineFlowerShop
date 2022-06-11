import datetime
import os.path
import time
import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import (askopenfilename)

import PIL
import cv2
import numpy as np
import tensorflow.keras as keras
from PIL import Image, ImageTk

import dataPreprocessing as dp

global pic, loginFlag, globalAccount, userPicture, cap, capFlag, capPicture, capLabelPicture, flowerRecognizePicture, \
    tempWindow, infoPicture, infoNumber
loginFlag = 0
capFlag = 0

(IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS) = (64, 64, 3)

cap = cv2.VideoCapture(0)

model = keras.models.load_model('./model{}x{}.h5'.format(IMG_HEIGHT, IMG_WIDTH))


def pic2TKpic(img, img_size):
    '''
    png图片转为tk格式图片
    :param img:
    :param img_size:
    :return:
    '''
    img_ = cv2.imread(img)
    img__ = cv2.resize(img_, img_size)
    img__ = cv2.cvtColor(img__, cv2.COLOR_BGR2RGB)
    img___ = Image.fromarray(img__)
    img____ = ImageTk.PhotoImage(image=img___)
    return img____


def cv2TKpic(img, img_size):
    """
    cv2格式图片转化为矩阵图片
    :param img:
    :param img_size:
    :return:
    """
    img_ = cv2.imread(img)
    img__ = cv2.resize(img_, img_size)
    img___ = Image.fromarray(img__)
    img____ = ImageTk.PhotoImage(image=img___)
    return img____


def readAccountFile(path='./account.txt'):
    """
    读取登录信息
    :param path:
    :return:
    """
    f = open(path, 'r', encoding='utf-8').readlines()
    res = [i.replace("\n", "").split(" ") for i in f]
    return res


def writeAccountFile(accSheet, path='./account.txt'):
    """
    写入注册信息
    :param accSheet:
    :param path:
    :return:
    """
    f = open(path, 'a+', encoding='utf-8')
    f.write(accSheet)
    f.close()


def loginButtonPress(*args):
    """
    登录功能
    :param args:
    :return:
    """
    global loginFlag, globalAccount
    acc = accountEntry.get()
    pas = passwordEntry.get()
    accSheet = readAccountFile()
    for i in range(len(accSheet)):
        if acc == accSheet[i][0] and pas == accSheet[i][1]:
            loginWindow.destroy()
            loginFlag = 1
            globalAccount = acc
            return
    tk.messagebox.showwarning('warning', message='账号或密码有误')


def registerButtonPress(*args):
    """
    注册功能
    :param args:
    :return:
    """
    acc = accountEntry.get()
    pas = passwordEntry.get()
    accSheet = readAccountFile()
    for i in range(len(accSheet)):
        if acc == accSheet[i][0]:
            tk.messagebox.showwarning('warning', message='账号已存在')
            return
    writeAccountFile("\n" + acc + " " + pas)
    tk.messagebox.showwarning('warning', message='账号注册成功')


def userPictureLabelPress(*args):
    """
    用户头像更好
    :param args:
    :return:
    """
    global userPicture
    path = askopenfilename()
    img = cv2.imread(path)
    img = cv2.resize(img, (100, 100))
    cv2.imwrite('./pic/{}.png'.format(globalAccount), img)
    userPicture = pic2TKpic('./pic/{}.png'.format(globalAccount), (100, 100))
    userPictureLabel.config(image=userPicture)
    pass


def getVideoCapButtonPress(*args):
    """
    录像、截屏
    :param args:
    :return:
    """
    global capFlag, videoWindowCanvas, capPicture
    if capFlag == 0:
        showCap()
    else:
        closeCap()
        return

    while True:
        if capFlag == 0:
            break
        flag, frame = cap.read()
        cov = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cov = cv2.resize(cov, (300, 300))
        capPicture = cov
        img = PIL.Image.fromarray(cov)
        img = PIL.ImageTk.PhotoImage(img)
        videoWindowCanvas.create_image(150, 150, image=img)
        mainWindow.update_idletasks()
        mainWindow.update()


def closeCap():
    """
    关闭摄像头
    :return:
    """
    global capFlag, videoWindowCanvas, capPicture, capLabelPicture
    capFlag = 0
    cv2.imwrite('temp.png', capPicture)
    capLabelPicture = cv2TKpic('temp.png', (300, 300))
    videoWindowCanvas.place(x=1000, y=1000, width=10, height=10)
    videoWindowLabel.place(x=140, y=140, width=300, height=300)
    videoWindowLabel.config(image=capLabelPicture)
    mainWindow.update_idletasks()
    mainWindow.update()
    print("close cap")


def showCap():
    """
    打开摄像头
    :return:
    """
    global capFlag, videoWindowCanvas
    capFlag = 1
    videoWindowCanvas.place(x=140, y=140, width=300, height=300)
    videoWindowLabel.place(x=1000, y=1000, width=300, height=300)
    mainWindow.update_idletasks()
    mainWindow.update()

    print("show cap")


def getFileButtonPress(*args):
    """
    选择本地文件
    :param args:
    :return:
    """
    global capLabelPicture
    path = askopenfilename()
    if capFlag == 1:
        closeCap()
    img = cv2.imread(path)
    cv2.imwrite("./temp.png", img)
    capLabelPicture = pic2TKpic("./temp.png", (300, 300))
    videoWindowLabel.config(image=capLabelPicture)
    pass


def lockPicturePress(*args):
    """
    锁定图片
    :param args:
    :return:
    """
    if capFlag == 1:
        closeCap()
    else:
        tk.messagebox.showwarning("提示", "未打开摄像头")
    pass


def recognizeButtonPress(*args):
    """
    开始识别图片
    :param args:
    :return:
    """
    global tempWindow
    if capFlag == 1:
        tk.messagebox.showwarning("提示", "摄像头未关闭")
        return
    if capLabelPicture is None:
        tk.messagebox.showwarning("提示", "未选取图片")
        return
    mainWindow.destroy()
    tempWindow = 2
    pass


def saveButtonPress(*args):
    """
    保存花卉信息
    :param args:
    :return:
    """
    fa = open('info.txt', 'a', encoding="utf-8")
    t = str(int(time.time()))
    fa.write("{} {} {} {}\n".format(globalAccount, a, datetime.datetime.today(), t))
    fa.close()
    fa = open("./data/flower/{}.txt".format(t), 'w', encoding='utf-8')
    fa.close()
    fpic = cv2.imread('temp.png')
    cv2.imwrite("./data/flower/{}.png".format(t), fpic)


def readFile():
    """
    读取花卉信息
    :return:
    """
    ff = open('info.txt', 'r', encoding="utf-8")
    z = ff.readlines()
    ff.close()
    zz = []
    for i in z:
        zz.append(i.replace("\n", "").split(" "))
    return zz


def infoButtonPress(*args):
    """
    进入个人历史记录
    :param args:
    :return:
    """
    global tempWindow
    mainWindow.destroy()
    tempWindow = 1
    pass


def showTablePress(*args):
    global infoPicture, infoNumber
    """
    打开记录手册
    :param args:
    :return:
    """
    s = showTable.get(showTable.curselection())
    idx = s.split(" ")[-1]
    infoNumber = idx
    s = idx + ".txt"
    s = './data/flower/' + s
    t = open(s, 'r', encoding='utf-8').read()
    infoLabel.insert('end', t)
    infoPicture = pic2TKpic('./data/flower/{}.png'.format(idx), (380, 380))
    infoPictureLabel.config(image=infoPicture)


def infoSaveTextButtonPress(*args):
    """
    保存最新的记录按钮
    :param args:
    :return:
    """
    t = infoLabel.get("1.0", tk.END)
    f = open('./data/flower/{}.txt'.format(infoNumber), 'w', encoding='utf-8')
    f.write(t)
    f.close()
    pass


def infoChangePictureButtonPress(*args):
    """
    更新图片按钮
    :param args:
    :return:
    """
    global infoPicture
    path = askopenfilename()
    fpic = cv2.imread(path)
    cv2.imwrite('./data/flower/{}.png'.format(infoNumber), fpic)
    infoPicture = pic2TKpic(path, (380, 380))
    infoPictureLabel.config(image=infoPicture)
    pass


loginWindow = tk.Tk()
loginWindow.geometry("400x200")
loginWindow.title('登录')
loginWindow.resizable(False, False)

accountLabel = tk.Label(loginWindow, text="账号", bg='lightblue')
accountLabel.place(x=20, y=20, width=100, height=40)

passwordLabel = tk.Label(loginWindow, text="密码", bg='lightblue')
passwordLabel.place(x=20, y=80, width=100, height=40)

accountEntry = tk.Entry(loginWindow)
accountEntry.place(x=140, y=20, width=240, height=40)

passwordEntry = tk.Entry(loginWindow)
passwordEntry.place(x=140, y=80, width=240, height=40)

loginButton = tk.Button(loginWindow, text="登录", bg='pink', command=loginButtonPress)
loginButton.place(x=60, y=140, width=100, height=40)

registerButton = tk.Button(loginWindow, text='注册', bg='pink', command=registerButtonPress)
registerButton.place(x=240, y=140, width=100, height=40)

loginWindow.mainloop()

globalAccount = "admin"
# if loginFlag == 0:
#     exit(0)
while True:
    mainWindow = tk.Tk()
    mainWindow.geometry("800x600")
    mainWindow.title('主页面')
    mainWindow.resizable(False, False)

    userPictureLabel = tk.Label(mainWindow, bg='lightblue')
    userPictureLabel.place(x=20, y=20, width=100, height=100)
    userPictureLabel.bind("<Button-1>", userPictureLabelPress)
    if os.path.exists('./pic/{}.png'.format(globalAccount)):
        userPicture = pic2TKpic('./pic/{}.png'.format(globalAccount), (100, 100))
        userPictureLabel.config(image=userPicture)
    else:
        userPictureLabel.config(text="单击上传图片")

    userNameLabel = tk.Label(mainWindow, text=globalAccount, bg='lightblue')
    userNameLabel.place(x=140, y=50, width=300, height=40)

    videoWindowCanvas = tk.Canvas(mainWindow, bg='pink')
    videoWindowCanvas.place(x=140, y=140, width=300, height=300)

    videoWindowLabel = tk.Label(mainWindow, bg='pink')
    videoWindowLabel.place(x=140, y=140, width=300, height=300)

    getVideoCapButton = tk.Button(mainWindow, text="打开摄像头", bg="lightyellow", command=getVideoCapButtonPress)
    getVideoCapButton.place(x=460, y=140, width=100, height=40)

    getFileButton = tk.Button(mainWindow, text="选择文件", bg="lightyellow", command=getFileButtonPress)
    getFileButton.place(x=460, y=200, width=100, height=40)

    lockPictureButton = tk.Button(mainWindow, text="锁定摄像头", bg="lightyellow", command=lockPicturePress)
    lockPictureButton.place(x=460, y=260, width=100, height=40)

    recognizeButton = tk.Button(mainWindow, text="开始识别", bg="lightyellow", command=recognizeButtonPress)
    recognizeButton.place(x=460, y=320, width=100, height=40)

    infoButton = tk.Button(mainWindow, text="进入日记", bg='lightyellow', command=infoButtonPress)
    infoButton.place(x=460, y=380, width=100, height=40)

    mainWindow.mainloop()

    if tempWindow == 2:

        recognizeWindow = tk.Tk()
        recognizeWindow.geometry("800x600")
        recognizeWindow.title('识别页面')
        recognizeWindow.resizable(False, False)

        flowerRecognizePicture = pic2TKpic("./temp.png", (300, 300))

        flowerShowLabel = tk.Label(recognizeWindow, image=flowerRecognizePicture)
        flowerShowLabel.place(x=20, y=20, width=300, height=300)

        # Label2.config(text=res)

        f = dp.ImgToNumpy("./temp.png", size=(IMG_HEIGHT, IMG_WIDTH))
        f = np.array([f]).astype('float32') / 255.0
        a = model.predict(f)
        a = np.argmax(a, axis=1)[0]
        print(a)

        resultLabel = tk.Label(recognizeWindow, text=str(dp.getDict2Name()[a]), bg='pink')
        resultLabel.place(x=20, y=340, width=300, height=40)
        word = open("./data/word/{}.txt".format(a), 'r', encoding="utf-8").read()
        infoLabel = tk.Text(recognizeWindow, bg='lightblue')
        infoLabel.place(x=340, y=20, width=300, height=400)
        infoLabel.insert('end', word)

        saveButton = tk.Button(recognizeWindow, text="保存信息", bg="lightyellow", command=saveButtonPress)
        saveButton.place(x=340, y=440, width=300, height=40)

        recognizeWindow.mainloop()

    else:
        infoWindow = tk.Tk()
        infoWindow.geometry("800x600")
        infoWindow.title('花花笔记')
        infoWindow.resizable(False, False)

        data = readFile()

        res = []
        for i in data:
            if i[0] == globalAccount:
                res.append(i)

        showTable = tk.Listbox(infoWindow, bg="pink")
        showTable.place(x=20, y=20, width=360, height=560)
        showTable.bind("<Button-1>", showTablePress)
        for i in res:
            showTable.insert("end", "{} {} {} {} {}".format(i[0], dp.getDict2Name()[int(i[1])], i[2], i[3], i[4]))

        infoPictureLabel = tk.Label(infoWindow, bg='lightblue')
        infoPictureLabel.place(x=400, y=20, width=380, height=380)

        infoLabel = tk.Text(infoWindow, bg='lightblue')
        infoLabel.place(x=400, y=420, width=380, height=100)

        infoChangePictureButton = tk.Button(infoWindow, text="更换图片", bg='lightyellow',
                                            command=infoChangePictureButtonPress)
        infoChangePictureButton.place(x=400, y=540, width=100, height=40)

        infoSaveTextButton = tk.Button(infoWindow, text="保存文本", bg='lightyellow', command=infoSaveTextButtonPress)
        infoSaveTextButton.place(x=680, y=540, width=100, height=40)

        infoWindow.mainloop()

    if os.path.exists("temp.png"):
        os.remove("temp.png")
