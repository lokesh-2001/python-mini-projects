import random
print("Good Luck! ")
words=['rainbow','computer','science','programming','python'
,'mathematics', 'player','condition','reverse','water','board','geeks']
word=random.choice(words)
print("\n\n", word ,"\n\n")
print("Guess the characters: ")
guesses=''
turns=12

while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1
    if failed == 0:
        print("YOU WON!!")
        print("the word is: ",word)
        break

    guess=input("guess a character: ")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("Wrong")
    if turns==0:
        print("YOU LOST!!")
