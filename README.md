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
