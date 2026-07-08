"""The validated CSP + LDA classification pipeline and evaluation.

This is the core motor-imagery classifier: CSP for spatial feature extraction,
LDA for classification. Single-band CSP+LDA was validated as the best approach
for this small-data regime (multi-band FBCSP did not improve on it).
"""
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import StratifiedKFold, cross_val_score
from mne.decoding import CSP

from src import config
from src import data_loading, preprocessing


def make_pipeline(n_components=None):
    """Build the CSP + LDA pipeline.

    Parameters
    ----------
    n_components : int, optional
        Number of CSP components. Defaults to config.N_CSP_COMPONENTS.

    Returns
    -------
    sklearn.pipeline.Pipeline
        Untrained CSP -> LDA pipeline.
    """
    if n_components is None:
        n_components = config.N_CSP_COMPONENTS

    csp = CSP(n_components=n_components, reg=None, log=True, norm_trace=False)
    lda = LinearDiscriminantAnalysis()
    return Pipeline([('CSP', csp), ('LDA', lda)])


def evaluate(X, y, n_components=None, n_splits=5, random_state=42):
    """Cross-validate the pipeline on one subject's data.

    CSP and LDA are re-fit inside each fold (no data leakage).

    Parameters
    ----------
    X : ndarray, shape (n_trials, n_channels, n_times)
    y : ndarray, shape (n_trials,)
    n_components : int, optional
    n_splits : int
        Number of cross-validation folds.
    random_state : int
        Seed for reproducible fold splits.

    Returns
    -------
    dict
        {'mean', 'std', 'scores', 'chance'} accuracy summary.
    """
    pipe = make_pipeline(n_components)
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True,
                         random_state=random_state)
    scores = cross_val_score(pipe, X, y, cv=cv, scoring='accuracy')
    chance = np.bincount(y).max() / len(y)
    return {
        'mean': scores.mean(),
        'std': scores.std(),
        'scores': scores,
        'chance': chance,
    }


def evaluate_subject(subject, n_components=None):
    """Full end-to-end evaluation for one subject: load -> preprocess -> evaluate.

    Convenience wrapper combining the whole pipeline.

    Parameters
    ----------
    subject : int
    n_components : int, optional

    Returns
    -------
    dict
        Accuracy summary from evaluate().
    """
    raw, events, event_id = data_loading.load_subject_raw(subject)
    epochs = preprocessing.make_epochs(raw, events, event_id)
    X, y = preprocessing.get_Xy(epochs)
    return evaluate(X, y, n_components=n_components)