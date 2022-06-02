import json
import tkinter as tk

import requests

import config
import frontend


class MainWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name, ids):
        super().__init__(width, height, name)

        self.userId = ids.replace(' ', '')
        self.userAccount = None
        self.userInfo = None
        self.orderInfo = None

        self.accountLabelText = self.makeLabel((20, 20, 60, 40), text='账号：', color='lightblue')
        self.accountLabel = self.makeLabel((100, 20, 140, 40))
        self.userIdLabelText = self.makeLabel((20, 80, 60, 40), text='id：', color='lightblue')
        self.userIdLabel = self.makeLabel((100, 80, 140, 40))

        self.orderInfoLabelText = self.makeLabel((20, 140, 220, 40), text='我的订单')
        self.orderInfoListbox = self.makeListbox((20, 200, 220, 680), self.orderInfoListboxPress)
        self.refreshButton = self.makeButton((260, 140, 100, 40), text='刷新', command=self.refreshButtonPress)
        self.init()
        self.window.mainloop()

    def init(self):
        userInfoData = requests.post(config.userGetByIdUrl, data={'id': self.userId}).content
        userInfoData = json.loads(userInfoData)

        self.userInfo = userInfoData['data']
        self.userAccount = self.userInfo['account'].replace(' ', '')
        self.accountLabel.configure(text=self.userAccount)
        self.userIdLabel.configure(text=self.userId)

        orderInfoData = requests.post(config.orderGetUserOrderById, data={'user_id': self.userId}).content
        orderInfoData = json.loads(orderInfoData)
        self.orderInfo = orderInfoData['data']
        self.orderInfoListbox.delete(0, tk.END)

        for i in self.orderInfo:
            s = f"名字： {i['bucket_id']['name']} 数量：{i['number']} 价格：{i['bucket_id']['price']}"
            self.orderInfoListbox.insert(0, s)

    def orderInfoListboxPress(self, event):
        ids = self.orderInfoListbox.curselection()
        if len(ids) > 0:
            ids = ids[0]
        else:
            return

        sFw = frontend.showFlowerWindow.MainWindow(400, 300, '花详细信息', self.orderInfo[ids]['id'])

    def refreshButtonPress(self, *args):
        self.init()
