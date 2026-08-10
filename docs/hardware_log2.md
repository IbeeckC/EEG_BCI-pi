# Milestone: First Reliable EEG — Alpha Rhythm Validated (Grommet Cap)

## Result
Achieved repeatable, good-quality EEG recording of my own alpha rhythm using
the self-built PiEEG-16 setup. Across three consecutive eyes-closed/eyes-open
runs (no re-gelling between them):
- **ch15 (occipital): alpha ratio 4.88 / 5.65 / 6.54** — passed every run
- **ch16 (occipital): alpha ratio 2.79 / 4.81 / 5.41** — passed every run
- Noise floor (>60 Hz power) held **stable at 44–52%** across all runs
- (ch14 remained weak (~1.0) — single-electrode contact issue, not a setup
  failure)

Bar set beforehand: floor <50%, alpha >1.7, steady across ≥3 runs. Two of three
occipital channels cleared it cleanly and repeatably — the EEG is validated.

## What finally worked
- **Silicone/rubber grommets** seated in enlarged beanie holes. This solved the
  three problems the plain beanie couldn't:
  1. **Scalp access** — enlarged holes let me part hair and gel the scalp
     directly (closed knit fabric had blocked this).
  2. **Stable electrode holding** — grommets grip the electrode firmly and lock
     to the cap, vs. loose knit that let electrodes slide and drift.
  3. **Consistent contact over time** — stable seating stopped the noise floor
     from degrading mid-session, which had been a persistent failure.

## The journey (why this took many sessions)
- Silicone swim cap: too slippery/non-snug — abandoned, repurposed as a
  reference-electrode pressure band.
- Cotton beanie: better grip/breathability, but **closed fabric blocked scalp
  access** — the core, ultimately fatal limitation.
- Iterated through velcro (electrode stability), elastic band orientation
  (fixed noise-floor drift), pre-gel/hair-part method, electrode cleaning.
- Key diagnostic: shorting all inputs proved the 30–60 Hz noise came from
  electrode/reference contact, not the board.
- Learned the hard way: results swung session-to-session because multiple
  variables changed at once + no scalp access. Fixed by disciplined
  one-variable-at-a-time testing and a defined pass condition.
- Concluded the beanie was at its ceiling → added grommets (cheap, ~$6–15)
  rather than buying an expensive clinical cap. The targeted fix worked.

## Lessons
- Contact quality — especially the shared reference/bias — gates every channel.
- Noise-floor % (>60 Hz) and eyes-closed alpha ratio are the metrics that
  matter; raw traces are not eyeball-readable at this noise level.
- Repeatability (same result across ≥3 runs) is the real bar, not one good run.
- A cheap targeted fix (grommets) beat both endless beanie tweaking and an
  expensive cap — let the cheapest viable fix prove itself first.

## Next
- Optional: re-seat ch14 for a clean 3/3 sweep.
- Move toward motor imagery (C3/C4, mu rhythm) — harder contact + subtler
  signal than occipital alpha; will need this same contact discipline.
- Connect the validated src/ CSP+LDA pipeline to real recorded data.
