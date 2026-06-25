# EEG Fundamentals

Notes in my own words on the core EEG concepts underlying this project.

## Frequency Bands

EEG rhythms are grouped into five frequency bands. The boundaries vary
slightly between sources, but the standard ranges and associations are:

- **Delta (< 4 Hz):** The lowest frequency, highest amplitude rhythm.
  Associated with deep, dreamless sleep. More prominent in young children's brains.
- **Theta (4–8 Hz):** Associated with drowsiness, relaxation, REM sleep,
  meditation, and memory processes.
- **Alpha (8–13 Hz):** Associated with relaxed wakefulness. Appears strongly
  over the occipital (visual) cortex when the eyes are closed and suppresses
  when the eyes open or visual attention engages.
- **Beta (13–30 Hz):** Associated with active, alert thinking, focused attention,
  and motor control. Sometimes split into low and high beta.
- **Gamma (> 30 Hz):** The highest frequency band. Associated with high-level
  cognitive processing, peak focus, and learning. Small and hard to measure
  cleanly from the scalp (heavily contaminated by muscle activity).

These rhythms vary from person to person, and can differ with factors such as
age and neurodivergence.

### Mu rhythm (important for this project)

The **mu rhythm** shares the same frequency range as alpha (8–13 Hz) but comes
from a different place and means something different:

- **Alpha** = idling rhythm of the **visual cortex** (occipital), suppresses when eyes open.
- **Mu** = idling rhythm of the **motor cortex** (electrodes C3, C4, Cz), suppresses
  when you move *or imagine moving*.

This motor-cortex suppression is the signal my BCI detects.

## ERD and ERS

When a cortical region changes state, the power of its idling rhythm changes:

- **ERD (Event-Related Desynchronization):** Power **drops** in a specific band over
  a cortical area. The idling rhythm breaks up because the region is **activating**.
  Example: imagining a hand movement causes mu/beta ERD over the opposite-side motor cortex.
- **ERS (Event-Related Synchronization):** Power **rises**. The region resynchronizes
  back into its idling rhythm as it **returns to rest**.

For motor imagery: imagining the **left** hand causes ERD over the **right** motor
cortex (C4); imagining the **right** hand causes ERD over the **left** motor cortex (C3).
This crossed (contralateral) lateralization is what makes left-vs-right classification possible.

## The 10–20 System

A standardized system for naming and placing EEG electrodes on the scalp.

- Positions are defined relative to four skull landmarks: the **nasion** (bridge of
  the nose), the **inion** (bump at the back of the skull), and the two
  **preauricular points** (in front of each ear).
- The numbers **10** and **20** refer to electrodes being spaced at **10% or 20%**
  of the total distance between these landmarks.
- Naming convention: letters indicate the brain region (F = frontal, C = central,
  P = parietal, O = occipital, T = temporal). Numbers indicate the hemisphere —
  **odd = left, even = right**, and **z = midline** (zero).
- Relevant to this project: **C3** sits over the left motor cortex, **C4** over the
  right motor cortex, **Cz** at the central midline.

Extensions (10–10, 10–05) add more electrodes at finer spacing.

## Common Artifacts

EEG is a microvolt-scale signal, so it is easily contaminated. Common artifacts:

- **Muscle activity (EMG):** Jaw clenching, frowning, neck tension. Broadband,
  strongest at higher frequencies (above ~20–30 Hz).
- **Eye movement / blinks (EOG):** Large, slow voltage swings, biggest at the front
  of the head. Blinks are often the largest feature in a raw frontal recording.
- **Mains interference:** A sharp spike at the power-line frequency — **60 Hz in
  the US** (50 Hz in Europe), plus harmonics. Picked up from power lines, chargers,
  and electronics. Removed with a notch filter.
- **Heartbeat (ECG):** Roughly 1–1.5 Hz, can intrude into the recording.
- **Drift / electrode artifacts:** Slow baseline wander from sweat, electrode movement,
  or poor skin contact (low-frequency).
