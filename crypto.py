from hashlib import pbkdf2_hmac
import hmac
import random
import string
import os
from pickle import *

    
def firstSetup(pwd: str) -> list:
    itr = 100000
    salt = os.urandom(16)
    hashed = pbkdf2_hmac('sha256', bytes(pwd, 'utf-8'), salt, itr, dklen=64)
    
    #print(f"New chosen password: {pwd}, salt: {salt.hex()}, hash: {hashed.hex()}")
    
    return [salt.hex(), hashed.hex(), itr]
    
def verifyPass(entered: str, salt: bytes, hashed: bytes, itr: int) -> bool:
    newKey = pbkdf2_hmac('sha256', bytes(entered, 'utf-8'), salt, itr, dklen=64)
    
    return hmac.compare_digest(newKey, hashed)
    
def pwdDump(pwd):
    with open('pass.vault', 'wb') as file:
        dump(pwd, file)
    
def loadPwd():
    with open('pass.vault', 'rb') as file:
            try:
                t = load(file)
                #print(t)
                return t
            
            except Exception as e:
                return None
            

# newSalt = firstSetup("kavish")
# print(newSalt)
# 
# same = verifyPass("kavish", bytes.fromhex(newSalt[0]), bytes.fromhex(newSalt[1]), newSalt[2])
# print(same)
