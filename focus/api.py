import logging

from flask import Flask, jsonify, request
from joblib import load

from focus import __version__, __name__ as package_name
from focus.conf import MODEL_PATH, CLASS_NAMES
from focus.utils import get_token_explanations, get_sentence_explanations, get_highlighting

app = Flask(package_name)

logging.getLogger().setLevel(logging.INFO)
logging.info("Loading model...")
model = load(MODEL_PATH)
logging.info(f"Model loaded from file {MODEL_PATH}.")

logging.info(f"{package_name}'s API loaded and listening...")


@app.route("/", methods=["GET"])
def health_check():
    """API health check on root URN."""
    logging.info(
        f"Received GET request on the root URN ({package_name} version {__version__})"
    )
    return __version__, 200


@app.route("/explain", methods=["POST"])
def return_score_and_explanations():
    """Get the score and prediction for a given input text."""
    status = 200
    try:
        input_text = request.json["text"]
    except KeyError:
        logging.warning(
            'Wrong request, expected POST request with JSON payload and a "text" field.'
        )
        status = 400
    logging.info(f"Received query with input text: {input_text}")

    y_prob = model.predict_proba([input_text])[0]

    top_class = CLASS_NAMES[y_prob.argmax()]
    logging.info(f"Predicted class: {top_class}")
    classes_scores = {
        f"{CLASS_NAMES[pred]} ({pred})": y_prob[pred] for pred in y_prob.argsort()[::-1]
    }
    logging.info(f"Predicted class: {classes_scores}")
    token_explanations = get_token_explanations(input_text, model)
    sentence_explanations = get_sentence_explanations(input_text, model)
    response = {
        "data": {
            "scores": classes_scores,
            "token_explanations": token_explanations,
            "sentence_explanations": sentence_explanations,
            "highlighted_tokens_top_class": get_highlighting(input_text, token_explanations[top_class]),
            "highlighted_sentences_top_class": get_highlighting(input_text, sentence_explanations[top_class]),
        }
    }
    return jsonify(response), status


if __name__ == "__main__":
    logging.info("Starting api...")
    app.run()
