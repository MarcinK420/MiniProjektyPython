import random
import time
points = 0

def update_points():
    global points
    points += 1
    return points

def get_current_time():
    current_time = time.time()
    return current_time

def update_time(timeA, timeB):
    global time_difference
    time_difference = timeB - timeA
    return time_difference

def random_sentence():
    sentence = ""
    words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    for i in range(0, random.randint(1, 10)):
        random_word = random.choice(words)
        if i == 0:
            sentence = random_word
        else:
            sentence = sentence + " " + random_word
    return sentence

def typing_race():
    sentance = random_sentence()
    print(sentance)
    user_input = input("Type the sentance above: ")
    if user_input.lower() == sentance.lower():
        print("You typed the sentance correctly!")
        update_points()
    else:
        print("You typed the sentance incorrectly!")
    return points

def play_game():
    print("Welcome to the typing game!")
    print("Type the sentence below as fast as you can!")
    start = input("Press Y to start the game!")
    if start.lower() == "y":
        time1 = get_current_time()
        for i in range(0, 5):
            typing_race()
        time2 = get_current_time()
        update_time(time1, time2)

time_difference = 0

play_game()
print("You got", points, "points!")
print("You took", time_difference, "seconds to complete the game!")        

