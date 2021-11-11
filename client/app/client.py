# Does a GET request on http://localhost:5000 to get data from server
# Basic python client server that does a GET request on http://localhost:5000
# Listens on port 5000
# Returns message received from the server
from flask import Flask
import requests
import urllib3

client = Flask(__name__)

def communicate():
    response = requests.get('http://localhost:5000')
    return str(response.text)

print(communicate())