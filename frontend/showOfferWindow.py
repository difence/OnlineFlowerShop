import json
import tkinter as tk
import tkinter.messagebox

import requests

import config
import frontend


class ShowOfferWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name, data):
        super().__init__(width, height, name)
        self.data = None
        self.ids = data['id']
        data = json.loads(requests.post(config.offerGetById, {'id': self.ids}).content.decode('utf-8'))
        self.data = data['data']

        self.nameText = self.makeText((20, 20, 360, 40))
        self.msgText = self.makeText((20, 80, 360, 140))

        self.nameText.insert('end', self.data['name'])
        self.msgText.insert('end', self.data['msg'])

        self.removeButton = self.makeButton((20, 240, 100, 40), '删除信息', self.removeButtonPress)
        self.updateButton = self.makeButton((140, 240, 100, 40), '修改信息', self.updateButtonPress)

        self.window.mainloop()

    def updateButtonPress(self, *args):
        name = self.nameText.get('0.0', tk.END)[:-1]
        msg = self.msgText.get('0.0', tk.END)[:-1]
        res = json.loads(
            requests.post(config.offerUpdateById, data={'id': self.ids, 'name': name, 'msg': msg}).content.decode(
                'utf-8'))
        if int(res['code']) == 1:
            tk.messagebox.showinfo('修改', res['msg'])
            self.window.destroy()
        pass

    def removeButtonPress(self, *args):
        res = json.loads(
            requests.post(config.offerRemoveById, data={'id': self.ids}).content.decode(
                'utf-8'))
        if int(res['code']) == 1:
            tk.messagebox.showinfo('删除', res['msg'])
            self.window.destroy()
        pass
