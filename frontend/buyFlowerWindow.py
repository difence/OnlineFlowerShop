import json
import tkinter as tk
import tkinter.messagebox

import requests

import config
import frontend.windowWidget


class UpdateFlowerWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name, data, userId):
        super().__init__(width, height, name)
        self.ids = data['id']
        self.userId = userId
        self.makeLabel((20, 20, 200, 40), '花名：{}'.format(data['name']))

        self.makeLabel((20, 80, 200, 40), '颜色：{}'.format(data['color']))

        self.makeLabel((20, 140, 200, 40), '供应商：'.format(data['offer_id']))

        self.makeLabel((20, 200, 200, 40), '购买数量：')
        self.bucketEntry = self.makeText((240, 200, 40, 40))
        self.bucketEntry.insert('end', data['bucket'])

        self.makeLabel((20, 260, 200, 40), '备注：{}'.format(data['msg']))

        self.makeLabel((20, 320, 200, 40), '售价：{}'.format(data['price']))

        self.insertButton = self.makeButton((240, 400, 100, 40), '购买', self.updateButtonPress)

        self.window.mainloop()

    def updateButtonPress(self, *args):
        bucket = self.bucketEntry.get('0.0', tk.END)[:-1]
        res = json.loads(
            requests.post(config.flowerBuy,
                          data={'id': self.ids,
                                'user_id': self.userId,
                                'bucket': bucket}).content.decode(
                'utf-8'))
        if int(res['code']) == 1:
            tk.messagebox.showinfo('购买', '购买成功')
            self.window.destroy()

        elif int(res['code']) == 2:
            tk.messagebox.showinfo('购买', '购买失败，库存不足')
            self.window.destroy()

        elif int(res['code']) == 0:
            tk.messagebox.showinfo('购买', '购买失败')
            self.window.destroy()
