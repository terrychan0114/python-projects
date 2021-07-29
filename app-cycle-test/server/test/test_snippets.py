from tkinter import *
import time
import json
from threading import *
import requests
import datetime

server_addr = 'http://localhost:8080/cycletest'
timestamp = datetime.datetime.now()
payload = {
            "cycle_status": True
}
r = requests.post(server_addr,json=payload)
print(r.status_code)