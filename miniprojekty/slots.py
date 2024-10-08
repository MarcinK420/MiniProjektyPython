import random
saldo = 1000
#definicja funkcji depozyt zwracającej stawkę za którą chcemy zagrać
def depozyt():
    print("Za jaką stawkę chcesz zagrać?")
    stawka = input("1: 100, 2: 200, 3: 300, 4: 400, 5: 500 ")
    if stawka not in ["1", "2", "3", "4", "5"]:
        print("Niepoprawna wartość")
    else:
        stawka = int(stawka)*100
        return stawka
    
#definicja funkcji spin, która losuje symbole i sprawdza czy wygraliśmy

def spin(stawka):
    symbole = ["jabłko", "gruszka", "pomarańcza", "arbuz"]
    kolumna1 = random.choice(symbole)
    kolumna2 = random.choice(symbole)
    kolumna3 = random.choice(symbole)
    print(kolumna1, kolumna2, kolumna3)
    #sprawdzanie czy wygraliśmy, jeśli 3 takie same symbole to wygraliśmy razy 3, 
    # jeśli 2 takie same symbole to wygraliśmy razy 2, 
    # jeśli 3 różne symbole to przegraliśmy
    if kolumna1 == kolumna2 == kolumna3:
        print("Wygrałeś!")
        global saldo
        saldo += stawka*3
        print("Twój aktualny stan konta to: ", saldo)
    elif kolumna1 == kolumna2 or kolumna1 == kolumna3 or kolumna2 == kolumna3:
        print("Wygrałeś!")
        saldo += stawka*2
        print("Twój aktualny stan konta to: ", saldo)
    else:
        print("Przegrałeś!")
        saldo -= stawka
        print("Twój aktualny stan konta to: ", saldo)
#definicja funkcji gra, która pyta czy chcemy zagrać, jeśli tak to wywołuje 
# funkcję depozyt i funkcję spin
def gra():
    #pętla while, która pyta czy chcemy zagrać, 
    # jeśli nie to kończy grę
    while True:
        print("Czy chcesz zakrecić? T/N")
        zakrecic = input()
        #jeśli chcemy zagrać to wywołujemy funkcję depozyt
        # i funkcję spin
        if zakrecic == "T":
            stawka=depozyt()
            spin(stawka)
        #jeśli nie chcemy zagrać to kończymy grę
        # i wyświetlamy aktualny stan konta
        # i kończymy pętlę while
        else:
            print("Dziękujemy za grę")
            print("Twój aktualny stan konta to: ", saldo)
            break
#uruchomienie funkcji gra
gra()
