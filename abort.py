from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

app.route('user/<id>')
def get_user(id):
    # user = load_user(id)
    # if not True:
        # abort(404)
        # return '<h1> aborting</h1>'
    return id