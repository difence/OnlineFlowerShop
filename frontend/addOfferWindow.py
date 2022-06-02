import json
import tkinter as tk
import tkinter.messagebox

import requests

import config
import frontend


class MainWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name):
        super().__init__(width, height, name)
        self.data = None
        self.makeLabel((20, 20, 160, 40), '供应商：')
        self.nameText = self.makeText((200, 20, 180, 40))
        self.msgText = self.makeText((20, 80, 360, 140))

        self.insertButton = self.makeButton((240, 240, 100, 40), '添加信息', self.insertButtonPress)

        self.window.mainloop()

    def insertButtonPress(self, *args):
        name = self.nameText.get('0.0', tk.END)[:-1]
        msg = self.msgText.get('0.0', tk.END)[:-1]
        attachment_ids = ''
        res = json.loads(
            requests.post(config.offerInsert,
                          data={'name': name, 'msg': msg, 'attachment_ids': attachment_ids}).content.decode(
                'utf-8'))
        if int(res['code']) == 1:
            tk.messagebox.showinfo('添加', '添加成功')
            self.window.destroy()
        pass
        pass
