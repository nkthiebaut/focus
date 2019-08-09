from lime.lime_text import LimeTextExplainer
from focus.conf import CLASS_NAMES, N_FEATURES_EXPLANATIONS
import numpy as np

explainer = LimeTextExplainer(class_names=CLASS_NAMES)


def get_explanations(sample, model):
    exp = explainer.explain_instance(
        sample,
        model.predict_proba,
        num_features=N_FEATURES_EXPLANATIONS,
        top_labels=len(CLASS_NAMES),
    )
    return {
        class_name: exp.as_list(label=i) for i, class_name in enumerate(CLASS_NAMES)
    }


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
