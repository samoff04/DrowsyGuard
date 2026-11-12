import cv2
import numpy as np

FACE_3D=np.array([
    (0.0,0.0,0.0),
    (0.0,-330.0,-65.0),
    (-225.0,170.0,-135.0),
    (225.0,170.0,-135.0),
    (-150.0,-150.0,-125.0),
    (150.0,-150.0,-125.0)
],dtype=np.float64)

LANDMARK_IDS=[1,152,33,263,61,291]

def detect_head_pose(frame,landmarks):
    height,width=frame.shape[:2]

    face_2d=[]

    for index in LANDMARK_IDS:
        point=landmarks.landmark[index]
        x=int(point.x*width)
        y=int(point.y*height)
        face_2d.append((x,y))

    face_2d=np.array(face_2d,dtype=np.float64)

    focal_length=width

    camera_matrix=np.array([
        [focal_length,0,width/2],
        [0,focal_length,height/2],
        [0,0,1]
    ],dtype=np.float64)

    distortion=np.zeros((4,1),dtype=np.float64)

    success,rotation_vector,translation_vector=cv2.solvePnP(
        FACE_3D,
        face_2d,
        camera_matrix,
        distortion,
        flags=cv2.SOLVEPNP_ITERATIVE
    )

    if not success:
        return 0.0,0.0

    rotation_matrix,_=cv2.Rodrigues(rotation_vector)
    angles,_,_,_,_,_=cv2.RQDecomp3x3(rotation_matrix)

    pitch=float(angles[0])
    yaw=float(angles[1])

    return pitch,yaw