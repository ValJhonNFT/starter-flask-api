from flask import Flask
import os
import threading
import time

global test

app = Flask(__name__)

# Global variables
counter = 0
thread_running = False

def test():
    global counter, thread_running
    while True:
        counter += 1
        time.sleep(5)  # Adjust sleep time as needed
        print('Thread is running...')

@app.route('/')
def hello_world():
    global thread_running
    if update_thread.is_alive():
        thread_running = True
    else:
        thread_running = False
    return jsonify({'thread_running': thread_running, 'counter': counter})

update_thread = threading.Thread(target=test)
update_thread.start()
