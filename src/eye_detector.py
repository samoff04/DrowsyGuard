import numpy as np

LEFT_EYE=[362,385,387,263,373,380]
RIGHT_EYE=[33,160,158,133,153,144]

MOUTH=[61,291,13,14,81,311,178,402]

def distance(p1,p2):
    return np.linalg.norm(np.array([p1.x,p1.y])-np.array([p2.x,p2.y]))

def calculate_ear(landmarks,indices):
    points=[landmarks.landmark[i] for i in indices]

    vertical_1=distance(points[1],points[5])
    vertical_2=distance(points[2],points[4])
    horizontal=distance(points[0],points[3])

    if horizontal==0:
        return 0.0

    return (vertical_1+vertical_2)/(2.0*horizontal)

def calculate_eye_aspect_ratio(landmarks):
    left_ear=calculate_ear(landmarks,LEFT_EYE)
    right_ear=calculate_ear(landmarks,RIGHT_EYE)

    return (left_ear+right_ear)/2.0

def calculate_mouth_aspect_ratio(landmarks):
    points=[landmarks.landmark[i] for i in MOUTH]

    vertical_1=distance(points[2],points[3])
    vertical_2=distance(points[4],points[6])
    vertical_3=distance(points[5],points[7])
    horizontal=distance(points[0],points[1])

    if horizontal==0:
        return 0.0

    return (vertical_1+vertical_2+vertical_3)/(3.0*horizontal)