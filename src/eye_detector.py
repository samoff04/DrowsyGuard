import cv2
import numpy as np

LEFT_EYE=[362,385,387,263,373,380]
RIGHT_EYE=[33,160,158,133,153,144]

def distance(p1,p2):
    return np.linalg.norm(np.array(p1)-np.array(p2))

def get_eye_points(landmarks,indices,width,height):
    points=[]

    for index in indices:
        landmark=landmarks.landmark[index]
        points.append(
            (
                int(landmark.x*width),
                int(landmark.y*height)
            )
        )

    return points

def eye_aspect_ratio(points):
    vertical_1=distance(points[1],points[5])
    vertical_2=distance(points[2],points[4])
    horizontal=distance(points[0],points[3])

    if horizontal==0:
        return 0.0

    return (vertical_1+vertical_2)/(2*horizontal)

def calculate_ear(landmarks,width,height):
    left=get_eye_points(
        landmarks,
        LEFT_EYE,
        width,
        height
    )

    right=get_eye_points(
        landmarks,
        RIGHT_EYE,
        width,
        height
    )

    left_ear=eye_aspect_ratio(left)
    right_ear=eye_aspect_ratio(right)

    ear=(left_ear+right_ear)/2

    return ear,left,right

def draw_eye_landmarks(frame,left,right):
    cv2.polylines(
        frame,
        [np.array(left)],
        True,
        (255,255,0),
        1
    )

    cv2.polylines(
        frame,
        [np.array(right)],
        True,
        (255,255,0),
        1
    )

    for point in left+right:
        cv2.circle(
            frame,
            point,
            2,
            (255,255,255),
            -1
        )

    return frame