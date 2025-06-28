def main():
        
    flag = True

    while(flag):    
        try:
            x = input("Enter master password: ")

            #Check if file exists. If not, create Master Password, else ask user for it
            if(x == master):
                print("Hello! ")
            
            
            else:
                print("Wrong password")
        
        except Exception as e:
            print("Error")


if __name__ == '__main__':
    
    main()
    print("Bye!")
