import sys
import requests
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit

class MarsRoverWindow(QMainWindow):
    
    def fetchimage(self):
        earth_date = self.earth_date_input.text()
        response = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={earth_date}&api_key=UVgW4xMfAabM1yCPc70bmGlgXjr0k3EKDNGR1Oe0")
        image_data = response.json()["photos"][0]["img_src"]
        image = QPixmap()
        image.loadFromData(requests.get(image_data).content)
        self.label.setPixmap(image)
        self.label.setAlignment(Qt.AlignCenter)
        
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mars Rover Images")
        self.setGeometry(100, 100, 500, 400)
        self.label = QLabel()
        self.earth_date_input = QLineEdit()
        self.earth_date_input.setPlaceholderText("Enter date (YYYY-M-D)")
        self.fetch_button = QPushButton("Fetch Image")
        self.fetch_button.clicked.connect(self.fetchimage)

        layout = QVBoxLayout()
        layout.addWidget(self.earth_date_input)
        layout.addWidget(self.label)
        layout.addWidget(self.fetch_button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.earth_date_input.setStyleSheet("padding: 10px; border: 2px solid gray; border-radius: 5px;")
        self.fetch_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px 20px; border-radius: 5px;")
        self.label.setStyleSheet("background-color: white; padding: 20px;")
        self.fetch_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px 20px; border-radius: 5px;")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MarsRoverWindow()
    window.show()
    sys.exit(app.exec_())
