import time
from collections import deque
from src.config import EAR_THRESHOLD,CONSECUTIVE_FRAMES,MAR_THRESHOLD,YAWN_CONSECUTIVE_FRAMES,BLINK_MIN_DURATION,BLINK_MAX_DURATION,BLINK_RATE_WINDOW,ALARM_COOLDOWN

class DrowsinessDetector:
    def __init__(self):
        self.closed_frames=0
        self.yawn_frames=0
        self.drowsy=False
        self.yawning=False
        self.last_alarm=0
        self.eyes_closed=False
        self.blink_start_time=None
        self.blinks=deque()

    def update(self,ear,mar):
        current_time=time.time()

        if ear<EAR_THRESHOLD:
            self.closed_frames+=1

            if not self.eyes_closed:
                self.eyes_closed=True
                self.blink_start_time=current_time

        else:
            if self.eyes_closed and self.blink_start_time is not None:
                duration=current_time-self.blink_start_time

                if BLINK_MIN_DURATION<=duration<=BLINK_MAX_DURATION:
                    self.blinks.append(current_time)

            self.closed_frames=0
            self.eyes_closed=False
            self.blink_start_time=None

        if mar>MAR_THRESHOLD:
            self.yawn_frames+=1
        else:
            self.yawn_frames=0

        self.drowsy=self.closed_frames>=CONSECUTIVE_FRAMES
        self.yawning=self.yawn_frames>=YAWN_CONSECUTIVE_FRAMES

        while self.blinks and current_time-self.blinks[0]>BLINK_RATE_WINDOW:
            self.blinks.popleft()

        should_alarm=False

        if (self.drowsy or self.yawning) and current_time-self.last_alarm>=ALARM_COOLDOWN:
            should_alarm=True
            self.last_alarm=current_time

        return self.drowsy,self.yawning,should_alarm

    def get_blink_count(self):
        return len(self.blinks)

    def get_blink_rate(self):
        current_time=time.time()
        while self.blinks and current_time-self.blinks[0]>BLINK_RATE_WINDOW:
            self.blinks.popleft()

        return len(self.blinks)

    def reset(self):
        self.closed_frames=0
        self.yawn_frames=0
        self.drowsy=False
        self.yawning=False
        self.eyes_closed=False
        self.blink_start_time=None
        self.blinks.clear()