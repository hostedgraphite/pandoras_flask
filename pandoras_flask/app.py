import flask
from pandoras_flask import metrics

ping_app = flask.Flask(__name__)
metrics.setup(ping_app)


@ping_app.route('/ping', methods=['GET'])
def ping():
    return 'Pong', 200


# We expect to run under `uwsgi` etc. but just in case someone wants to run
# this script directly, we provide a default
if __name__ == '__main__':  # pragma: no cover
    ping_app.run(debug=True, host='0.0.0.0', port=8040)
