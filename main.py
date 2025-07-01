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
                
                print('Vault was missing, created a new one! ')
                createVault()
                
            else:
                masterContents = loadPwd()
            
            entered = input("Enter master password or enter 0 to exit: ")

            #Check if file exists. If not, create Master Password, else ask user for it
            if(verifyPass(entered, masterContents[0], masterContents[1], masterContents[2])):
                flag2 = True
                
                while(flag2):
                    print("Hello! What do you want to do today? ")                    
                    y = input("1 to find a password\n2 to store a password\n3 to log out\n4 to view all\n5 to change master password\n6 to delete a password: ")
                    
                    if(y == '1'):
                        service = input("Which service? ")
                        
                        if service.strip() != '':
                            res = readVault(service)
                            print()
                            
                            if res:
                                for uname, pwd in res:
                                    print(f"The password for your {service} account ({uname}) is: {pwd}")
                                    
                            else:
                                print("This service does not exist ")
                            
                            print()
                            
                        else:
                            print("You need to enter a service to view its password")
                            continue
                    
                    elif(y == '2'):
                        users = []          

                        #Service prompt
                        t = input("Enter a service or 0 to reset: ")
                        if t.strip() != '' and t != '0':
                            users.append(t)
                        else:
                            print('You tried to add an empty string. \n')
                            continue

                        #Username prompt                            
                        u = input("Enter a username or 0 to reset: ")
                        if u.strip() != '' and u != '0':
                            users.append(u)
                        else:
                            print('You tried to add an empty string. \n')
                            continue

                        #Password prompt
                        v = input("Enter a password or 0 to reset: ")
                        if v.strip() != '' and v != '0':
                            users.append(v)
                        else:
                            print('You exited the loop or you tried to add an empty string. \n')
                            continue

                            
                        print(users)
                        print()
                        
                        if users:
                            storeInVault(users)
                    
                    elif(y == '3'):
                        flag2 = False
                        
                    elif(y == '4'):
                        viewAll()
                        print()
                        
                    elif(y == '5'):
                        chgPwd = input('Setup your new master password: ')
                        newMaster = firstSetup(chgPwd)
                        pwdDump(newMaster)
                        
                    elif(y == '6'):
                        toDel = input('Which account do you want to delete? Enter the full username: ')
                        delRecord(toDel)
                        print('Deleted!\n')
                    
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
