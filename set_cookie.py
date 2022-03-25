from flask import Flask, make_response

app = Flask(__name__)
@app.route('/')
def index():
    response = make_response("<h1> Hello! there is coookie here do you wana eat!")
    response.set_cookie("hacker loi","tauseedzaman")
    return response
if __name__=="__main__":
    app.run(debug=True)