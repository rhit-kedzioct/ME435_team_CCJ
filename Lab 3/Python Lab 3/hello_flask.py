import flask
app = flask.Flask(__name__)

@app.route("/")
def hello_route():
    return "Hello, World!"


if __name__ == "__main__":
    print("Running flask")
    app.run(host="0.0.0.0", port=8080, debug = True)