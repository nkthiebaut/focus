import os
from focus.conf import MODELS_DIR


def test_models_dir_existence():
    """ Check all necessary directories exist """
    assert os.path.exists(MODELS_DIR)
