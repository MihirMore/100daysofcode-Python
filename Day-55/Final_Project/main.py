from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1><p>This is a paragraph</p>'


@app.route('/bye')
def say_bye():
    return "Bye"


@app.route('/<username>/<int:number>')
def greet(username, number):
    user_name = username.title()
    return f"Hello {user_name}!, you're {number} years old."


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
