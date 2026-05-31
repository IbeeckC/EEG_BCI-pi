# Day 1: Pi setup + project foundations

## What I did
- Set up Raspberry Pi 5 with 64-bit OS, SSH, and Python development environment
- Installed numpy, scipy, scikit-learn, MNE-Python, and Jupyter on a project venv
- Configured VS Code Remote-SSH for headless development from my MacBook
- Created the project structure, initialized git, pushed to GitHub

## What I learned
- macOS Local Network permissions can silently block VS Code Remote-SSH connections — took me a while to find this
- The Pi 5 is plenty fast for the signal processing workloads ahead
- SSH key auth + a clean `~/.ssh/config` makes the development loop much smoother

## Next
- Download the PhysioNet EEG Motor Movement/Imagery Dataset
- Load a single subject with MNE-Python
- Plot raw EEG and find the alpha rhythm
