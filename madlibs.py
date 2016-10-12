from random import choice, sample, randint

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']
MADLIBTEMPLATES = ['madlib.html', 'madlib2.html']

@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = sample(AWESOMENESS, randint(1, len(AWESOMENESS)))

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def play_game():
    """Play game."""
    # player = request.args.get("person")
    game_response = request.args.get("response")

    if game_response == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    """Make a madlib."""
    # player = request.args.get("person")
    name = request.args.get("name")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    adject2 = request.args.getlist("adject2")
    madlib_result = choice(MADLIBTEMPLATES)

    return render_template(madlib_result, name=name, color=color, 
                                    noun=noun, adjective=adjective, adject2=adject2)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
