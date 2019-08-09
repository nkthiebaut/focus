import logging

from flask import Flask, jsonify, request
from keras.models import load_model

from focus import __version__, __name__
from focus.conf import MODEL_PATH

app = Flask(__name__)

logging.info("Loading model...")
model = load_model(MODEL_PATH)
logging.info(f"Model loaded from file {MODEL_PATH}.")

test_pred = model.predict(["test text"])
logging.info(f"Test prediction (score should be larger than 0.8): {test_pred:.2f}")

logging.info(f"{__name__}'s API loaded and listening...")


@app.route("/", methods=["GET"])
def health_check():
    """API health check on root URN."""
    logging.info(
        f"Received GET request on the root URN ({__name__} version {__version__})"
    )
    return __version__, 200


@app.route("/explain", methods=["POST"])
def return_score_and_explanations():
    """Get the score and prediction for a given input text."""
    status = 200
    # try:
    #     request_argument = request.args["explains"]
    # except KeyError:
    #     logging.warning(
    #         'Wrong request, expected argument "explains", received the following'
    #         " arguments: %s",
    #         request.args,
    #     )
    #     status = 400
    input_ = request.json
    print(input_)
    response = {"data": {"explains": input_}}
    return jsonify(response), status


if __name__ == "__main__":
    logging.info("Starting api...")
    app.run()
