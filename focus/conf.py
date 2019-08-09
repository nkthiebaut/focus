import logging
import os
import sys

MODELS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "models"
)

# Load lighter embeddings for tests
if hasattr(sys, "_called_from_test"):
    logging.warning("Loading toy embeddings for testing")
    DEFAULT_EMBEDDINGS_NAME = "glove-twitter-25"
    MODEL = os.path.join(MODELS_DIR, "model_tests.h5")
else:
    DEFAULT_EMBEDDINGS_NAME = "glove-twitter-100"
    MODEL_VERSION = "1.0"

MODEL_PATH = os.path.join(MODELS_DIR, f"model_v{MODEL_VERSION}.h5")
