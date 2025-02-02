import random

def random_number():
    """
    Generates a random number between 1 and 100 and returns it.

    Returns:
        int: The random number generated.
    """
    return random.randint(1, 100)

def guess_number():
    """
    Main game loop that prompts the user to guess the random number and provides feedback.
    """
    number = random_number()
    print("Zgadnij liczbę z zakresu od 1 do 100")
    liczba_prob = 0
    while True:
        try:
            guess = int(input("Enter a number: "))
        except ValueError:
            print("That's not a valid number. Please enter a valid integer.")
            continue
        liczba_prob += 1
        if guess < number:
            print("Za mało")
        elif guess > number:
            print("Za dużo")
        else:
            print("Zgadłeś!")
            break

    print("Liczba prób:", liczba_prob)

def main():
    """
    Main function that calls the guess_number function.
    """
    guess_number()

main()