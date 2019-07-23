command="" #empty string that don`t have any character
while command.lower()!="quit":
        command = input("> ") # getting the variable and toring the same
        if command.lower()== "start":
            print("Car has started....")
        elif command.lower()== "stop":
            print("Car is stopped...")
        elif command.lower()== "help":
            print("""
    START= to start the car
    STOP= To stop the car
    QUIT= to quit the game
                """)
        elif command.lower()=="quit":
            print("you have quit the game")
            break
else:
    print("i don`t understand")

