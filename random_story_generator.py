import random
starter=['About 100 years ago', 'In the 20 BC','Once upon a time']

character1=[' there lived a king.',' there was a man named jacob.','there lived a farmer.']

time=[' One day',' One full-moon night']

story=[' he was passing by',' he was going for a picnic to ']

place=[' the mountains',' the garden']

character2=[' he saw a man',' he saw a young lady']

age=[' who seemed to be in late 20s',' who seemed very old and feeble']

work=[' searching something.', ' digging a well on roadside.']

print(random.choice(starter)+random.choice(character1)+random.choice(time)+random.choice(story)+random.choice(place)+random.choice(character2)+random.choice(age)+random.choice(work))
