"""Preprocessing: filtering and epoching for motor imagery classification.

Takes a raw recording and produces cleaned, epoched data ready for the
CSP+LDA pipeline.
"""
import mne

from src import config


def filter_raw(raw):
    """Apply notch + bandpass filtering to a copy of the raw data.

    Filters on continuous data (before epoching) so filter edge effects
    stay at the recording boundaries, not inside each epoch.

    Parameters
    ----------
    raw : mne.io.Raw
        Continuous recording.

    Returns
    -------
    mne.io.Raw
        A filtered copy (original is left untouched).
    """
    r = raw.copy()
    r.notch_filter(config.NOTCH_FREQ, picks='eeg', verbose=False)
    r.filter(config.BAND_LOW, config.BAND_HIGH, picks='eeg', verbose=False)
    return r


def make_epochs(raw, events, event_id):
    """Filter, then epoch into labeled left/right imagery trials.

    Parameters
    ----------
    raw : mne.io.Raw
        Continuous recording (unfiltered — this function filters it).
    events : ndarray
        Events array from load_subject_raw.
    event_id : dict
        Label mapping containing at least 'T1' and 'T2'.

    Returns
    -------
    mne.Epochs
        Filtered, epoched trials for T1 (left) and T2 (right).
    """
    raw_filtered = filter_raw(raw)

    epochs = mne.Epochs(
        raw_filtered, events,
        event_id={'T1': event_id['T1'], 'T2': event_id['T2']},
        tmin=config.EPOCH_TMIN, tmax=config.EPOCH_TMAX,
        baseline=None, picks='eeg', preload=True, verbose=False,
    )
    return epochs


def get_Xy(epochs):
    """Extract the data array X and labels y from epochs for scikit-learn.

    Parameters
    ----------
    epochs : mne.Epochs

    Returns
    -------
    X : ndarray, shape (n_trials, n_channels, n_times)
    y : ndarray, shape (n_trials,)
    """
    X = epochs.get_data(copy=False)
    y = epochs.events[:, -1]
    return X, y