import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2, 
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def deposit():
    while True:
        amount = input("Enter the amount to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive amount.")
        else:
            print("Invalid input. Please enter a valid amount.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid mumber of lines.")
        else:
            print("Invalid input. Please enter a valid number of lines.")

    return lines

def get_bet():
    while True:
        bet = input("Enter the amount to bet on each line: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Invalid input. Please enter a valid amount.")

    return bet

def spin_slots(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols += [symbol] * count

    if len(all_symbols) < rows * cols:
        raise ValueError("Not enough symbols to fill the slot machine.")

    random.shuffle(all_symbols)
    slots = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(all_symbols.pop())
        slots.append(row)

    return slots

def print_slots(slots):
    for row in slots:
        print(" | ".join(row))
    print()

def check_winnings(slots, bet, lines, symbol_values):
    winnings = 0
    for line in range(lines):
        if slots[0][line] == slots[1][line] == slots[2][line]:
            winnings += bet * symbol_values[slots[0][line]]
    return winnings

def game(balance):
    while True:
        print(f"Current balance: ${balance}")
        if balance <= 0:
            print("You have no balance left. Game over!")
            break

        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance to bet ${total_bet}.")
            continue
        print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")
        slots = spin_slots(ROWS, COLS, symbol_count)
        print_slots(slots)

        winnings = check_winnings(slots, bet, lines, symbol_value)
        print(f"You won ${winnings} this round.")
        balance += winnings - total_bet

        if winnings > 0:
            print(f"You won ${winnings}!")
        else:
            print("You did not win this round.")

def main():
    print("Welcome to the Slot Machine Game!")
    balance = deposit()
    
    try:
        game(balance)
    except ValueError as e:
        print(f"Error: {e}")
    


main()