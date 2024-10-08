from datetime import datetime

lista = []
# Try to open the file, if it doesn't exist, create a new file
try:
    with open('zadania.txt', 'r') as file:
        lista = file.read().splitlines()
except FileNotFoundError:
    print("Plik zadania.txt nie istnieje. Zostanie utworzony nowy plik.")

# Function to save tasks to the file in chronological order
def save_tasks():
    sorted_tasks = sorted(lista, key=lambda x: datetime.strptime(x.split(" - ")[1], "%d.%m.%Y"))
    with open('zadania.txt', 'w') as file:
        for task in sorted_tasks:
            file.write(task + '\n')

# Declaring an add function
# It asks the user for a task and a date
# And appends the task to the list
def add():
    task = input("Dodaj zadanie: ")
    date = input("Podaj datę zadania (dd.mm.yyyy): ")
    lista.append("[]" + task + " - " + date)
    save_tasks()

# Declaring a view function
# It prints all tasks from the list
# And asks the user what to do next
def view():
    sorted_tasks = sorted(lista, key=lambda x: datetime.strptime(x.split(" - ")[1], "%d.%m.%Y"))
    for i in range(len(sorted_tasks)):
        print(i+1, sorted_tasks[i])
    while True:
        print("Co chcesz zrobić? Usunąć zadanie (U), oznaczyć zadanie jako zakończone (E) czy wrócić do menu (M)?")
        choice = input().upper()
        if choice == "U":
            deletetask()
        elif choice == "E":
            endtask()
        elif choice == "M":
            break
        else:
            print("Niepoprawna wartość")

# Declaring an endtask function, which marks a task as done
# And saves the changes to the file
# It iterates over the list and replaces the first occurrence of "[]"
def endtask():
    try:
        task = int(input("Które zadanie chcesz oznaczyć jako zakończone? Wpisz numer zadania: "))
        if 0 < task <= len(lista):
            if lista[task-1].startswith("[]"):
                lista[task-1] = lista[task-1].replace("[]", "[x]", 1)  # Replace only the first occurrence of "[]"
                save_tasks()
                print("Zadanie zostało oznaczone jako zakończone.")
            else:
                print("Zadanie jest już oznaczone jako zakończone.")
        else:
            print("Niepoprawny numer zadania.")
    except ValueError:
        print("Niepoprawna wartość. Podaj numer zadania.")

# Declaring a deletetask function, which deletes a task
# And saves the changes to the file
# It uses the pop method to remove the task from the list
def deletetask():
    try:
        task = int(input("Które zadanie chcesz usunąć? Wpisz numer zadania: "))
        if 0 < task <= len(lista):
            lista.pop(task-1)
            save_tasks()
            print("Zadanie zostało usunięte.")
        else:
            print("Niepoprawny numer zadania.")
    except ValueError:
        print("Niepoprawna wartość. Podaj numer zadania.")

# Main loop, which asks the user what to do
# And calls the appropriate function
# It breaks the loop if the user chooses to quit
while True:
    print("Co chcesz zrobić? Dodać zadanie (D), zobaczyć zadania (Z), zakończyć (Q)")
    choice = input().upper()
    if choice == "D":
        add()
    elif choice == "Z":
        view()
    elif choice == "Q":
        break
    else:
        print("Niepoprawna wartość")