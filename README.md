# DrowsyGuard

DrowsyGuard is a real-time driver drowsiness detection system built with Python, OpenCV, and MediaPipe. It monitors facial landmarks to detect prolonged eye closure and yawning, providing real-time visual and audio alerts.

## Features

- Face and facial landmark detection
- Eye Aspect Ratio (EAR) calculation
- Mouth Aspect Ratio (MAR) calculation
- Real-time drowsiness warning
- Audio alerts using system beep
- FPS monitoring

## Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy

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

### Clone the Repository

```bash
git clone https://github.com/samoff04/DrowsyGuard.git
cd DrowsyGuard
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Press `Q` to exit the application.

## Author

Samarth Varshney