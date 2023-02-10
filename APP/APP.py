import sys
import requests
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QComboBox, QHBoxLayout, QDateEdit, QMessageBox
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import ezgmail




class MarsRoverWindow(QMainWindow):

    def fetchimages(self):
        earth_date = self.earth_date_input.text()
        rover = self.rover_input.currentText()
        camera = self.camera_input.currentText()
        response = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?earth_date={earth_date}&camera={camera}&api_key=GOhUrbNjUaK2s9AQbvQKT8ETBKfQRPfjKIQA0TFi")
        try:
            image_urls = [photo["img_src"] for photo in response.json()["photos"][:10]]
        except KeyError:
            QMessageBox.warning(self,"error", "failed to fetch images(KEY ERROR), try later :( ")
            return 
        self.image_urls = image_urls
        self.current_index = 0
    
        if not os.path.exists("images"):
            os.makedirs("images")
            
        self.statusBar().showMessage("Downloading images...", 2000)
        QApplication.processEvents()
        for i, image_url in enumerate(image_urls):
            image_data = requests.get(image_url).content
            with open(f"images/image_{i}.jpg", "wb") as f:
                f.write(image_data)
                     
        self.statusBar().showMessage("Images loaded successfully!", 2000)
        self.display_image()
        
    
    def display_image(self):
        if not self.image_urls:
            return
        image = QPixmap(f"images/image_{self.current_index}.jpg")
        self.label.setPixmap(image)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setPixmap(image.scaled(self.label.size(), Qt.KeepAspectRatio))
       


    def next_image(self):
        if self.current_index < len(self.image_urls) - 1:
            self.current_index += 1
            self.display_image()
    
    def prev_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_image()
    
    def open_email_window(self):
        self.email_window = QMainWindow()
        self.email_window.setWindowTitle("Email")
        self.email_window.setFixedSize(500, 500)
        self.email_window.setStyleSheet("background-color: black;")

        email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        subject_label = QLabel("Subject:")
        self.subject_input = QLineEdit()
        body_label = QLabel("Body:")
        self.body_input = QLineEdit()
        send_button = QPushButton("Send")
        send_button.clicked.connect(self.mail)

        email_layout = QHBoxLayout()
        email_layout.addWidget(email_label)
        email_layout.addWidget(self.email_input)
        subject_layout = QHBoxLayout()
        subject_layout.addWidget(subject_label)
        subject_layout.addWidget(self.subject_input)
        body_layout = QHBoxLayout()
        body_layout.addWidget(body_label)
        body_layout.addWidget(self.body_input)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(send_button)
        main_layout = QVBoxLayout()
        main_layout.addLayout(email_layout)
        main_layout.addLayout(subject_layout)
        main_layout.addLayout(body_layout)
        main_layout.addLayout(button_layout)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.email_window.setCentralWidget(central_widget)
        self.email_input.setStyleSheet("padding: 10px; border: 2px solid red; border-radius: 5px;")
        self.subject_input.setStyleSheet("padding: 10px; border: 2px solid red; border-radius: 5px;")
        self.body_input.setStyleSheet("padding: 10px; border: 2px solid red; border-radius: 5px;")

        self.email_window.show()
            
    def mail(self):
            email_list = self.email_input.text().split(',')
            for email in email_list:
                ezgmail.send(email, self.subject_input.text(), self.body_input.text(), attachments=f"images/image_{self.current_index}.jpg")
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Email sent successfully!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            
    def __init__(self):
        super().__init__()
        
        self.statusBar().showMessage("Ready")
        self.setWindowTitle("Mars Rover Images")
        self.setFixedSize(900,1000)
        self.label = QLabel()
        self.earth_date_input = QDateEdit()
        self.earth_date_input.setDisplayFormat("yyyy-MM-dd")
        self.rover_input = QComboBox()
        self.rover_input.addItems(["Curiosity", "Spirit", "Opportunity"])
        self.camera_input = QComboBox()
        self.camera_input.addItems(["FHAZ", "RHAZ", "NAVCAM"])
        self.fetch_button = QPushButton("Fetch Images")
        self.fetch_button.clicked.connect(self.fetchimages)
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_image)
        self.prev_button = QPushButton("Previous")
        self.prev_button.clicked.connect(self.prev_image)
        self.email_button = QPushButton("Mail")
        self.email_button.clicked.connect(self.open_email_window)
        self.pixmap=QPixmap(f'space.jpg')  
        self.label.setPixmap(self.pixmap)
        
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.prev_button)
        hlayout.addWidget(self.next_button)
        
        layout = QVBoxLayout()
        layout.addWidget(self.earth_date_input)
        layout.addWidget(self.rover_input)
        layout.addWidget(self.camera_input)
        layout.addWidget(self.label)
        layout.addWidget(self.fetch_button)
        layout.addLayout(hlayout)
        layout.addWidget(self.email_button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.earth_date_input.setStyleSheet("padding: 10px; border: 5px solid black; border-radius: 10px;")
        self.rover_input.setStyleSheet("padding: 10px; border: 5px solid black; border-radius: 10px;")
        self.camera_input.setStyleSheet("padding: 10px; border: 5px solid black; border-radius: 10px;")
        self.fetch_button.setStyleSheet("background-color: #000000; color: white; padding: 10px 20px; border-radius: 15px;")
        self.label.setStyleSheet("background-image: space.jpg; padding: 20px;")
        self.next_button.setStyleSheet("background-color: #FFD700; color: black; padding: 10px 20px; border-radius: 15px;")
        self.prev_button.setStyleSheet("background-color: #FFD700; color: black; padding: 10px 20px; border-radius: 15px;")
        self.email_button.setStyleSheet("background-color: #12E18E ; color: black; padding: 10px 20px; border-radius: 15px;" )
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MarsRoverWindow()
    window.show()
    sys.exit(app.exec_())

