from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/elephanthumanprediction")
def elephantHumanPred():
    return render_template("elephanthumanprediction.html")


if __name__ == "__main__":
    app.run()