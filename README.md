# Motor Imagery Brain-Computer Interface

A real-time 2-channel EEG-based motor imagery BCI built on a Raspberry Pi 5. The system acquires EEG signals from a custom analog front-end, processes them in real time using a DSP pipeline (notch filter, bandpass, Common Spatial Patterns), and classifies left vs. right hand motor imagery using Linear Discriminant Analysis to drive an external output.

## Status

🚧 Under construction. Currently in Phase 0: foundations and dataset exploration.

## Project structure
## Setup

```bash
git clone git@github.com:beeckiC/EEG_BCI-pi.git
cd EEG_BCI-pi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Roadmap

- [x] Set up Raspberry Pi development environment
- [ ] Phase 0: Foundations — explore PhysioNet motor imagery dataset
- [ ] Phase 1: Real-time signal acquisition (ADS1299)
- [ ] Phase 2: DSP pipeline (notch, bandpass, CSP)
- [ ] Phase 3: Motor imagery classifier (LDA)
- [ ] Phase 4: Live demo
- [ ] Phase 5 (stretch): Custom analog front-end PCB

## License

MIT