from flask import Flask
from Utils import SCORES_FILE_NAME

app = Flask(__name__)


def read_score():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read().strip()
        return score
    except Exception as e:
        return str(e)


@app.route('/')
def score_server():
    score = read_score()
    if score.isdigit():
        html_response = f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is <div id="score">{score}</div></h1>
            </body>
        </html>
        """
        return html_response
    else:
        html_response = f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <body>
                    <h1><div id="score" style="color:red">{score}</div></h1>
                    <h2>Error running end-to-end tests</h2>
                <body>
            </body>
        </html>
        """
        return html_response


if __name__ == '__main__':
    app.run()