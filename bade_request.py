from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # you con pass the second perammeter as a responce code in this case 404 with mean not found
    return "<h1>Bade Request 404 </h1>",404   

if __name__=="__main__":
    app.run(debug=True)