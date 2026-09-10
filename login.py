import flask

app = flask.Flask(__name__)


@app.route('/login')
def login():
    return flask.render_template('login.html')
