from flask import Flask

app = Flask(__name__)

SCORES_FILE = "scores.txt"

def get_score():
    try:
        with open(SCORES_FILE, "r") as file:
            score = file.read().strip()
    except FileNotFoundError:
        score = "0"  # If file doesn't exist, set score to 0
    return score

def generate_html(score):
    html = f"""
    <html>
        <head>
            <title>Score Game</title>
        </head>
        <body>
            <h1>The Score is : </h1>
            <div id="score">{score}</div>
        </body>
    </html>
    """
    return html

def generate_error_html(error_message):
    html = f"""
    <html>
        <head>
            <title>Score Game</title>
        </head>
        <body>
            <h1>ERROR</h1>
            <div id="score" style="color:red">{error_message}</div>
        </body>
    </html>
    """
    return html

@app.route('/')
def score_server():
    try:
        score = get_score()
        html = generate_html(score)
    except Exception as e:
        error_message = str(e)
        html = generate_error_html(error_message)
    return html

