import json
import os
import tkinter as tk
import tkinter.messagebox

import requests

import config
import frontend
import tool


class ShowFlowerWindow(frontend.windowTopLevel.WindowTopLevel):
    def __init__(self, width, height, name, data):
        super().__init__(width, height, name)
        self.pic = None
        self.ids = data
        self.data = json.loads(requests.post(config.orderGetOrderById, data={'id': self.ids}).content.decode('utf-8'))[
            'data']
        statusDict = {0: '订单已完成', 1: '订单配送中，请稍后', 2: '订单提交工单，卖家正在处理', 3: '已退款，给您的体验带来不便请理解',
                      None: '订单异常，请联系管理员处理'}
        self.makeLabel((20, 20, 120, 40), '名字：{}'.format(self.data['bucket_id']['name']))
        self.makeLabel((160, 20, 120, 40), '花色：{}'.format(self.data['bucket_id']['color']))

        self.flowerLabel = self.makeLabel((300, 20, 80, 80), command=self.flowerLabelPress)

        self.makeLabel((20, 80, 120, 40), '数量：{}'.format(self.data['number']))
        self.makeLabel((160, 80, 120, 40), '价格：{}'.format(self.data['bucket_id']['price']))

        self.makeLabel((20, 140, 360, 40), '状态：{}'.format(statusDict[self.data['status']]))
        self.makeLabel((20, 200, 360, 40), '购买时间：{}'.format(self.data['create_date']))

        self.makeButton((180, 260, 100, 40), '提交工单', self.orderStatusButtonPress)

        self.initPic()
        self.window.mainloop()

    def orderStatusButtonPress(self, *args):
        a = json.loads(
            requests.post(config.orderUpdateStatusById, {'id': self.ids, 'status': 2}).content.decode('utf-8'))
        if int(a['code']) == 1:
            tk.messagebox.showinfo('提示', '提交工单成功')

    def flowerLabelPress(self, *args):
        ids = self.ids
        picId = self.data['bucket_id']['attachment_ids'][0]
        res = requests.post(config.fileDownloadById, data={'id': picId}).content.decode('utf-8')
        res = json.loads(res)['data']['url']

    def initPic(self):
        try:
            picId = self.data['bucket_id']['attachment_ids']
            res = requests.post(config.fileDownloadById, data={'id': picId}).content.decode('utf-8')
            res = json.loads(res)['data']['url']
            pic = requests.get(res, data={'id': picId}).content
            with open('./temp.jpg', 'bw') as f:
                f.write(pic)
            self.pic = tool.fun.pic2TKpic(f'./temp.jpg', (80, 80))
            self.flowerLabel.configure(image=self.pic)
            if os.path.exists(f'./temp.jpg'):
                os.remove(f'./temp.jpg')
        except:
            pass
