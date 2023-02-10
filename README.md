# Martian-Chronicles-pyqt

## Introduction 

The Mars Rover Image Retriever is a simple desktop application that allows users to view images taken by NASA's Mars Rovers. The app retrieves images using the Mars Rover Photos API, which provides information about the photos taken by NASA's Mars Rovers.

## Features

* Simple, easy-to-use interface for searching and viewing images
* Option to choose between the Mars Rovers (Curiosity, Opportunity, and Spirit)
* Option to filter images by camera and by earth-date 
* Display of full-size images
* Email sending functionality
* Pop up messages when errors show up and a status bar to let the user know that images are downloading

![Screenshot from 2023-02-11 01-46-32](https://user-images.githubusercontent.com/115163471/218125406-7f496200-9d11-4a2d-9029-169cb41b98b9.png)

## How to Use

**1.** Select the Mars Rover you would like to view images from.

**2.** (Optional) Filter the images by camera or by earth-date.

**3.** Click the "Fetch Images" button to retrieve a selection of images.

**4.** Navigate through the images using the next and previous buttons

**5.** (Optional) Click the "Mail" button to send the image on screen to somebody's email

![Screenshot from 2023-02-11 01-47-01](https://user-images.githubusercontent.com/115163471/218126223-b5c985ef-9509-43bf-96f4-4b422a3c2295.png)
![Screenshot from 2023-02-11 02-16-53](https://user-images.githubusercontent.com/115163471/218127722-27a7f175-7680-4cf2-b2c7-39d0b3254d19.png)

## Technical Details

The Mars Rover Image Retriever is built with Python and uses the Requests library to make API requests. The GUI and image display is implemented by using the PYQT library. The email sending functionality is made with the help of ezgmail python module. The user can send email to multiple recipients by entering their emails separated by a comma. An "images" directory will be created where the images will be downloaded when the fetch button is clicked.

## Conclusion

The Mars Rover Image Retriever is a fun and educational tool that provides easy access to the wealth of images captured by NASA's Mars Rovers. Whether you're a space enthusiast or just curious about the Red Planet, this app is a great way to explore the Martian landscape and learn more about Mars.

