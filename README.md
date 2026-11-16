# DrowsyGuard

A real-time driver drowsiness and distraction detection system built using Python, OpenCV and MediaPipe.

## Features

- Face and facial landmark detection
- Eye closure and yawning detection using EAR and MAR
- Blink counting and rate analysis
- Head pose estimation using yaw and pitch
- Driver distraction detection
- Combined alertness score with audio warnings

## Tech Stack

Python · OpenCV · MediaPipe · NumPy

## Project Structure

```text
DrowsyGuard/
├── src/
├── assets/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

```bash
git clone https://github.com/samoff04/DrowsyGuard.git
cd DrowsyGuard
python -m venv venv
```

Activate the environment and install dependencies:

```bash
venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Press `Q` to exit.

## Author

Samarth Varshney