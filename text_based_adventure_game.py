import emoji
def start():
    print("\nYou are standing in a dark room.")
    print("There is a door to your left and right, which one do you take?")
    input1=input("type ('l' or 'left') or ('r' or 'right')\n>>>").lower()
    if (input1=="l" or input1=="left"):
        bear_room()
    elif(input1=="r" or input1=="right"):
        monster_room()
    else:
        game_over("Start taking typing classes!!\U0001F923")


def bear_room():
    print("\n\nYou entered in the bear room.")
    print("\n There is a bear hear, Behind the bear there is another door")
    print("bear is eating tasty honey!! what would you do? ")
    print("1). Take the honey.")
    print("2). Taunt the bear.")
    ans=int(input("type 1 or 2 \n>>>"))
    if (ans==1):
        game_over("The bear killed you!")
    elif(ans==2):
        print("\nYour good time, the bear moved from the door. You can go through it now!")
        diamond_room()
    else:
        game_over("Start taking typing classes!!\U0001F923")
 
def monster_room():
    print("\n\nYou entered monster room")
    print("the monster is sleeping.\nBehind the monster there is a door. What would you do?")
    print("1). Go through the door silently.")
    print("2). Kill the monster and show your courage.")
    ans=int(input("type 1 or 2 \n>>>"))
    if (ans==1):
        diamond_room()
    elif(ans==2):
        game_over("The monster was hungry, he ate you!")
    
    else:
        game_over("Start taking typing classes!!\U0001F923")


def diamond_room():
    print("\n\nYou entered a room filled with diamonds.")
    print("There is a door. What would you do?")
    print("1). Take some diamonds and go through the door.")
    print("2). Just go through the door.")
    ans=int(input("type 1 or 2 \n>>>"))
    if (ans==1):
        game_over("The diamonds were cursed! The moment you touched it, the building collapsed, you died!!")
    elif(ans==2):
        print("Congrats!! You are an honest man! YOU WON THE GAME!!!!!!!!")
        play_again()
    else:
        game_over("Start taking typing classes!!\U0001F923")


def game_over(reason):
    print("\n\n"+reason)
    print("YOU LOST GAME OVER!!")

    play_again()

def play_again():
    print("Do you want to play again type y or n")
    ans=input(">>>").lower()

    if ans=="y":
        start()
    else:
        exit()


start()