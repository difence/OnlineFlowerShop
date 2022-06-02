import threading

import backend
import frontend

work = threading.Thread(target=backend.controller.run)
work.start()

loginWindow = frontend.loginWindow.LoginWindow(400, 300, '登录界面')
