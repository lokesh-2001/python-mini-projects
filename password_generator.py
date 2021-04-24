import random

def shuffle(string):
    temp=list(string)
    random.shuffle(temp)
    return ''.join(temp)

letter1=chr(random.randint(65,90))
letter2=chr(random.randint(65,90))
letter3=chr(random.randint(65,90))
letter4=chr(random.randint(65,90))
letter5=chr(random.randint(65,90))
letter6=chr(random.randint(65,90))
letter7=chr(random.randint(65,90))
letter8=chr(random.randint(65,90))

password=letter1+letter2+letter3+letter4+letter5+letter6+letter7+letter8

print(shuffle(password))

