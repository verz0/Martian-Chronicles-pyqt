import random
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Images from mars rover"
        self.left = 50
        self.top = 50
        self.width = 500
        self.height = 400
        self.createUI()
    def createUI(self):
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.setWindowTitle(self.title)
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        
        
    