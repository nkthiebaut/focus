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
    MODEL_NAME = "pipeline.joblib"
else:
    DEFAULT_EMBEDDINGS_NAME = "glove-twitter-100"
    MODEL_VERSION = "1.0"
    MODEL_NAME = f"model_v{MODEL_VERSION}.h5"
    MODEL_NAME = "pipeline.joblib"

MODEL_PATH = os.path.join(MODELS_DIR, MODEL_NAME)

N_FEATURES_EXPLANATIONS = 10

CLASS_NAMES = [
    "alt.atheism",
    "comp.graphics",
    "comp.os.ms-windows.misc",
    "comp.sys.ibm.pc.hardware",
    "comp.sys.mac.hardware",
    "comp.windows.x",
    "misc.forsale",
    "rec.autos",
    "rec.motorcycles",
    "rec.sport.baseball",
    "rec.sport.hockey",
    "sci.crypt",
    "sci.electronics",
    "sci.med",
    "sci.space",
    "soc.religion.christian",
    "talk.politics.guns",
    "talk.politics.mideast",
    "talk.politics.misc",
    "talk.religion.misc",
]
