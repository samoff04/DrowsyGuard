import cv2
import winsound
from src.config import CAMERA_INDEX,WINDOW_NAME,FRAME_WIDTH,FRAME_HEIGHT,YAW_THRESHOLD,PITCH_THRESHOLD
from src.face_detector import detect_face
from src.eye_detector import calculate_eye_aspect_ratio,calculate_mouth_aspect_ratio
from src.drowsiness_detector import DrowsinessDetector
from src.head_pose_detector import detect_head_pose
from src.utils import FPSCounter

def main():
    cap=cv2.VideoCapture(CAMERA_INDEX,cv2.CAP_MSMF)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    detector=DrowsinessDetector()
    fps_counter=FPSCounter()

    while True:
        ret,frame=cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        frame=cv2.flip(frame,1)
        landmarks=detect_face(frame)

        if landmarks:
            ear=calculate_eye_aspect_ratio(landmarks)
            mar=calculate_mouth_aspect_ratio(landmarks)

            drowsy,yawning,should_alarm=detector.update(ear,mar)

            pitch,yaw=detect_head_pose(frame,landmarks)

            distracted=abs(yaw)>YAW_THRESHOLD or abs(pitch)>PITCH_THRESHOLD

            if should_alarm:
                winsound.Beep(1000,500)

            blink_count=detector.get_blink_count()
            blink_rate=detector.get_blink_rate()

            if drowsy:
                status="DROWSINESS DETECTED"
                status_color=(0,0,255)
            elif yawning:
                status="YAWNING DETECTED"
                status_color=(0,140,255)
            elif distracted:
                status="DISTRACTED"
                status_color=(0,0,255)
            else:
                status="AWAKE"
                status_color=(0,255,0)

            cv2.putText(frame,f"EAR: {ear:.2f}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

            cv2.putText(frame,f"MAR: {mar:.2f}",(20,70),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

            cv2.putText(frame,status,(20,110),cv2.FONT_HERSHEY_SIMPLEX,0.8,status_color,2)

            cv2.putText(frame,f"Eye Frames: {detector.closed_frames}",(20,145),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)

            cv2.putText(frame,f"Yawn Frames: {detector.yawn_frames}",(20,175),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)

            cv2.putText(frame,f"Blinks (60s): {blink_count}",(20,205),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)

            cv2.putText(frame,f"Blink Rate: {blink_rate}/min",(20,235),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)

            cv2.putText(frame,f"Pitch: {pitch:.1f}",(20,270),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)

            cv2.putText(frame,f"Yaw: {yaw:.1f}",(20,300),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)

        else:
            detector.reset()
            cv2.putText(frame,"FACE NOT DETECTED",(20,40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

        fps=fps_counter.update()

        cv2.putText(frame,f"FPS: {fps:.1f}",(20,335),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)

        cv2.imshow(WINDOW_NAME,frame)

        if cv2.waitKey(1)&0xFF==ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()