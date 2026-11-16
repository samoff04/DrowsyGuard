import time
from src.config import LOW_BLINK_THRESHOLD,HIGH_BLINK_THRESHOLD,ALERTNESS_ALARM_THRESHOLD,ALERTNESS_ALARM_COOLDOWN

class AlertnessAnalyzer:
    def __init__(self):
        self.last_alarm=0

    def calculate_score(self,drowsy,yawning,distracted,blink_count,elapsed_time):
        score=0

        if drowsy:
            score+=40

        if yawning:
            score+=20

        if distracted:
            score+=20

        if elapsed_time>=60:
            if blink_count<LOW_BLINK_THRESHOLD or blink_count>HIGH_BLINK_THRESHOLD:
                score+=20

        score=min(score,100)

        if score>=60:
            level="HIGH RISK"
        elif score>=40:
            level="WARNING"
        elif score>=20:
            level="CAUTION"
        else:
            level="ALERT"

        return score,level

    def should_alarm(self,score):
        current_time=time.time()

        if score>=ALERTNESS_ALARM_THRESHOLD and current_time-self.last_alarm>=ALERTNESS_ALARM_COOLDOWN:
            self.last_alarm=current_time
            return True

        return False