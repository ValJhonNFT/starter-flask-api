from flask import Flask
import os
import threading
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

def test():
    print("Test")
    time.sleep(15)
 
update_thread = threading.Thread(target=test)
update_thread.start()
