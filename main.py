import psutil
import subprocess
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    running = False
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if 'python' in proc.info['name'] and 'start' in proc.info['cmdline']: 
            running = True
            break
    if running:
        return 'Bot is Running...'
    else:
        # Start the bot using the bash startup script
        subprocess.Popen(['bash', 'start'])
        return 'Bot is Now Alive'

@app.route('/health')
def health_check():
    return "PragyanBot is alive", 200

@app.route('/dev', methods=['POST'])
def dev_command():
    return "@pragyan is a developer", 200

if __name__ == '__main__':
    # Start Flask app in the main thread
    app.run(host="0.0.0.0", port=7860, debug=True)
