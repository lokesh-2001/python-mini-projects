import random
class qa:
    # constructor
    def __init__(self,question,correct_answer,other_answer):
        self.question=question
        self.corr_ans=correct_answer
        self.other_ans=other_answer
    
li=[qa("Where is Minsk?","in Belarus",["in Russia","such a city does not exist"]),
qa("What is the capital of Australia?","Canberra",["Sydney","New York","Australia does not exist"]),
qa("which of the following does not exit on Earth?","Sea of Tranquility",["Mediterranean Sea","Baltic Sea","North Sea"]),
qa("Which of the following is not a continent?","Arctica",["America","Asia","Antartica"]),
qa("Which of the following is not an African country?","Malaysia",["Madagascar","Djibouti","South Africa","Zimbabwe"])]


score=0
random.shuffle(li)
for qaItem in li:
    print(qaItem.question)
    print("Possible answers are: ")
    possible= qaItem.other_ans+[qaItem.corr_ans]
    random.shuffle(possible)
    count=0
    while count<len(possible):
        print(str(count+1)+":"+possible[count])
        count+=1
    print("enter the number of your answer: ")
    ans=input()
    while not ans.isdigit():
        print("Thats not a number. Please enter the number of your answer: ")
        ans=input()
    ans=int(ans)
    while not (ans>0 and ans<=len(possible)):
        print("That number doesn't correspond to any answer. Please enter the number of your answer")
        ans=int(input())
    if possible[ans-1]==qaItem.corr_ans:
        print("Correct!!")
        score+=10
    else:
        print("Your answer was wrong")
        score-=5
        print("Correct ans was: ",qaItem.corr_ans)
    print('\n\n')


print("You scored "+str(score))