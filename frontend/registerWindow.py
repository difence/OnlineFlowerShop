import json
import tkinter as tk
import tkinter.messagebox

import requests

import config
import frontend.windowWidget
import tool.fun


class RegisterWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name):
        super().__init__(width, height, name)

        self.accountLabel = self.makeLabel((20, 20, 100, 40), '账号：')
        self.passwordLabel = self.makeLabel((20, 80, 100, 40), '密码：')
        self.telLabel = self.makeLabel((20, 140, 100, 40), '手机：')
        self.birthLabel = self.makeLabel((20, 200, 100, 40), '生日：')

        self.accountEntry = self.makeEntry((140, 20, 240, 40))
        self.passwordEntry = self.makeEntry((140, 80, 240, 40))
        self.telEntry = self.makeEntry((140, 140, 240, 40))
        self.birthEntry = self.makeEntry((140, 200, 240, 40))

        self.registerButton = self.makeButton((150, 260, 100, 40), '注册', self.registerButtonPress)

        self.window.mainloop()

    def registerButtonPress(self, *args):
        acc = self.accountEntry.get()
        pas = self.passwordEntry.get()
        tel = self.telEntry.get()
        bir = self.birthEntry.get()

        res = requests.post(config.userRegisterUrl,
                            data={'account': acc,
                                  'password': tool.fun.encodingPassowrd(pas),
                                  'tel': tel,
                                  'birth': bir}).content
        res = json.loads(res)
        if res['code'] == 0:
            tk.messagebox.showwarning('注册', res['msg'])
        else:
            tk.messagebox.showinfo('注册', res['msg'])
            self.window.destroy()

        pass
