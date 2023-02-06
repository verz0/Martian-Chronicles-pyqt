import sys
from PySide6.QtWidgets import *

import APP.window_test as window_test
from APP.window_test import Window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_test = Window()
    window_test.show()
    sys.exit(app.exec())