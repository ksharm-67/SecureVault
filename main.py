from vault import *
from crypto import *
from AESencryption import *
from strength import *

def main():
    
    flag = True

    while(flag):    
        try:
            if not checkVault():
                newPass = input('Setup your master password: ')
                
                if len(newPass) >= 8:
                    if checkStrength(newPass):
                        masterContents = firstSetup(newPass)
                    else:
                        print('Your password is quite weak. It should have at least one number, uppercase letter, and special character\nContinue? (y/n)')
                        if(input().lower() == 'y'):
                            masterContents = firstSetup(newPass)
                        else:
                            continue
                        
                    pwdDump(masterContents)
                else:
                    print('Password is too short. You need a minimum length of 8 characters')
                    continue
                
                print('Vault was missing, created a new one! ')
                createVault()
                
            else:
                masterContents = loadPwd()
            
            entered = input("Enter master password or enter 0 to exit: ")
            print()

            #Check if file exists. If not, create Master Password, else ask user for it
            if(verifyPass(entered, masterContents[0], masterContents[1], masterContents[2])):
                flag2 = True
                
                while(flag2):
                    print("Hello! What do you want to do today? ")                    
                    y = input("\n1 to find a password\n2 to store a password\n3 to delete a password:\n4 to view all\n5 to change master password\n6 to log out: ")
                    
                    if(y == '1'):
                        service = input("Which service? ")
                        
                        if service.strip() != '':
                            res = readVault(service)
                            print()
                            
                            if res:
                                for uname, pwd in res:
                                    decodedPass = decryptPwd(pwd, entered, bytes.fromhex(masterContents[0]))
                                    print(f"The password for your {service} account ({uname}) is: {decodedPass}")
                                    
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
                            
                            #Send the salt to encryptPwd to use for the encrypted key
                            ctxt = encryptPwd(v, bytes.fromhex(masterContents[0]), entered)
                            users.append(ctxt)
                        else:
                            print('Error: You tried to add an empty string. \n')
                            continue

                            
                        print(users)
                        print()
                        
                        if users:
                            storeInVault(users)
                    
                    elif(y == '3'):
                        toDel = input('Which account do you want to delete? Enter the full username: ')
                        if toDel.strip() != '':
                            delRecord(toDel)
                        else:
                            print('Can\'t delete an empty string!\n')
                            continue
                        
                        print('Deleted!\n')
                        
                        
                    elif(y == '4'):
                        viewAll(entered, bytes.fromhex(masterContents[0]))
                        print()
                        
                    elif(y == '5'):
                        chgPwd = input('Setup your new master password: ')
                        
                        if len(chgPwd) >= 8:
                            if checkStrength(chgPwd):
                                pass
                            else:
                                print('Your password is quite weak. It should have at least one number, uppercase letter, and special character\nContinue? (y/n)')
                                if(input().lower() == 'y'):
                                    pass
                                else:
                                    continue
                            
                            confirm = input('Confirm new master password: ')
                            
                        else:
                            print('Your chosen password is too short!\n')
                            continue
                        
                        if chgPwd == confirm:
                            newMaster = firstSetup(chgPwd)
                        else:
                            print('Passwords do not match. Try again\n')
                            continue
                        
                        pwdDump(newMaster)
                        print('Master password changed successfully!\n')
                        
                    elif(y == '6'):
                        flag2 = False
                    
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
