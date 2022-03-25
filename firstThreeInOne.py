from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    # this shows the browser with version
    agent = request.headers.get('User-Agent')
    return "<h1> you are using %s" %agent

@app.route('/user-agent')
def user_agent():
    # this shows the browser with version
    agent = request.headers.get('User-Agent')
    return "<h1> you are using %s" %agent

@app.route('/me/<name>')
def user(name):
    return "<h1>Hello this is %s</h1>" % name


if __name__ == "__main__":
    app.run(debug=True)