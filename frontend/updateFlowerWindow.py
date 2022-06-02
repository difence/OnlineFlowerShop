import json
import tkinter as tk
import tkinter.messagebox

import requests

import config
import frontend.windowWidget


class UpdateFlowerWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name, data):
        super().__init__(width, height, name)
        self.ids = data['id']
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

        self.insertButton = self.makeButton((240, 460, 100, 40), '修改信息', self.updateButtonPress)

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
