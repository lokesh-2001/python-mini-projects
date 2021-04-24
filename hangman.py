import random
import time

print("Welcome to the game. The game will start within few seconds.\nAre you ready?")
time.sleep(5)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess=["january","border","image","file","promise","kids","lungs","doll","rhyme","damage","plants"]
    word=random.choice(words_to_guess)
    print("\n\nTHE WORD TO GUESS IS "+word+"\n\n")
    print(" the length of word is "+str(len(word)))
    length=len(word)
    count=0
    display='_'*length
    already_guessed=[]
    play_game=""

def play_loop():
    global play_game
    play_game=input("Do you want to play again enter y or n\n\n>>>")
    while play_game not in ["y","n","Y","N"]:
        play_game=input("Do you want to play again enter y or n\n\n>>>")

    if (play_game=="y" or play_game=="Y"):
        main()
    else:
        print("Thanks for playing!!")
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit =5
    guess=input("The word is "+display+ "\n\n Enter your choice\n\n>>>")
    guess=guess.strip()
    if(len(guess.strip())==0 or len(guess.strip())>=2 or guess<="9"):
        print("invalid input")
        hangman()
    elif(guess in word):
        already_guessed.extend([guess])
        index=word.find(guess)
        word=word[:index]+"_"+word[index+1:]
        display=display[:index]+guess+display[index + 1:]
        #print(display)
    elif guess in already_guessed:
        print("Try another letter")
    else:
        count+=1
        if(count==1):
            time.sleep(1)
            print("  ________  ")
            print(" |          ")
            print(" |          ")
            print(" |          ")
            print(" |          ")
            print(" |          ")
            print(" |          ")
            print(" |          ")
            print("_|_         ")
            print("\nWrong Guess!!!\n"+"guess remaining: "+str(limit-count))

        elif(count==2):
            time.sleep(1)
            print("  ________  ")
            print(" |        | ")
            print(" |        | ")
            print(" |          ")
            print(" |          ")
            print(" |          ")
            print(" |          ")
            print(" |          ")
            print("_|_         ")
            print("\nWrong Guess!!!\n"+"guess remaining: "+str(limit-count))

        elif(count==3):
            time.sleep(1)
            print("  ________  ")
            print(" |        | ")
            print(" |        | ")
            print(" |        | ")
            print(" |        O ")
            print(" |          ")
            print(" |          ")
            print(" |          ")
            print("_|_         ")
            print("\nWrong Guess!!!\n"+"guess remaining: "+str(limit-count))


        elif(count==4):
            time.sleep(1)
            print("  ________  ")
            print(" |        | ")
            print(" |        | ")
            print(" |        | ")
            print(" |        O ")
            print(" |       /|\\")
            print(" |          ")
            print(" |          ")
            print("_|_         ")
            print("\nWrong Guess!!!\n"+"guess remaining: "+str(limit-count))


        elif(count==5):
            time.sleep(1)
            print("  ________  ")
            print(" |        | ")
            print(" |        | ")
            print(" |        | ")
            print(" |        O ")
            print(" |       /|\\")
            print(" |       / \\")
            print(" |          ")
            print("_|_         ")
            print("\nWrong Guess!!!\n"+"guess remaining: "+str(limit-count))

            print("\n\n\nGame Over!!!!Game Over!!!!")
            print("the word was: ",already_guessed,word)
            play_loop()

    if(word=="_"*length):
        print("You have guessed the word correctly!!")
        play_loop()
        
    elif count!= limit:
        hangman()
main()
hangman()