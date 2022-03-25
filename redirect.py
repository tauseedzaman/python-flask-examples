from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> <a href='/there'>Here</a></h1>"

@app.route("/there")
def there():
    return "<h1>welcome to there!</h1>"

if __name__ == "__main__":
    app.run(debug=True)