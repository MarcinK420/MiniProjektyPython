# MiniProjektyPython
Zbiór pomniejszych projektów w pythonie, bez szału.
# Slot Machine Game

This is a simple slot machine game simulation written in Python. The player starts with an initial balance and can place bets to spin the reels. Based on the outcome of the spin, the player either wins or loses the amount staked.

## Table of Contents

1. [How to Play](#how-to-play)
2. [Functions](#functions)
   - [depozyt()](#depozyt)
   - [spin(stawka)](#spinstawka)
   - [gra()](#gra)
3. [Game Logic](#game-logic)

---

## How to Play

1. When the game starts, the player is prompted to decide whether they want to spin the reels.
2. If the player agrees, they are asked to select a stake amount from a predefined list (100, 200, 300, 400, or 500).
3. The slot machine then spins three reels, each displaying one of four symbols: "jabłko" (apple), "gruszka" (pear), "pomarańcza" (orange), or "arbuz" (watermelon).
4. Depending on the combination of symbols, the player either wins a prize or loses the staked amount. If all three symbols match, the player wins 3x their stake. If two symbols match, the player wins 2x their stake. If none match, they lose the stake.

---

## Functions

### `depozyt()`

**Description**:  
This function prompts the user to enter the amount they wish to stake in the game. The user is presented with a choice between five different stakes (100, 200, 300, 400, or 500). If the user enters an invalid value, an error message is displayed.

**Returns**:  
- An integer value representing the chosen stake amount.

---

### `spin(stawka)`

**Arguments**:  
- `stawka (int)`: The amount staked for the spin.

**Description**:  
This function simulates a spin of the slot machine. Three random symbols are chosen from the list `["jabłko", "gruszka", "pomarańcza", "arbuz"]`. The player's balance is updated based on the result of the spin:
- If all three symbols match, the player wins 3x their stake.
- If two symbols match, the player wins 2x their stake.
- If no symbols match, the player loses their stake.

**Global Variable**:  
- `saldo`: The player's current balance, updated based on the result of the spin.

---

### `gra()`

**Description**:  
This is the main loop of the game. It repeatedly asks the player if they want to spin the slot machine:
- If the player chooses to play, they are prompted to enter their stake and the game proceeds with a spin.
- If the player chooses not to play, the game ends and the player's final balance is displayed.

---

## Game Logic

1. The player starts with an initial balance of 1000.
2. For each spin:
   - The player selects a stake from 100 to 500.
   - Three symbols are randomly chosen.
   - Depending on the outcome, the player's balance is updated.
3. The game continues until the player decides to quit.

---

## Example

```bash
Czy chcesz zakrecić? T/N
T
Za jaką stawkę chcesz zagrać?
1: 100, 2: 200, 3: 300, 4: 400, 5: 500 
1
jabłko gruszka arbuz
Przegrałeś!
Twój aktualny stan konta to: 900
Czy chcesz zakrecić? T/N
N
Dziękujemy za grę
Twój aktualny stan konta to: 900
```

---

Feel free to clone the repository and enjoy the game!

# Task Manager in Python

This is a simple command-line task manager written in Python. The user can add tasks, view tasks sorted by date, mark them as completed, or delete them. Tasks are saved in a file called `zadania.txt` and loaded every time the program is run.

## Table of Contents

1. [How It Works](#how-it-works)
2. [Features](#features)
3. [File Structure](#file-structure)
4. [Functions](#functions)
   - [save_tasks()](#save_tasks)
   - [add()](#add)
   - [view()](#view)
   - [endtask()](#endtask)
   - [deletetask()](#deletetask)
5. [Usage](#usage)

---

## How It Works

The task manager performs the following operations:
- **Load tasks**: Upon start, the program attempts to load tasks from `zadania.txt`. If the file does not exist, it creates a new one.
- **Manage tasks**: Users can add new tasks, view all tasks sorted by date, mark tasks as completed, or delete tasks.
- **Save tasks**: After each operation, tasks are saved back to `zadania.txt`.

---

## Features

- **Task addition**: Add tasks with specific deadlines (in the format `dd.mm.yyyy`).
- **Task completion**: Mark tasks as completed, which is visually indicated by changing `[]` to `[x]`.
- **Task deletion**: Remove tasks that are no longer needed.
- **Automatic sorting**: Tasks are sorted by their due dates.
- **Persistent storage**: Tasks are saved to `zadania.txt` and are loaded when the program is run again.

---

## File Structure

- **zadania.txt**: The file that stores tasks in the format `[] Task - dd.mm.yyyy`. Tasks are sorted by their date and saved to this file after every modification.

---

## Functions

### `save_tasks()`

**Description**:  
Saves the list of tasks to `zadania.txt`, sorting them chronologically by date.

**Operation**:  
- Reads the tasks from `lista`.
- Sorts the tasks by their due date.
- Writes the sorted tasks back to `zadania.txt`.

---

### `add()`

**Description**:  
Allows the user to add a new task to the list. The user is prompted to provide the task description and a due date. The task is added to `lista` and then saved.

---

### `view()`

**Description**:  
Displays all tasks in chronological order. After viewing, the user is prompted to either delete a task, mark a task as completed, or return to the main menu.

---

### `endtask()`

**Description**:  
Allows the user to mark a task as completed. The user selects a task by its number, and the program updates the task by replacing `[]` with `[x]`. The task list is then saved.

---

### `deletetask()`

**Description**:  
Allows the user to delete a task by selecting its number. The task is removed from `lista`, and the updated list is saved.

---

## Usage

1. Run the program from the command line.
2. You will be prompted to choose between the following actions:
   - **D**: Add a task.
   - **Z**: View all tasks, where you can also mark tasks as completed or delete them.
   - **Q**: Quit the program.
3. When adding a task, you will be prompted to provide a task description and a due date in the format `dd.mm.yyyy`.
4. Tasks are automatically saved to `zadania.txt` and will persist between program runs.

### Example

```bash
Co chcesz zrobić? Dodać zadanie (D), zobaczyć zadania (Z), zakończyć (Q)
D
Dodaj zadanie: Napisać raport
Podaj datę zadania (dd.mm.yyyy): 12.10.2024
Zadanie zostało dodane.

Co chcesz zrobić? Dodać zadanie (D), zobaczyć zadania (Z), zakończyć (Q)
Z
1 [] Napisać raport - 12.10.2024

Co chcesz zrobić? Usunąć zadanie (U), oznaczyć zadanie jako zakończone (E) czy wrócić do menu (M)?
E
Które zadanie chcesz oznaczyć jako zakończone? Wpisz numer zadania: 1
Zadanie zostało oznaczone jako zakończone.

Co chcesz zrobić? Dodać zadanie (D), zobaczyć zadania (Z), zakończyć (Q)
Q
```

Tasks are stored in the following format in the `zadania.txt` file:

```
[] Napisać raport - 12.10.2024
[x] Zrobić zakupy - 09.10.2024
```

---

Feel free to clone this project and use it to manage your tasks!
