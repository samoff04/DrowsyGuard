import time
from src.config import EAR_THRESHOLD,CONSECUTIVE_FRAMES,MAR_THRESHOLD,YAWN_CONSECUTIVE_FRAMES,ALARM_COOLDOWN

class DrowsinessDetector:
    def __init__(self):
        self.closed_frames=0
        self.yawn_frames=0
        self.drowsy=False
        self.yawning=False
        self.last_alarm=0

    def update(self,ear,mar):
        current_time=time.time()

        if ear<EAR_THRESHOLD:
            self.closed_frames+=1
        else:
            self.closed_frames=0

        if mar>MAR_THRESHOLD:
            self.yawn_frames+=1
        else:
            self.yawn_frames=0

        self.drowsy=self.closed_frames>=CONSECUTIVE_FRAMES
        self.yawning=self.yawn_frames>=YAWN_CONSECUTIVE_FRAMES

        should_alarm=False

        if (self.drowsy or self.yawning) and current_time-self.last_alarm>=ALARM_COOLDOWN:
            should_alarm=True
            self.last_alarm=current_time

        return self.drowsy,self.yawning,should_alarm

    def reset(self):
        self.closed_frames=0
        self.yawn_frames=0
        self.drowsy=False
        self.yawning=False