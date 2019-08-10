from lime.lime_text import LimeTextExplainer
from focus.conf import CLASS_NAMES, N_FEATURES_EXPLANATIONS
import numpy as np
from nltk import sent_tokenize
from functools import partial

token_explainer = LimeTextExplainer(class_names=CLASS_NAMES)
sentence_explainer = LimeTextExplainer(class_names=CLASS_NAMES, split_expression=sent_tokenize)


def get_explanations(sample, model, explainer, n_features=N_FEATURES_EXPLANATIONS):
    class_names = explainer.class_names
    exp = explainer.explain_instance(
        sample,
        model.predict_proba,
        num_features=n_features,
        top_labels=len(class_names),
    )
    return {
        class_name: exp.as_list(label=i) for i, class_name in enumerate(class_names)
    }


get_token_explanations = partial(get_explanations, explainer=token_explainer)
get_sentence_explanations = partial(get_explanations, explainer=sentence_explainer)


def get_highlighting(text, tokens_scores_mapping):
    for token, score in tokens_scores_mapping:
        highlight = (
            f"rgba(0, 230, 0, {np.sqrt(score)})"
            if score > 0
            else f"rgba(232, 47, 58, {np.sqrt(-score)})"
        )
        text = text.replace(
            token, f'<span style="background-color: {highlight}">{token}</span>'
        )
    return text
