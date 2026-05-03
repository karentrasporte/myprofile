from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/learning')
def learning():
    posts = [{
            "date": "May 2026",
            "title": "Getting started with Flask",
            "body": "Set up my first Flask app using the application factory pattern. Learned about Blueprints, routes, and Jinja2 templates. Biggest surprise: how lightweight Flask is compared to enterprise frameworks I've used before."
        },
        {
            "date": "April 2026",
            "title": "Docker fundamentals",
            "body": "Containerised my Flask app using Docker. Learned why copying requirements.txt before the rest of the code speeds up builds through layer caching. Running docker compose up --build for the first time was very satisfying."
        },
        {
            "date": "March 2026",
            "title": "Python virtual environments",
            "body": "Spent more time than I'd like to admit figuring out why 'python' wasn't found on my Mac. Turns out modern Macs use python3 and venv is the right way to isolate dependencies per project."
        }
    ]
    return render_template('learning.html', posts=posts)