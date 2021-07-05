from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/bye')
def say_bye():
    return "Bye"


@app.route('/<username>/<path:number>')
def greet(username, number):
    user_name = username.title()
    return f"Hello {user_name}!, you're {number} years old."


if __name__ == "__main__":
    app.run(debug=True)
