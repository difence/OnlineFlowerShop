import json
import tkinter as tk
import tkinter.messagebox

import requests

import config
import frontend.windowWidget
import tool


class ForgetWindow(frontend.windowWidget.WindowWidget):
    def __init__(self, width, height, name):
        super().__init__(width, height, name)

        self.accountLabel = self.makeLabel((20, 40, 100, 40), '账号：')
        self.passwordLabel = self.makeLabel((20, 120, 100, 40), '密码：')

        self.accountEntry = self.makeEntry((140, 40, 240, 40))
        self.passwordEntry = self.makeEntry((140, 120, 240, 40))

        self.forgetButton = self.makeButton((150, 220, 100, 40), '修改密码', self.forgetButtonPress)

        self.window.mainloop()

    def forgetButtonPress(self, *args):
        acc = self.accountEntry.get()
        pas = self.passwordEntry.get()

        res = requests.post(config.userForgetUrl,
                            data={'account': acc,
                                  'password': tool.fun.encodingPassowrd(pas)}).content
        res = json.loads(res)

        if res['code'] == 0:
            tk.messagebox.showwarning('找回密码', res['msg'])
        else:
            tk.messagebox.showinfo('找回密码', res['msg'])
            self.window.destroy()
