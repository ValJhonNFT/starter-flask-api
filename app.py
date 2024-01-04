from flask import Flask
import os
import threading
import time

global test

app = Flask(__name__)

# Global variable to track the thread status
thread_running = False

def test():
    global thread_running
    print("Test")
    while True:
        time.sleep(5)
        print("Thread is running...")


@app.route('/')
def hello_world():
    global thread_running
    if update_thread.is_alive():
        thread_running = True
    else:
        thread_running = False
    return f'Thread is running: {thread_running}'


update_thread = threading.Thread(target=test)
update_thread.start()
