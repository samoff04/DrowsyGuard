import time
from src.config import EAR_THRESHOLD,CONSECUTIVE_FRAMES,ALARM_COOLDOWN

class DrowsinessDetector:

    def __init__(self):
        self.closed_frames=0
        self.last_alarm=0
        self.drowsy=False

    def update(self,ear):

        if ear<EAR_THRESHOLD:
            self.closed_frames+=1
        else:
            self.closed_frames=max(0,self.closed_frames-2)

        self.drowsy=self.closed_frames>=CONSECUTIVE_FRAMES

        alarm=False

        if self.drowsy:
            now=time.time()

            if now-self.last_alarm>=ALARM_COOLDOWN:
                alarm=True
                self.last_alarm=now

        return self.drowsy,alarm

    def reset(self):
        self.closed_frames=0
        self.drowsy=False