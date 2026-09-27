from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy",
        "service": "test-recovery-service"
    })


@app.route("/")
def home():

    return jsonify({
        "message": "Test recovery service is running"
    })


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5001,
        debug=False
    )