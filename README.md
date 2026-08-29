# DrowsyGuard AI

DrowsyGuard AI is a real-time driver drowsiness detection system built with Python, OpenCV, and MediaPipe. It monitors eye movement through facial landmarks and uses the Eye Aspect Ratio (EAR) to detect prolonged eye closure and provide an instant warning.

## Features

* Real-time webcam monitoring
* Face and eye landmark detection
* Eye Aspect Ratio (EAR) calculation
* Real-time drowsiness warning
* Audio alert using system beep

## Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy

## Project Structure

```text
DrowsyGuard/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── face_detector.py
│   ├── eye_detector.py
│   ├── drowsiness_detector.py
│   └── utils.py
├── assets/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/samoff04/DrowsyGuard.git
cd DrowsyGuard
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Author

Samarth Varshney
---