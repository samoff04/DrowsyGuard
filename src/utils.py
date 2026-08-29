import cv2
import time
from src.config import EAR_THRESHOLD,CONSECUTIVE_FRAMES

class FPSCounter:

    def __init__(self):
        self.previous=time.time()
        self.fps=0

    def update(self):
        current=time.time()
        elapsed=current-self.previous

        if elapsed>0:
            self.fps=1/elapsed

        self.previous=current

        return self.fps


def draw_header(frame):
    height,width=frame.shape[:2]

    cv2.rectangle(
        frame,
        (0,0),
        (width,75),
        (18,18,18),
        -1
    )

    cv2.putText(
        frame,
        "DROWSYGUARD",
        (25,38),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255,255,255),
        2
    )

    cv2.putText(
        frame,
        "REAL-TIME DRIVER MONITORING",
        (25,62),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.45,
        (160,160,160),
        1
    )

    cv2.putText(
        frame,
        "Q  EXIT",
        (width-105,42),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (180,180,180),
        1
    )

    return frame


def draw_metrics(frame,ear,drowsy,fps,closed_frames):

    height,width=frame.shape[:2]

    x=25
    y=height-155

    cv2.rectangle(
        frame,
        (x,y),
        (x+350,height-20),
        (18,18,18),
        -1
    )

    cv2.putText(
        frame,
        "SYSTEM METRICS",
        (x+20,y+30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (180,180,180),
        1
    )

    cv2.putText(
        frame,
        f"EAR       {ear:.3f}",
        (x+20,y+65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255,255,255),
        2
    )

    cv2.putText(
        frame,
        f"FPS       {fps:.1f}",
        (x+20,y+95),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255,255,255),
        2
    )

    cv2.putText(
        frame,
        f"EYE STATE {'CLOSED' if ear<EAR_THRESHOLD else 'OPEN'}",
        (x+20,y+125),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255,255,255),
        1
    )

    progress=min(
        closed_frames/CONSECUTIVE_FRAMES,
        1.0
    )

    bar_x=x+20
    bar_y=y+137
    bar_width=310
    bar_height=8

    cv2.rectangle(
        frame,
        (bar_x,bar_y),
        (bar_x+bar_width,bar_y+bar_height),
        (60,60,60),
        -1
    )

    cv2.rectangle(
        frame,
        (bar_x,bar_y),
        (
            bar_x+int(bar_width*progress),
            bar_y+bar_height
        ),
        (0,180,255) if not drowsy else (0,0,255),
        -1
    )

    return frame


def draw_status(frame,ear,drowsy,face_detected):

    height,width=frame.shape[:2]

    if not face_detected:

        cv2.rectangle(
            frame,
            (width//2-190,95),
            (width//2+190,155),
            (20,20,20),
            -1
        )

        cv2.putText(
            frame,
            "FACE NOT DETECTED",
            (width//2-165,133),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,165,255),
            2
        )

        return frame

    if drowsy:

        cv2.rectangle(
            frame,
            (0,75),
            (width,145),
            (0,0,180),
            -1
        )

        cv2.putText(
            frame,
            "DROWSINESS DETECTED",
            (width//2-190,120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255,255,255),
            3
        )

    else:

        cv2.rectangle(
            frame,
            (width-235,90),
            (width-25,140),
            (20,20,20),
            -1
        )

        cv2.putText(
            frame,
            "●  AWAKE",
            (width-215,123),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (0,255,0),
            2
        )

    return frame