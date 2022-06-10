import json
import tkinter as tk

import matplotlib.pyplot as plt
import requests

import config
import frontend.windowWidget


class AdminWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name, ids):
        super().__init__(width, height, name)

        self.flowerInfo = None
        self.offerInfo = None
        self.userId = ids.replace(' ', '')
        self.userAccount = None
        self.userInfo = None
        self.orderInfo = None

        self.accountLabelText = self.makeLabel((20, 20, 60, 40), text='账号：', color='lightblue')
        self.accountLabel = self.makeLabel((100, 20, 140, 40))
        self.userIdLabelText = self.makeLabel((20, 80, 60, 40), text='id：', color='lightblue')
        self.userIdLabel = self.makeLabel((100, 80, 140, 40))

        self.showButton = self.makeButton((260, 80, 100, 40), text='报表', command=self.show)

        self.orderInfoLabelText = self.makeLabel((20, 140, 220, 40), text='订单统计')
        self.refreshButton = self.makeButton((260, 140, 100, 40), text='刷新', command=self.refreshButtonPress)

        self.orderInfoListbox = self.makeListbox((20, 200, 400, 680), self.orderInfoListboxPress)

        self.offerInfoLabelText = self.makeLabel((440, 140, 220, 40), text='供应商统计')
        self.offerAddButton = self.makeButton((680, 140, 100, 40), text='添加供应商', command=self.insertOfferButtonPress)
        self.offerInfoListbox = self.makeListbox((440, 200, 400, 680), self.offerInfoListboxPress)

        self.flowerInfoLabelText = self.makeLabel((860, 140, 220, 40), text='花卉信息')
        self.flowerAddButton = self.makeButton((1100, 140, 100, 40), text='添加花卉', command=self.insertFlowerButtonPress)
        self.flowerInfoListbox = self.makeListbox((860, 200, 320, 680), self.flowerInfoListboxPress)

        self.init()
        self.window.mainloop()

    def init(self):
        userInfoData = requests.post(config.userGetByIdUrl, data={'id': self.userId}).content
        userInfoData = json.loads(userInfoData)

        self.userInfo = userInfoData['data']
        self.userAccount = self.userInfo['account'].replace(' ', '')
        self.accountLabel.configure(text=self.userAccount)
        self.userIdLabel.configure(text=self.userId)

        orderInfoData = requests.post(config.orderGetUserOrderById).content
        orderInfoData = json.loads(orderInfoData)
        self.orderInfo = orderInfoData['data']
        self.orderInfoListbox.delete(0, tk.END)
        statusDict = {0: '已完成', 1: '配送中', 2: '工单', 3: '已退款',
                      None: '异常'}
        for i in self.orderInfo:
            s = f"名字： {i['bucket_id']['name']} 数量：{i['number']} 价格：{i['bucket_id']['price']} 状态：{statusDict[i['status']]} 购买者：{i['user_id']['account']}"
            self.orderInfoListbox.insert(0, s)

        offerInfoData = requests.post(config.offerGetAll).content.decode('utf-8')
        offerInfoData = json.loads(offerInfoData)
        self.offerInfo = offerInfoData['data']

        self.offerInfoListbox.delete(0, tk.END)
        for i in self.offerInfo:
            s = f"id： {i['id']} 供应商： {i['name']}"
            self.offerInfoListbox.insert(0, s)

        flowerInfoData = requests.post(config.flowerGetAll).content.decode('utf-8')
        flowerInfoData = json.loads(flowerInfoData)
        self.flowerInfo = flowerInfoData['data']

        self.flowerInfoListbox.delete(0, tk.END)
        for i in self.flowerInfo:
            s = f"花名： {i['name']} 颜色： {i['color']} 数量：{i['bucket']}"
            self.flowerInfoListbox.insert(0, s)

        self.orderInfo.reverse()
        self.flowerInfo.reverse()
        self.offerInfo.reverse()

    def orderInfoListboxPress(self, event):
        ids = self.orderInfoListbox.curselection()
        if len(ids) > 0:
            ids = ids[0]
        else:
            return

        sAF = frontend.showAdminFlowerWindow.ShowAdminFlowerWindow(400, 300,
                                                                   '订单详情信息：{}'.format(self.orderInfo[ids]['id']),
                                                                   self.orderInfo[ids], self.userId)

    def offerInfoListboxPress(self, event):
        ids = self.offerInfoListbox.curselection()
        if len(ids) > 0:
            ids = ids[0]
        else:
            return

        sOW = frontend.showOfferWindow.ShowOfferWindow(400, 300, '供应商详情信息：{}'.format(self.offerInfo[ids]['id']),
                                                       self.offerInfo[ids])

    def insertOfferButtonPress(self, *args):
        aOW = frontend.addOfferWindow.AddOfferWindow(400, 300, '添加供应商')

    def refreshButtonPress(self, *args):
        self.init()

    def insertFlowerButtonPress(self, *args):

        aFW = frontend.addFlowerWindow.AddFlowerWindow(400, 620, '添加花卉', self.userId, self.offerInfo)
        pass

    def flowerInfoListboxPress(self, event):
        ids = self.flowerInfoListbox.curselection()
        if len(ids) > 0:
            ids = ids[0]
        else:
            return

        sOW = frontend.updateFlowerWindow.UpdateFlowerWindow(400, 620, '修改花卉：{}'.format(self.flowerInfo[ids]['id']),
                                                             self.flowerInfo[ids], self.userId)

    def show(self, *args):
        d1 = self.offerInfo
        data = [[], []]
        for i in d1:
            if i['name'] not in data[1]:
                data[1].append(i['name'])
                data[0].append(0)
            data[0][data[1].index(i['name'])] += 1

        plt.pie(data[0], labels=data[1])
        plt.show()

        d1 = self.orderInfo
        data = [[], []]
        pr = []
        for i in d1:
            if i['bucket_id']['name'] not in data[1]:
                data[1].append(i['bucket_id']['name'])
                data[0].append(0)
            data[0][data[1].index(i['bucket_id']['name'])] += 1
            pr.append(float(i['bucket_id']['price'] * i['number']))

        plt.pie(data[0], labels=data[1])
        plt.show()

        plt.plot(pr, label='购买价格')
        plt.legend()
        plt.show()
