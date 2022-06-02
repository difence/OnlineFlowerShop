import json
import tkinter as tk
import tkinter.messagebox

import requests

import config
import frontend


class MainWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name, ids):
        super().__init__(width, height, name)
        self.ids = ids

        self.makeButton((20, 20, 200, 40), '已完成', self.button0)

        self.makeButton((20, 80, 200, 40), '配送', self.button1)

        self.makeButton((20, 140, 200, 40), '挂起', self.button2)

        self.makeButton((20, 200, 200, 40), '退款', self.button3)

    def button0(self, *args):
        a = json.loads(
            requests.post(config.orderUpdateStatusById, {'id': self.ids, 'status': 0}).content.decode('utf-8'))
        if int(a['code']) == 1:
            tk.messagebox.showinfo('提示', '修改成功')
            self.window.destroy()

    def button1(self, *args):
        a = json.loads(
            requests.post(config.orderUpdateStatusById, {'id': self.ids, 'status': 1}).content.decode('utf-8'))
        if int(a['code']) == 1:
            tk.messagebox.showinfo('提示', '修改成功')
            self.window.destroy()

    def button2(self, *args):
        a = json.loads(
            requests.post(config.orderUpdateStatusById, {'id': self.ids, 'status': 2}).content.decode('utf-8'))
        if int(a['code']) == 1:
            tk.messagebox.showinfo('提示', '修改成功')
            self.window.destroy()

    def button3(self, *args):
        a = json.loads(
            requests.post(config.orderUpdateStatusById, {'id': self.ids, 'status': 3}).content.decode('utf-8'))
        if int(a['code']) == 1:
            tk.messagebox.showinfo('提示', '修改成功')
            self.window.destroy()
