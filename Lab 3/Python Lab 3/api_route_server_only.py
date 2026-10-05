import flask
app = flask.Flask(__name__)

@app.get("/api/hello/<name>")
def hello_name(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("Running flask")
    app.run(host="0.0.0.0", port=8080, debug = True)


