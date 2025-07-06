import time
from datetime import datetime
from pickle import *

def init_failed_login():
    with open('attempts.vault', 'wb') as file:
        dump({'count' : 0}, file)    

def failedAttempt(enteredPwd: str, numWrong):
    numWrong += 1
    
    with open('attempts.vault', 'wb') as file:
        dump({'count' : numWrong, 'when' : datetime.now()}, file)
    

    delay = min(3 * numWrong, 30)
    print(f"Wrong password! Wrong attempts: {numWrong}, Locked for {delay} seconds\n")
    time.sleep(delay)
    
    return numWrong
