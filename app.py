import cv2
import winsound

from src.face_detector import detect_face
from src.eye_detector import calculate_ear,draw_eye_landmarks
from src.drowsiness_detector import DrowsinessDetector
from src.utils import FPSCounter,draw_header,draw_metrics,draw_status
from src.config import CAMERA_INDEX,WINDOW_NAME,FRAME_WIDTH,FRAME_HEIGHT

cap=cv2.VideoCapture(CAMERA_INDEX,cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

detector=DrowsinessDetector()
fps_counter=FPSCounter()

print("="*50)
print("DrowsyGuard AI")
print("Real-Time Drowsiness Detection System")
print("="*50)
print("Press Q to exit")
print("="*50)

while True:

    success,frame=cap.read()

    if not success:
        break

    frame=cv2.flip(frame,1)

    height,width=frame.shape[:2]

    face=detect_face(frame)

    ear=0.0
    drowsy=False
    alarm=False
    face_detected=False

    if face:

        face_detected=True

        ear,left_eye,right_eye=calculate_ear(
            face,
            width,
            height
        )

        frame=draw_eye_landmarks(
            frame,
            left_eye,
            right_eye
        )

        drowsy,alarm=detector.update(ear)

        if alarm:
            winsound.Beep(1000,500)

    else:
        detector.reset()

    fps=fps_counter.update()

    frame=draw_header(frame)

    frame=draw_status(
        frame,
        ear,
        drowsy,
        face_detected
    )

    frame=draw_metrics(
        frame,
        ear,
        drowsy,
        fps,
        detector.closed_frames
    )

    cv2.imshow(WINDOW_NAME,frame)

    key=cv2.waitKey(1)&0xFF

    if key==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("DrowsyGuard AI stopped.")