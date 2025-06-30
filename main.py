from vault import *
from crypto import * 

def main():
    
    flag = True

    while(flag):    
        try:
            if not checkVault():
                newPass = input('Setup your master password: ')
                masterContents = firstSetup(newPass)
                pwdDump(masterContents)
                
                print('Vault was missing, created another one! ')
                storeInVault([])
                
            else:
                masterContents = loadPwd()
            
            entered = input("Enter master password or enter 0 to exit: ")

            #Check if file exists. If not, create Master Password, else ask user for it
            if(verifyPass(entered, bytes.fromhex(masterContents[0]), bytes.fromhex(masterContents[1]), masterContents[2])):
                flag2 = True
                
                while(flag2):
                    print("Hello! What do you want to do today? ")                    
                    y = input("1 to read, 2 to write, 3 to log out, 4 to check password contents: ")
                    
                    if(y == '1'):
                        readVault()
                        print()
                    
                    elif(y == '2'):
                        t = ''
                        users = []
                        
                        while t != '0':
                            t = input("Enter a service, username, password, pressing enter after each. Enter 0 when you're done. ")
                            if t != '0' and len(users) < 3 and t.strip() != '':
                                users.append(t)
                            else:
                                print('Either you already completed the record, or you tried to add an empty string. ')
                                t = '0'
                                
                            print(users)
                            print()
                            
                        if users:
                            storeInVault(users)
                    
                    elif(y == '3'):
                        flag2 = False
                        
                    elif(y == '4'):
                        loadPwd()
                    
                    else:
                        print('Error. Not an option' )
                        print()
                        
            elif(entered == '0'):
                break
            
            else:
                print('Wrong password')
                    
        except Exception as e:
            print('Exception: ', e)
            break


if __name__ == '__main__':
    #master = "kavish"
    main()
    print("Bye!")
