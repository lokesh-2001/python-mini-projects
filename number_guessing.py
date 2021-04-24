import random

play='y'
start=1
end=100
direction='N'
smallest=start
largest = end

while play=='y':
    smallest = start
    largest = end
    print("guess a number between 1 and 100: ")
    n= random.randint(start,end)
    print(n)
    count=0
    direction='N'
    while(direction!='C'):
        direction=input('enter that whether the number is it too Large(L), too Small(S) or Correct(C): ')
        if(direction=='S'):
            if(n>smallest):
                smallest=n+1
            n=random.randint(smallest,largest)
            print(n)

        if(direction=='L'):
            if(n<largest):
                smallest=n-1
            n=random.randint(smallest,largest)
            print(n)
        count=count+1
    print("You won! you guessed correctly in "+ str(count)+" turns.")
    print()
    play = input("Want to play again ? if yes type y and n for no: ")
