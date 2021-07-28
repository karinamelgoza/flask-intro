"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href='/hello'>Hello</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <label for='compliments'>Select a compliment:</label>
          <select name='compliments' id=compliments'>
            <option value='awesome'>awesome</option>
            <option value='terrific'>terrific</option>
            <option value='neato'>neato</option>
            <option value='ducky'>ducky</option>
          <input type="submit" value="Submit">
        </form>
        <form action="/superhero">
          What's your name? <input type="text" name="person">
          <label for='superhero'>Select a superhero:</label>
          <select name='superhero' id=superhero'>
            <option value='ironman'>Iron Man</option>
            <option value='wonderwoman'>Wonder Woman</option>
            <option value='batman'>Batman</option>
            <option value='mrs.incredible'>Mrs. Incredible</option>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get('compliments')

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route('/superhero')
def diss():
    player = request.args.get("person")

    superhero = request.args.get('superhero')

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Superhero</title>
      </head>
      <body>
        Hi, {player}! I think you're as incredible as {superhero}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
