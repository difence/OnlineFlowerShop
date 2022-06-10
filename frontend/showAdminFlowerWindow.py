import json
import os.path
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

import cv2
import requests

import config
import frontend.windowTopLevel
import tool.fun


class ShowAdminFlowerWindow(frontend.windowTopLevel.WindowTopLevel):
    def __init__(self, width, height, name, data, userId):
        super().__init__(width, height, name)
        self.pic = None
        self.ids = data['id']
        self.userId = userId
        statusDict = {0: '已完成', 1: '配送中', 2: '工单', 3: '已退款',
                      None: '异常'}
        self.data = json.loads(requests.post(config.orderGetOrderById, data={'id': self.ids}).content.decode('utf-8'))[
            'data']
        self.makeLabel((20, 20, 120, 40), '名字：{}'.format(data['bucket_id']['name']))
        self.makeLabel((160, 20, 120, 40), '花色：{}'.format(data['bucket_id']['color']))

        self.flowerLabel = self.makeLabel((300, 20, 80, 80), command=self.flowerLabelPress)

        self.makeLabel((20, 80, 120, 40), '数量：{}'.format(data['number']))
        self.makeLabel((160, 80, 120, 40), '价格：{}'.format(data['bucket_id']['price']))

        self.makeLabel((20, 140, 360, 40), '状态：{}'.format(statusDict[self.data['status']]))
        self.makeLabel((20, 200, 360, 40), '购买时间：{}'.format(data['create_date']))

        self.makeButton((180, 260, 100, 40), '处理工单', self.orderStatusButtonPress)

        self.initPic()

        self.window.mainloop()

    def orderStatusButtonPress(self, *args):
        sow = frontend.solveOrderWindow.SolveOrderWindow(400, 300, '处理订单', self.ids)
        self.window.destroy()
        pass

    def flowerLabelPress(self, *args):
        path = tk.filedialog.askopenfilename()
        fname = os.path.split(path)[1]
        name, type = os.path.splitext(fname)
        res = requests.post(config.fileUpload, data={'update_id': self.userId,
                                                     'name': name,
                                                     'type': type[1:],
                                                     'tname': fname}).content.decode('utf-8')
        res = json.loads(res)
        resUrl = res['data']['url']
        resId = res['data']['id']

        img = cv2.imread(path)
        img = cv2.resize(img, (80, 80))
        cv2.imwrite(f'./{name}.jpg', img)
        with open(f'./{name}.jpg', 'rb') as f:
            z = requests.put(resUrl, f)
            if str(z.status_code) == '200':
                tk.messagebox.showinfo('修改', '图片修改成功')
        self.pic = tool.fun.pic2TKpic(f'./{name}.jpg', (80, 80))
        self.flowerLabel.configure(image=self.pic)
        requests.post(config.flowerUpdateAttsById, data={'id': self.data['bucket_id']['id'], 'attachment_ids': resId})
        if os.path.exists(f'./{name}.jpg'):
            os.remove(f'./{name}.jpg')

    def initPic(self):
        try:
            picId = self.data['bucket_id']['attachment_ids']
            res = requests.post(config.fileDownloadById, data={'id': picId}).content.decode('utf-8')
            res = json.loads(res)['data']['url']
            pic = requests.get(res, data={'id': picId}).content
            with open('temp.jpg', 'bw') as f:
                f.write(pic)
            self.pic = tool.fun.pic2TKpic(f'./temp.jpg', (80, 80))
            self.flowerLabel.configure(image=self.pic)
            if os.path.exists(f'./temp.jpg'):
                os.remove(f'./temp.jpg')
        except:
            pass
