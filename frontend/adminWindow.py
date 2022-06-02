import json
import pprint
import tkinter as tk

import requests

import config
import frontend.windowWidget


class AdminWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name, ids):
        super().__init__(width, height, name)

        self.offerInfo = None
        self.userId = ids.replace(' ', '')
        self.userAccount = None
        self.userInfo = None
        self.orderInfo = None

        self.accountLabelText = self.makeLabel((20, 20, 60, 40), text='账号：', color='lightblue')
        self.accountLabel = self.makeLabel((100, 20, 140, 40))
        self.userIdLabelText = self.makeLabel((20, 80, 60, 40), text='id：', color='lightblue')
        self.userIdLabel = self.makeLabel((100, 80, 140, 40))

        self.orderInfoLabelText = self.makeLabel((20, 140, 220, 40), text='订单统计')
        self.refreshButton = self.makeButton((260, 140, 100, 40), text='刷新', command=self.refreshButtonPress)

        self.orderInfoListbox = self.makeListbox((20, 200, 400, 680), self.orderInfoListboxPress)

        self.offerInfoLabelText = self.makeLabel((440, 140, 220, 40), text='供应商统计')
        self.refreshButton = self.makeButton((680, 140, 100, 40), text='添加供应商', command=self.insertOfferButtonPress)
        self.offerInfoListbox = self.makeListbox((440, 200, 400, 680), self.offerInfoListboxPress)

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
        pprint.pprint(self.offerInfo)

        self.offerInfoListbox.delete(0, tk.END)
        for i in self.offerInfo:
            s = f"id： {i['id']} 供应商： {i['name']}"
            self.offerInfoListbox.insert(0, s)

    def orderInfoListboxPress(self, event):
        ids = self.orderInfoListbox.curselection()
        if len(ids) > 0:
            ids = ids[0]
        else:
            return

        sAF = frontend.showAdminFlowerWindow.ShowAdminFlowerWindow(400, 300,
                                                                   '订单详情信息：{}'.format(self.orderInfo[ids]['id']),
                                                                   self.orderInfo[ids])

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
