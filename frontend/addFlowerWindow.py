import json
import tkinter as tk
import tkinter.messagebox

import requests

import config
import frontend.windowWidget


class AddFlowerWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name):
        super().__init__(width, height, name)
        self.data = None
        self.makeLabel((20, 20, 100, 40), '花名：')
        self.nameEntry = self.makeEntry((140, 20, 200, 40))

        self.makeLabel((20, 80, 100, 40), '颜色：')
        self.colorEntry = self.makeEntry((140, 80, 200, 40))

        self.makeLabel((20, 140, 100, 40), '供应商：')
        self.offerEntry = self.makeEntry((140, 140, 200, 40))

        self.makeLabel((20, 200, 100, 40), '数量：')
        self.bucketEntry = self.makeEntry((140, 200, 200, 40))

        self.makeLabel((20, 260, 100, 40), '备注：')
        self.msgEntry = self.makeEntry((140, 260, 200, 40))

        self.makeLabel((20, 320, 100, 40), '过期时间：')
        self.dueEntry = self.makeEntry((140, 320, 200, 40))

        self.makeLabel((20, 380, 100, 40), '售价：')
        self.priceEntry = self.makeEntry((140, 380, 200, 40))

        self.insertButton = self.makeButton((240, 460, 100, 40), '添加信息', self.insertButtonPress)

        self.window.mainloop()

    def insertButtonPress(self, *args):
        name = self.nameEntry.get()
        color = self.colorEntry.get()
        offer = self.offerEntry.get()
        bucket = self.bucketEntry.get()
        msg = self.msgEntry.get()
        due = self.dueEntry.get()
        price = self.priceEntry.get()
        attachment_ids = ''
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
