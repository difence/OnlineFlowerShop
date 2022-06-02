import json
import pprint
import tkinter as tk
import tkinter.messagebox

import requests

import config
import frontend


class ShowFlowerWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name, data):
        super().__init__(width, height, name)
        pprint.pprint(data)
        self.ids = data['id']
        self.data = json.loads(requests.post(config.orderGetOrderById, data={'id': self.ids}).content.decode('utf-8'))[
            'data']
        statusDict = {0: '订单已完成', 1: '订单配送中，请稍后', 2: '订单提交工单，卖家正在处理', 3: '已退款，给您的体验带来不便请理解',
                      None: '订单异常，请联系管理员处理'}
        self.makeLabel((20, 20, 120, 40), '名字：{}'.format(data['bucket_id']['name']))
        self.makeLabel((160, 20, 120, 40), '花色：{}'.format(data['bucket_id']['color']))

        self.flowerLabel = self.makeLabel((300, 20, 80, 80))

        self.makeLabel((20, 80, 120, 40), '数量：{}'.format(data['number']))
        self.makeLabel((160, 80, 120, 40), '价格：{}'.format(data['bucket_id']['price']))

        self.makeLabel((20, 140, 360, 40), '状态：{}'.format(statusDict[self.data['status']]))
        self.makeLabel((20, 200, 360, 40), '购买时间：{}'.format(data['create_date']))

        self.makeButton((180, 260, 100, 40), '提交工单', self.orderStatusButtonPress)

        self.window.mainloop()

    def orderStatusButtonPress(self, *args):
        a = json.loads(
            requests.post(config.orderUpdateStatusById, {'id': self.ids, 'status': 2}).content.decode('utf-8'))
        if int(a['code']) == 1:
            tk.messagebox.showinfo('提示', '提交工单成功')
