command=""
started=False
stopped=False
while command !="quit":
    command=input("> ").lower()
    if command=="start":
        if started:
             print("Car started...Ready to go!")
        else:
            started=True
            print('Car started.') 
                
    elif command=="stop":
        """
        if not started:
             print("Car is already stopped!") 
            
        else:
            started=False
            print("Car stopped. ") 
           

        """
        if  stopped:
            print("Car is already stopped!")
              
        else:
            stopped=True
            print("Car stopped. ") 
         
         
                      
    elif command=="help":
         print("""
Choose to any option.......
start - to start the car"
stop - to stop the car" start
quit - to exit""")
    elif command=="quit":
        break;
    else:        
         print("Sorry,..I don't understand that...")
         print("Enter to help")

         
         
               