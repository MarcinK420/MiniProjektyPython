import datetime, random

def wygenerujUrodziny(liczbaUrodzin):
    urodzinyM = []
    for i in range(liczbaUrodzin):
        startRoku = datetime.date(2024, 1, 1)

        losowaIloscDni = datetime.timedelta(random.randint(0, 364))
        urodziny = startRoku + losowaIloscDni
        urodzinyM.append(urodziny)
    return urodzinyM

def znajdzPowiazanie(urodzinyM):
    if len(urodzinyM) == len(set(urodzinyM)):
        return None
    
    for a, urodzinyA in enumerate(urodzinyM):
        for b, urodzinyB in enumerate(urodzinyM[a + 1 :]):
            if urodzinyA == urodzinyB:
                return urodzinyA
            
MIESIACE = ('styczen', 'luty', 'marzec', 'kwiecien', 
            'maj', 'czerwiec', 'lipiec', 'sierpien', 
            'wrzesien', 'pazdziernik', 'listopad', 'grudzien')

while True:
    print('Ile mam wygenerowac urodzin? MAX 50!')
    odpowiedz = input('> ')
    if odpowiedz.isdecimal() and (0 < int(odpowiedz) <= 100):
        iloUro = int(odpowiedz)
        break
print()

print(f"Oto twoje wygenerowane {iloUro} urodziny:")
urodzinyM = wygenerujUrodziny(iloUro)
for i, urodziny in enumerate(urodzinyM):
    if i != 0:
        print(', ', end='')
    nazwaMiesiaca = MIESIACE[urodziny.month - 1]
    formatDaty = '{} {}'.format(nazwaMiesiaca, urodziny.day)
    print(formatDaty, end='')
print()
print()

powiazanie = znajdzPowiazanie(urodzinyM)

print('W tej symulacji, ', end='')
if powiazanie != None:
    nazwaMiesiaca = MIESIACE[powiazanie.month - 1]
    formatDaty = '{} {}'.format(nazwaMiesiaca, powiazanie.day)
    print("Pare ludzikow ma urodziny w", formatDaty)
else:
    print("Nie ma wspolnych urodzin WTF?!")
print()

print(f'Generujemy {iloUro} 100,000 razy.')
iloscPowiazan = 0
for i in range(100_000):
    if i % 1_000 == 0:
        print(f'{i} wykonanych symulacji...')
    urodzinyM = wygenerujUrodziny(iloUro)
    if znajdzPowiazanie(urodzinyM) != None:
        iloscPowiazan = iloscPowiazan + 1
print('Wykonano 100,000 symulacji.')

prawdopodobienstwo = round(iloscPowiazan / 100_000 * 100, 2)
print(f"W 100,000 symulacji {iloUro} urodzin, bylo {iloscPowiazan} powiazan.")
print(f"prawdopodobienstwo dla tylu dni wynioslo: {prawdopodobienstwo}")