import random
points = 0

def updatePoints ():
    global points
    points += 1
    return points

def RandomSentance ():
    sentance = ""
    words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    for i in range(0, random.randint(1, 10)):
        random_word = random.choice(words)
        if i == 0:
            sentance = random_word
        else:
            sentance = sentance +" "+ random_word
    return sentance


def TypingRace ():
    sentance = RandomSentance()
    print(sentance)
    user_input = input("Type the sentance above: ")
    if user_input.lower() == sentance.lower():
        print("You typed the sentance correctly!")
        updatePoints()
    else:
        print("You typed the sentance incorrectly!")
    return points

def play():
    print("Welcome to the typing game!")
    print("Type the sentance below as fast as you can!")
    start = input("Press Y to start the game!")
    if start == "Y":
        for i in range(0, 5):
            points = TypingRace()

play()
print("You got", points, "points!")
        

