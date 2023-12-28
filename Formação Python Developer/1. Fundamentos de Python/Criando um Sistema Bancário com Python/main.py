def lin(tam=15):
    return "=-=" * tam


def header(txt):
    print(lin())
    print(txt.center(45))
    print(lin())


def dash(options):
    while True:
        header("Sperb - Systems")
        o = 1
        for i in options:
            print(f"{o} - {i}")
            o += 1
        print(lin())
        opt = input("Choose an option: ")
        print(lin())
        if opt.isdigit():
            opt = int(opt)
            if 1 <= opt <= len(options):
                return opt
        print("Please enter a valid option!")


balance = 0
withdrawals_made = 0
daily_withdrawal_limit = 3
max_withdrawal_amount = 500
transaction_history = []


def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        transaction_history.append(f"Deposit: +{amount}")
        return f"Deposit of ${amount} successful."
    else:
        return "Invalid deposit amount."


def withdraw():
    global balance, withdrawals_made
    amount = float(input("Please specify the amount to be withdrawn: "))
    if (
        withdrawals_made < daily_withdrawal_limit
        and amount <= max_withdrawal_amount
        and amount <= balance
    ):
        balance -= amount
        withdrawals_made += 1
        transaction_history.append(f"Withdrawal: -{amount}")
        return f"Withdrawal of ${amount} successful."
    else:
        return "Withdrawal cannot be processed. Check the daily limit, withdrawal amount, or balance."


def view_statement():
    global balance
    header("Bank Statement")
    print(f"Current balance: ${balance}")
    print("Transaction history:")
    for transaction in transaction_history:
        print(transaction)
    print(lin())


while True:
    opt = dash(
        ["Account Deposit", "Checking Account Withdrawal", "Bank Statement", "Exit"]
    )
    if opt == 4:
        header("Exiting...")
        break
    elif opt == 1:
        amo = float(input("Please specify the amount to be deposited: "))
        print(deposit(amo))
    elif opt == 2:
        print(withdraw())
    elif opt == 3:
        view_statement()
