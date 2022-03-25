from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/me/<name>')
def user(name):
    return "<h1>Hello this is %s</h1>" % name

if __name__ == "__main__":
    app.run(debug=True)