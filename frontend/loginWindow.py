import json
import tkinter.messagebox

import requests

import config
import frontend.windowWidget
import tool


class LoginWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name):
        super().__init__(width, height, name)

        self.accountLabel = self.makeLabel((20, 40, 100, 40), '账号：')
        self.passwordLabel = self.makeLabel((20, 120, 100, 40), '密码：')

        self.accountEntry = self.makeEntry((140, 40, 240, 40))
        self.passwordEntry = self.makeEntry((140, 120, 240, 40))
        self.passwordEntry.config(show="*")

        self.loginButton = self.makeButton((30, 220, 100, 40), '登录', self.loginButtonPress)
        self.registerButton = self.makeButton((150, 220, 100, 40), '注册', self.registerButtonPress)
        self.registerButton = self.makeButton((270, 220, 100, 40), '忘记密码', self.forgetButtonPress)

        self.window.mainloop()

    def loginButtonPress(self, *args):
        res = json.loads(requests.post(config.userLoginUrl, data=self.getAccountAndPassword()).content)
        if res['code'] == 1:
            tkinter.messagebox.showinfo('登录', res['msg'])
            name = self.accountEntry.get()
            self.window.destroy()
            auth = res['data']['auth']
            if auth == 0:
                mw = frontend.mainWindow.MainWindow(1440, 900, '杂货商de网上花店', res['data']['id'])
            else:
                aw = frontend.adminWindow.AdminWindow(1440, 900, '后台管理员', res['data']['id'])
        else:
            tkinter.messagebox.showwarning('登录', res['msg'])

    def registerButtonPress(self, *args):
        rw = frontend.registerWindow.RegisterWindow(400, 320, '注册界面')
        pass

    def getAccountAndPassword(self):
        acc = self.accountEntry.get()
        pas = self.passwordEntry.get()
        return {'account': acc,
                'password': tool.fun.encodingPassowrd(pas)}

    def forgetButtonPress(self, *args):
        fw = frontend.forgetWindow.ForgetWindow(400, 300, '忘记密码')
        pass
