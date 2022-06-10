import json
import os
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

import cv2
import requests

import config
import frontend.windowTopLevel
import tool


class UpdateFlowerWindow(frontend.windowTopLevel.WindowTopLevel):
    def __init__(self, width, height, name, data, userId):
        super().__init__(width, height, name)
        self.pic = None
        self.ids = data['id']
        self.data = data
        self.userId = userId
        self.makeLabel((20, 20, 100, 40), '花名：')
        self.nameEntry = self.makeText((140, 20, 200, 40))
        self.nameEntry.insert('end', data['name'])

        self.makeLabel((20, 80, 100, 40), '颜色：')
        self.colorEntry = self.makeText((140, 80, 200, 40))
        self.colorEntry.insert('end', data['color'])

        self.makeLabel((20, 140, 100, 40), '供应商：')
        self.offerEntry = self.makeText((140, 140, 200, 40))
        self.offerEntry.insert('end', data['offer_id'])

        self.makeLabel((20, 200, 100, 40), '数量：')
        self.bucketEntry = self.makeText((140, 200, 200, 40))
        self.bucketEntry.insert('end', data['bucket'])

        self.makeLabel((20, 260, 100, 40), '备注：')
        self.msgEntry = self.makeText((140, 260, 200, 40))
        self.msgEntry.insert('end', data['msg'])

        self.makeLabel((20, 320, 100, 40), '过期时间：')
        self.dueEntry = self.makeText((140, 320, 200, 40))
        self.dueEntry.insert('end', data['due_date'])

        self.makeLabel((20, 380, 100, 40), '售价：')
        self.priceEntry = self.makeText((140, 380, 200, 40))
        self.priceEntry.insert('end', data['price'])

        self.flowerLabel = self.makeLabel((20, 440, 80, 80), command=self.flowerLabelPress)

        self.insertButton = self.makeButton((240, 460, 100, 40), '修改信息', self.updateButtonPress)
        self.initPic()
        self.window.mainloop()

    def updateButtonPress(self, *args):
        name = self.nameEntry.get('0.0', tk.END)[:-1]
        color = self.colorEntry.get('0.0', tk.END)[:-1]
        offer = self.offerEntry.get('0.0', tk.END)[:-1]
        bucket = self.bucketEntry.get('0.0', tk.END)[:-1]
        msg = self.msgEntry.get('0.0', tk.END)[:-1]
        due = self.dueEntry.get('0.0', tk.END)[:-1]
        price = self.priceEntry.get('0.0', tk.END)[:-1]
        attachment_ids = ''
        res = json.loads(
            requests.post(config.flowerUpdateNumberById,
                          data={'id': self.ids,
                                'name': name,
                                'color': color,
                                'offer_id': offer,
                                'bucket': bucket,
                                'msg': msg,
                                'due_date': due,
                                'price': price,
                                'attachment_ids': attachment_ids}).content.decode(
                'utf-8'))
        if int(res['code']) == 1:
            tk.messagebox.showinfo('添加', '修改成功')
            self.window.destroy()

    def initPic(self):
        try:
            picId = self.data['attachment_ids']
            res = requests.post(config.fileDownloadById, data={'id': picId}).content.decode('utf-8')
            res = json.loads(res)['data']['url']
            pic = requests.get(res, data={'id': picId}).content
            with open('temp.jpg', 'bw') as f:
                f.write(pic)
            self.pic = tool.fun.pic2TKpic(f'./temp.jpg', (80, 80))
            self.flowerLabel.configure(image=self.pic)
            if os.path.exists(f'./temp.jpg'):
                os.remove(f'./temp.jpg')
        except:
            pass

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

        img = cv2.imread(path)
        img = cv2.resize(img, (80, 80))
        cv2.imwrite(f'./{name}.jpg', img)
        with open(f'./{name}.jpg', 'rb') as f:
            z = requests.put(resUrl, f)
            if str(z.status_code) == '200':
                tk.messagebox.showinfo('修改', '图片修改成功')
        self.pic = tool.fun.pic2TKpic(f'./{name}.jpg', (80, 80))
        self.flowerLabel.configure(image=self.pic)
        requests.post(config.flowerUpdateAttsById, data={'id': self.data['id'], 'attachment_ids': resId})
        if os.path.exists(f'./{name}.jpg'):
            os.remove(f'./{name}.jpg')
