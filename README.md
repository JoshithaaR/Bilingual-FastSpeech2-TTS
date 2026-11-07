# Bilingual Text-to-Speech using FastSpeech 2

## Project Overview

This project explores FastSpeech 2 for English and Telugu text-to-speech
synthesis. It contains language-specific experiment configurations,
training records, checkpoints, generated outputs, and a technical report.

## Architecture

Text / phoneme sequence
→ FastSpeech 2 Encoder
→ Variance Adaptor (duration, pitch, energy)
→ Decoder
→ Mel-spectrogram
→ HiFi-GAN vocoder
→ Speech waveform

## Telugu Experiment

- Dataset: IndicTTS Telugu
- Processed samples: 1,562
- Training samples: 1,297
- Validation samples: 265
- Audio preprocessing: 16 kHz mono
- Phoneme vocabulary: 52 symbols
- Selected checkpoint: Step 3000
- Backup checkpoint: Step 4000

The duration preparation used MMS word-level timing with heuristic
within-word phoneme-duration allocation. It should not be interpreted
as fully supervised phoneme-level forced alignment.

### Telugu outputs

- Five test utterances: T1, T2a, T2b, T3, T4
- Duration, pitch and energy variance-adaptor plots
- Training and validation loss plots
- Additional generated sample WAV files

The selected Step 3000 checkpoint was chosen after validation analysis
and listening-based comparison. Step 2000 had the lowest reported total
validation loss, while Step 3000 had the lowest mel and postnet mel losses.

## English Experiment

- Filtered training samples: 1,133
- Filtered validation samples: 232
- Training steps: 1,000
- Checkpoints: 250, 500, 750 and 1000

English training logs, loss plots and test audio (E1, E2a, E2b, E3, E4, generated
from the step-1000 checkpoint) are included. Pitch and energy losses remained
disproportionately large (thousands), most likely because the stored pitch/energy
features are not on the normalised scale the model expects, so the English output
is not intelligible. English synthesis is therefore not claimed as successful.
See Report/Technical_Report.pdf, Sections 5 and 8.

## Repository Structure

- `English/` — English experiment scripts and configurations.
- `Telugu/` — Telugu training script, configurations and checkpoints.
- `Results/English/` — English logs, loss plots and checkpoint inventory.
- `Results/Telugu/` — Telugu generated audio, loss plots and variance plots.
- `FastSpeech2_Source/` — shared FastSpeech 2 source implementation.
- `Report/Technical_Report.pdf` — technical report.

## Source Code and Reproducibility Notes

The shared FastSpeech 2 implementation is retained in `FastSpeech2_Source/`.
The language folders contain experiment entry-point scripts and configurations.

Important: the included generic preprocessing and synthesis scripts have
not been fully adapted for Telugu. The Telugu inference script currently
contains English and Mandarin text-processing paths, not a verified Telugu
G2P implementation. The Telugu preprocessing configuration also requires
adaptation to reproduce the completed 16 kHz Telugu feature pipeline.

The English experiment uses precomputed features and its synthesis
pipeline has not been validated successfully. Do not treat the included
English configuration as a verified end-to-end synthesis setup.

The completed Telugu outputs and checkpoints are preserved as experiment
artifacts. Re-running preprocessing or inference requires the language-
specific adaptations described above.

## Large Checkpoints

Model checkpoints are approximately 398 MB each and should be distributed
using Git LFS or an external download location, rather than ordinary Git.

The selected Telugu checkpoint is:
`Telugu/checkpoints/Telugu_FastSpeech2_Selected_Step3000.pth.tar`

The Step 4000 checkpoint is retained as a backup.

## Report

See `Report/Technical_Report.pdf` for implementation details, training
observations, evaluation artifacts and limitations.
