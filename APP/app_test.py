import sys
from PySide6.QtWidgets import *

import window
from window import Window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())