from flask import Flask, flash
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is the proxy pool"


if __name__ == "__main__":
    app.run()