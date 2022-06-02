import json
import tkinter as tk

import requests

import config
import frontend


class UserWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name, ids):
        super().__init__(width, height, name)

        self.flowerInfo = None
        self.userId = ids.replace(' ', '')
        self.userAccount = None
        self.userInfo = None
        self.orderInfo = None

        self.accountLabelText = self.makeLabel((20, 20, 60, 40), text='账号：', color='lightblue')
        self.accountLabel = self.makeLabel((100, 20, 140, 40))
        self.userIdLabelText = self.makeLabel((20, 80, 60, 40), text='id：', color='lightblue')
        self.userIdLabel = self.makeLabel((100, 80, 140, 40))

        self.refreshButton = self.makeButton((260, 80, 100, 40), text='刷新', command=self.refreshButtonPress)

        self.orderInfoLabelText = self.makeLabel((20, 140, 220, 40), text='我的订单')
        self.orderInfoListbox = self.makeListbox((20, 200, 220, 680), self.orderInfoListboxPress)

        self.flowerInfoLabelText = self.makeLabel((260, 140, 220, 40), text='花卉信息')
        self.flowerInfoListbox = self.makeListbox((260, 200, 300, 680), self.flowerInfoListboxPress)
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

        flowerInfoData = requests.post(config.flowerGetAll).content.decode('utf-8')
        flowerInfoData = json.loads(flowerInfoData)
        self.flowerInfo = flowerInfoData['data']

        self.flowerInfoListbox.delete(0, tk.END)
        for i in self.flowerInfo:
            s = f"花名： {i['name']} 颜色： {i['color']} 数量：{i['bucket']}"
            self.flowerInfoListbox.insert(0, s)

        self.orderInfo.reverse()
        self.flowerInfo.reverse()

    def orderInfoListboxPress(self, event):
        ids = self.orderInfoListbox.curselection()
        if len(ids) > 0:
            ids = ids[0]
        else:
            return

        sFw = frontend.showFlowerWindow.ShowFlowerWindow(400, 300, '花详细信息', self.orderInfo[ids]['id'])

    def flowerInfoListboxPress(self, event):
        ids = self.flowerInfoListbox.curselection()
        if len(ids) > 0:
            ids = ids[0]
        else:
            return

        sFW = frontend.buyFlowerWindow.UpdateFlowerWindow(400, 520, '购买花卉：{}'.format(self.flowerInfo[ids]['id']),
                                                          self.flowerInfo[ids], self.userId)

    def refreshButtonPress(self, *args):
        self.init()
