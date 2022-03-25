from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    # this shows the browser with version
    agent = request.headers.get('User-Agent')
    return "<h1> you are using %s" %agent


if __name__ == "__main__":
    app.run(debug=True)