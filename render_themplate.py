from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user.html",name=name)

@app.route("/list")
def list():
    list = [
        'ali',
        'khan',
        'osama',
        'tauseed',
        'zaman',
        'hegab',
        'jabran',
    ]
    return render_template("list.html",list=list)

if __name__=="__main__":
    app.run(debug=True)