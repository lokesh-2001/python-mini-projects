import random
print("ROCK PAPER SCISSOR")

win=0 
loss=0 
tie=0
print(f"Win: {win} Loss: {loss} Tie: {tie}")
print("""Enter Your Move:
        r-rock
        p-paper
        s-scissor
        q=quit""")

while True:
    move=input("\n>>>")
    if(move=="score"):
        print(f"Win: {win} Loss: {loss} Tie: {tie}")
    elif(move=='p' or move=='r' or move=='s' or move=='q'):
        if move=='q':
            print(f"Win: {win} Loss: {loss} Tie: {tie}")
            exit()
        no=random.randint(1,3)
        if no==1:
                com='r'
                print("Rock")
        elif no==2:
                com='p'
                print("Paper")
        elif no==3:
                com='s'
                print("scissor")
    

        if move==com:
            print("TIE!!")
            tie+=1
        elif move=='r' and com=='s':
            print("YOU WON!!")
            win+=1
        elif move=='p' and com=='r':
            print("YOU WON!!")
            win+=1
        elif move=='s' and com=='p':
            print("YOU WON!!")
            win+=1
        elif move=='s' and com=='r':
            print("YOU LOST!!")
            loss+=1
        elif move=='r' and com=='p':
            print("YOU LOST!!")
            loss+=1
        elif move=='p' and com=='s':
            print("YOU LOST!!")
            loss+=1
    
    else:
        print("Enter correct move: ")
"""        
            move=input("Enter Your Move:
            r-rock
            p-paper
            s-scissor
            q=quit\n\n>>>")
"""
    
    