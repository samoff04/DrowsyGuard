import cv2
import mediapipe as mp
from src.config import MAX_NUM_FACES,MIN_DETECTION_CONFIDENCE,MIN_TRACKING_CONFIDENCE

mp_face_mesh=mp.solutions.face_mesh

face_mesh=mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=MAX_NUM_FACES,
    refine_landmarks=True,
    min_detection_confidence=MIN_DETECTION_CONFIDENCE,
    min_tracking_confidence=MIN_TRACKING_CONFIDENCE
)

def detect_face(frame):
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return None

    return results.multi_face_landmarks[0]