import random

# Initial balance
saldo = 1000

def depozyt():
    """
    Prompts the user to enter a stake amount and returns the corresponding value.

    Returns:
        int: The stake amount chosen by the user.
    """
    print("Za jaką stawkę chcesz zagrać?")
    stawka = input("1: 100, 2: 200, 3: 300, 4: 400, 5: 500 ")
    if stawka not in ["1", "2", "3", "4", "5"]:
        print("Niepoprawna wartość")
    else:
        stawka = int(stawka) * 100
        return stawka

def spin(stawka):
    """
    Simulates a slot machine spin, checks the result, and updates the balance.

    Args:
        stawka (int): The stake amount for the spin.
    """
    symbole = ["jabłko", "gruszka", "pomarańcza", "arbuz"]
    kolumna1 = random.choice(symbole)
    kolumna2 = random.choice(symbole)
    kolumna3 = random.choice(symbole)
    print(kolumna1, kolumna2, kolumna3)

    global saldo
    if kolumna1 == kolumna2 == kolumna3:
        print("Wygrałeś!")
        saldo += stawka * 3
        print("Twój aktualny stan konta to: ", saldo)
    elif kolumna1 == kolumna2 or kolumna1 == kolumna3 or kolumna2 == kolumna3:
        print("Wygrałeś!")
        saldo += stawka * 2
        print("Twój aktualny stan konta to: ", saldo)
    else:
        print("Przegrałeś!")
        saldo -= stawka
        print("Twój aktualny stan konta to: ", saldo)

def gra():
    """
    Main game loop that asks the user if they want to play, and if so,
    calls the depozyt and spin functions. Ends the game if the user chooses not to play.
    """
    while True:
        print("Czy chcesz zakrecić? T/N")
        zakrecic = input()
        if zakrecic == "T":
            stawka = depozyt()
            spin(stawka)
        else:
            print("Dziękujemy za grę")
            print("Twój aktualny stan konta to: ", saldo)
            break

# Start the game
gra()