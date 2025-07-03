MAX_LINES = 3

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

def get_number_of_lines()
while True:
        lines = input("Enter the number of lines to bet on (1-+" + str(MAX_LINES) + ")? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive amount.")
        else:
            print("Invalid input. Please enter a valid amount.")

    return amount
def main()
    balance = deposit()


main()