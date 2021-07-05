from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/bye')
def say_bye():
    return "Bye"


@app.route('/<username>/<int:number>')
def greet(username, number):
    user_name = username.title()
    return f"Hello {user_name}!, you're {number} years old."


@app.route('/bye')
def bye():
    print("Bye!")


if __name__ == "__main__":
    app.run(debug=True)
