from datetime import datetime

# List to store tasks
lista = []
# Try to open the file, if it doesn't exist, create a new file
try:
    with open('zadania.txt', 'r') as file:
        lista = file.read().splitlines()
except FileNotFoundError:
    print("Plik zadania.txt nie istnieje. Zostanie utworzony nowy plik.")

def save_tasks():
    """
    Save tasks to the file in chronological order.
    """
    sorted_tasks = sorted(lista, key=lambda x: datetime.strptime(x.split(" - ")[1], "%d.%m.%Y"))
    with open('zadania.txt', 'w') as file:
        for task in sorted_tasks:
            file.write(task + '\n')

def add():
    """
    Add a new task to the list.
    Prompts the user for a task and a date, then appends the task to the list and saves it.
    """
    task = input("Dodaj zadanie: ")
    date = input("Podaj datę zadania (dd.mm.yyyy): ")
    lista.append("[]" + task + " - " + date)
    save_tasks()

def view():
    """
    View all tasks in the list.
    Prints all tasks sorted by date and prompts the user for further actions.
    """
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

def endtask():
    """
    Mark a task as done.
    Prompts the user for the task number, marks it as done, and saves the changes.
    """
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

def deletetask():
    """
    Delete a task from the list.
    Prompts the user for the task number, deletes it from the list, and saves the changes.
    """
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