import flask
from plateloader import PlateLoader
import threading

app = flask.Flask(__name__, static_url_path="",static_folder="public")
serial_lock = threading.Lock()
plateloader = PlateLoader("COM4") # /dev/ttyUSB0 Real PlateLoader! # python -m serial.tools.miniterm

@app.get("/") # If URL has no other commands, like api/command, just spits out the index file text
def handle_naked_domain():
    return flask.redirect("/index.html")

@app.get("/api/<command>") # Primary command function. 
def api_command(command):
    with serial_lock:
        plateloader.connect()
        response = plateloader.send_command(command)
        plateloader.disconnect()
    return response

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=8080, use_reloader=False)
    finally:
        print("Disconnecting Plate Loader")
        plateloader.disconnect()
