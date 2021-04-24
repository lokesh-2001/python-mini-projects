import random
play='y'
while(play=='y'):
    ans=random.randint(1,100)
    print(str(ans))
    print("You have 5 turns to win the game")
    n=int(input("enter a number between 1 and 100: "))
    count=1
    while(ans!=n):
        if(n>ans):
            print("You have entered a number greater than the ans")
        elif(n<ans):
            print("You have entered a number smaller than the ans")
        print("left turns: "+ str(5-count))
        n=int(input("enter the number again: "))

        count+=1
        if(count>=5):
            print ("You lost ")
            quit()
    print("You won! you guessed correctly in "+ str(count)+" turns.")
    print()
    play = input("Want to play again ? if yes type y and n for no: ")