#!/usr/bin/python3
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    # start the flask development server
    # List on all all available network interfaces (0.0.0.0) and port 5000
    app.run(host="0.0.0.0", port=5000)
