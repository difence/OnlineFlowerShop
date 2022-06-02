import threading

import backend

work = threading.Thread(target=backend.controller.run)
work.start()
