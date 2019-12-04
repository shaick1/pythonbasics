is_started=False
while (True):
    command1 = input(">").lower()
    if command1 == "start":
        if is_started == True:
            print("Already started")
        else:
            print("Car is started")
            is_started=True
    elif command1 == "stop":
        if is_started == False:
            print("Already stopped")
        else:
            print("Car is stopped")
            is_started=False
    elif (command1 == "help"):
        print("""
start - to start car
stop - to stop car
quit - to quit        
        """)
    elif (command1 == "quit"):
        break
    else:
        print ("Don't understand the command")

print ("Program Ended")
