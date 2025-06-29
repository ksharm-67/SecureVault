from pickle import *

def storeInVault(users: list):
    with open('pwd.vault', 'ab') as file:
        dump(users, file)
        
def readVault():
    with open('pwd.vault', 'rb') as file:
        
        while True:
            try:
                loadNames = load(file)
                print(loadNames)
            except Exception as e:
                print('No more names')
                break
                
        
def checkVault():
    try:
        with open('pwd.vault', 'rb') as file:
            load(file)
        return True
        
    except Exception as e:
        print("Exception: ", e)
        storeInVault([])
        return False
        
