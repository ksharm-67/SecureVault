from pickle import *
import os

def storeInVault(users: list):
    with open('storage.vault', 'ab') as file:
        dump(users, file)
        
def createVault():
    with open('storage.vault', 'wb'):
        pass

def readVault(service: str):
    matches = []
    
    with open('storage.vault', 'rb') as file:
        while True:
            try:
                entry = load(file)
                if entry[0] == service:
                    matches.append((entry[1], entry[2]))
                
            except Exception as e:
                break
    
    return matches

def delRecord(rec: str):
    
    with open('temp.vault', 'wb') as temp:
        with open('storage.vault', 'rb') as file:
            while True:
                try:
                    entry = load(file)
                    if entry[1] != rec:
                        dump(entry, temp)
                    
                except Exception as e:
                    break
    
    os.replace('temp.vault', 'storage.vault')
    
def viewAll():
    with open('storage.vault', 'rb') as file:
        
        while True:
            try:
                loadNames = load(file)
                print(loadNames)
            except Exception as e:
                break
            
        
def checkVault():
    try:
        with open('storage.vault', 'rb') as file:
            load(file)
        return True
        
    except Exception as e:
        print("Exception: ", e)
        return False
        
