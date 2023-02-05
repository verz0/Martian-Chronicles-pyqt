import requests
import json
from PIL import Image
from urllib.request import urlopen
import webbrowser

params = {"earth_date":"2016-10-17", "api_key":"UVgW4xMfAabM1yCPc70bmGlgXjr0k3EKDNGR1Oe0"}
f = r"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?"
data = requests.get(f, params = params)

    

