import flask
import metrics

ping_app = flask.Flask(__name__)
metrics.setup(ping_app)


@ping_app.route('/ping', methods=['GET'])
def ping():
    return 'Pong', 200


if __name__ == '__main__':  # pragma: no cover
    ping_app.run(debug=True, host='0.0.0.0', port=8040)
