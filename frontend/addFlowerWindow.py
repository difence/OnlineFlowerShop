import json
import os
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk as ttk

import cv2
import requests

import config
import frontend.windowTopLevel
import tool


class AddFlowerWindow(frontend.windowTopLevel.WindowTopLevel):
    def __init__(self, width, height, name, userId, offerData):
        super().__init__(width, height, name)
        self.picId = None
        self.pic = None
        self.data = None
        self.userId = userId
        self.offerData = offerData
        self.makeLabel((20, 20, 100, 40), '花名：')
        self.nameEntry = self.makeEntry((140, 20, 200, 40))

        self.makeLabel((20, 80, 100, 40), '颜色：')
        self.colorEntry = self.makeEntry((140, 80, 200, 40))

        self.makeLabel((20, 140, 100, 40), '供应商：')
        self.offerCombobox = ttk.Combobox(self.window)
        self.offerCombobox.place(x=140, y=140, width=200, height=40)
        self.offerIds = []

        for i in self.offerData:
            self.offerIds.append(i['id'])
        self.offerCombobox.configure(values=self.offerIds)

        self.makeLabel((20, 200, 100, 40), '数量：')
        self.bucketEntry = self.makeEntry((140, 200, 200, 40))

        self.makeLabel((20, 260, 100, 40), '备注：')
        self.msgEntry = self.makeEntry((140, 260, 200, 40))

        self.makeLabel((20, 320, 100, 40), '过期时间：')
        self.dueEntry = self.makeEntry((140, 320, 200, 40))

        self.makeLabel((20, 380, 100, 40), '售价：')
        self.priceEntry = self.makeEntry((140, 380, 200, 40))

        self.flowerLabel = self.makeLabel((20, 440, 80, 80), command=self.flowerLabelPress)

        self.insertButton = self.makeButton((240, 460, 100, 40), '添加信息', self.insertButtonPress)

        self.window.mainloop()

    def insertButtonPress(self, *args):
        name = self.nameEntry.get()
        color = self.colorEntry.get()
        offer = self.offerCombobox.get()
        bucket = self.bucketEntry.get()
        msg = self.msgEntry.get()
        due = self.dueEntry.get()
        price = self.priceEntry.get()
        attachment_ids = self.picId
        res = json.loads(
            requests.post(config.flowerInsert,
                          data={'name': name,
                                'color': color,
                                'offer_id': offer,
                                'bucket': bucket,
                                'msg': msg,
                                'due_date': due,
                                'price': price,
                                'attachment_ids': attachment_ids}).content.decode(
                'utf-8'))
        if int(res['code']) == 1:
            tk.messagebox.showinfo('添加', '添加成功')
            self.window.destroy()

    def flowerLabelPress(self, *args):
        path = tk.filedialog.askopenfilename()
        fname = os.path.split(path)[1]
        name, type = os.path.splitext(fname)
        res = requests.post(config.fileUpload, data={'update_id': self.userId,
                                                     'name': name,
                                                     'type': type[1:],
                                                     'tname': fname}).content.decode('utf-8')
        res = json.loads(res)
        resUrl = res['data']['url']
        resId = res['data']['id']
        self.picId = resId

        img = cv2.imread(path)
        img = cv2.resize(img, (80, 80))
        cv2.imwrite(f'./{name}.jpg', img)
        with open(f'./{name}.jpg', 'rb') as f:
            z = requests.put(resUrl, f)
            if str(z.status_code) == '200':
                tk.messagebox.showinfo('修改', '图片上传成功')
        self.pic = tool.fun.pic2TKpic(f'./{name}.jpg', (80, 80))
        self.flowerLabel.configure(image=self.pic)
        if os.path.exists(f'./{name}.jpg'):
            os.remove(f'./{name}.jpg')
