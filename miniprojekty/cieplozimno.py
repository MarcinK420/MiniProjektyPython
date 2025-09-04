import random

ilosc_liczb = 3
ilosc_prob = 10

def main():
    print('''Witaj w mojej grze!

    Sprobuj zgadnac jaka unikalna, {}-cyfrowa liczbe mam na mysli.
    Bede dawac ci wskazowki:
    Cieplo - cyfra jest poprawna ale na zlym miejscu
    Goraco - cyfra jest poprawna i na dobrym miejscu.
    Zimno - nic nie jest poprawne.

    Na przyklad jesli zgadywana liczba to 248 a twoj strzal to 843, Wskazowki brzmialyby
    goraco, cieplo.'''.format(ilosc_liczb))

    while True:
        sekretnaLiczba = getSekretnaLiczba()
        print("Wymyslilem liczbe.")
        print(f"Masz {ilosc_prob} aby ja zgadnac.")

        nr_proby = 1
        while nr_proby <= ilosc_prob:
            proba = ''
            while len(proba) != ilosc_liczb or not proba.isdecimal():
                print(f"Proba #{nr_proby}: ")
                proba = input("> ")

            wskazowki = getWskazowki(proba, sekretnaLiczba)
            print(wskazowki)
            nr_proby += 1

            if proba == sekretnaLiczba:
                break
            if nr_proby > ilosc_prob:
                print("Skonczyly ci sie proby.")
                print(f"Poprawna odpowiedz to: {sekretnaLiczba}")
        print("Chcesz zagrac jeszcze raz? (tak lub nie)")
        if not input('> ').lower().startswith('t'):
            break
    print("Dzieki za zagranie w moja gre!")

def getSekretnaLiczba():
    liczby = list('0123456789')
    random.shuffle(liczby)

    sekretnaLiczba = ''
    for i in range(ilosc_liczb):
        sekretnaLiczba += str(liczby[i])

    return sekretnaLiczba

def getWskazowki(proba, sekretnaLiczba):
    if proba == sekretnaLiczba:
        return 'Brawo!!!'
    
    wskazowki = []

    for i in range(len(proba)):
        if proba[i] == sekretnaLiczba[i]:
            wskazowki.append('Goraco')
        elif proba[i] in sekretnaLiczba:
            wskazowki.append('Cieplo')
    if len(wskazowki) == 0:
        return 'Zimno'
    else:
        wskazowki.sort()
        return ' '.join(wskazowki)

if __name__ == '__main__':
    main()