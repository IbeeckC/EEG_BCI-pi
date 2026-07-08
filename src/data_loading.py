"""Data loading for the PhysioNet EEG Motor Movement/Imagery dataset.

Handles downloading, loading, and preparing a subject's motor imagery runs
into a clean MNE Raw object plus events.
"""
import mne
from mne.datasets import eegbci

from src import config


def load_subject_raw(subject, runs=None):
    """Download and prepare one subject's motor imagery runs.

    Parameters
    ----------
    subject : int
        Subject number (1-109 in the PhysioNet dataset).
    runs : list of int, optional
        Which runs to load. Defaults to the imagery runs from config.

    Returns
    -------
    raw : mne.io.Raw
        Concatenated, standardized, montaged continuous recording.
    events : ndarray
        Events array from the annotations.
    event_id : dict
        Mapping of annotation labels (e.g. 'T1', 'T2') to integer codes.
    """
    if runs is None:
        runs = config.IMAGERY_RUNS

    # Download (or load from disk if already present)
    fnames = eegbci.load_data(
        subjects=[subject], runs=list(runs),
        path=str(config.DATA_DIR), verbose=False,
    )

    # Load each run and concatenate into one continuous recording
    raws = [mne.io.read_raw_edf(f, preload=True, verbose=False) for f in fnames]
    raw = mne.concatenate_raws(raws, verbose=False)

    # Clean channel names and apply electrode-position montage
    eegbci.standardize(raw)
    raw.set_montage(config.get_montage(), verbose=False)

    # Extract events from the annotations
    events, event_id = mne.events_from_annotations(raw, verbose=False)

    return raw, events, event_id