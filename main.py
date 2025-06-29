from vault import *

def main(master):
    
    flag = True

    while(flag):    
        try:
            if not checkVault():
                print('Vault was missing, created another one! ')
            
            x = input("Enter master password: ")

            #Check if file exists. If not, create Master Password, else ask user for it
            if(x == master):
                flag2 = True
                
                while(flag2):
                    print("Hello! What do you want to do today? ")                    
                    y = input("1 to read, 2 to write, 3 to quit: ")
                    
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
                        break
                    
                    else:
                        print('Error. Not an option' )
                        print()
                
                flag = False
            
            else:
                print("Wrong password ")
        
        except Exception as e:
            break


if __name__ == '__main__':
    master = "kavish"
    main(master)
    print("Bye!")
