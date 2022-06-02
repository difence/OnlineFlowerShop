import json
import pprint

import requests

import config
import frontend


class ShowAdminFlowerWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name, data):
        super().__init__(width, height, name)
        pprint.pprint(data)
        self.ids = data['id']
        statusDict = {0: '已完成', 1: '配送中', 2: '工单', 3: '已退款',
                      None: '异常'}
        self.data = json.loads(requests.post(config.orderGetOrderById, data={'id': self.ids}).content.decode('utf-8'))[
            'data']
        self.makeLabel((20, 20, 120, 40), '名字：{}'.format(data['bucket_id']['name']))
        self.makeLabel((160, 20, 120, 40), '花色：{}'.format(data['bucket_id']['color']))

        self.flowerLabel = self.makeLabel((300, 20, 80, 80))

        self.makeLabel((20, 80, 120, 40), '数量：{}'.format(data['number']))
        self.makeLabel((160, 80, 120, 40), '价格：{}'.format(data['bucket_id']['price']))

        self.makeLabel((20, 140, 360, 40), '状态：{}'.format(statusDict[self.data['status']]))
        self.makeLabel((20, 200, 360, 40), '购买时间：{}'.format(data['create_date']))

        self.makeButton((180, 260, 100, 40), '处理工单', self.orderStatusButtonPress)

        self.window.mainloop()

    def orderStatusButtonPress(self, *args):
        sow = frontend.solveOrderWindow.SolveOrderWindow(400, 300, '处理订单', self.ids)
        self.window.destroy()
        pass
