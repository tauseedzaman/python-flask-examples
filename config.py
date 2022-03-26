from flask import Flask
app = Flask(__name__)
app.config['super_secret']="this is hacker loi"
@app.route('/') 
def index():
    return '<h1> Hello world </h1>'



if __name__ == '__main__':
    app.run(debug=True)