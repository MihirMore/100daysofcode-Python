from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/bye')
def say_bye():
    return "Bye"


@app.route('/username/<name>')
def greet(name):
    user_name = name.title()
    return f"Hello {user_name}!"


if __name__ == "__main__":
    app.run()
