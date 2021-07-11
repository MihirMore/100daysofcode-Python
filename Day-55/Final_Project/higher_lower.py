from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
        "<img src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)