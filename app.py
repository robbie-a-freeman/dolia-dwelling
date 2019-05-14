"""Controls the web server for the entire site with a Flask framework. Assumes
that the main app is app.py. Contains links to the rest of the site, and it
handles non-static downloads.
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import abort
from flask import redirect
from flask import url_for
from flask import send_file

import os
import sys

app = Flask(__name__)

__author__ = "Robbie Freeman"
__credits__ = ["Robbie Freeman"]
__maintainer__ = "Robbie Freeman"
__email__ = "robbie.a.freeman@gmail.com"
__status__ = "Development"

# calls the app so it can run
if __name__ == "__main__":
    app.run()

# loads Smoke Stop page
@app.route('/home')
@app.route('/')
def smokestop():
    return render_template('index.html')
