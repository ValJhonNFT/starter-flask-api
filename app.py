from flask import Flask
import os
import threading

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

def test():
    print("Test")
 
update_thread = threading.Thread(target=test)
update_thread.start()
