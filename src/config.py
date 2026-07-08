"""Shared configuration for the BCI project.

Central place for constants used across data loading, preprocessing, and
classification, so notebooks and scripts stay consistent.
"""
from pathlib import Path
import mne

# Where raw datasets live
DATA_DIR = Path.home() / "projects" / "bci" / "data" / "raw"

# Motor imagery runs (imagined left vs right fist) in the PhysioNet dataset
IMAGERY_RUNS = [4, 8, 12]

# Standard electrode-position montage
MONTAGE_NAME = "standard_1005"

# Preprocessing: notch + bandpass
NOTCH_FREQ = 60.0          # US mains
BAND_LOW = 8.0             # bandpass low edge (mu/beta)
BAND_HIGH = 30.0           # bandpass high edge

# Epoching window (seconds relative to cue) — validated as the best default
EPOCH_TMIN = 0.5
EPOCH_TMAX = 2.5

# Classifier
N_CSP_COMPONENTS = 4

def get_montage():
    """Return the standard montage object."""
    return mne.channels.make_standard_montage(MONTAGE_NAME)