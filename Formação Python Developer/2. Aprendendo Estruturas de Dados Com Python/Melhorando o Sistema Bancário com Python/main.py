def get_valid_input(prompt, validation_func, error_message): #Função que valida a entrada do usuário de acordo com a função de validação passada como parâmetro
    while True:                   
        user_input = input(prompt) #Pega o que foi digitado no terminal e atribui a variável
        if validation_func(user_input): #Se a função de validação passada retornar True, retorna a entrada do terminal
            return user_input
        else: #Caso o dado inserido não seja válido, irá retornar a mensagem de erro esspecificada na função de validação
            print(error_message)


def is_positive_number(value): #Função que valida se o dado inserido é um número positivo
    return value.isdigit() and int(value) > 0


def is_valid_float(value): #Função que valida se o dado inserido é um float válido
    try:
        float_value = float(value)
        return float_value >= 0 #Valida se o número é maior que 0, evitando depósitos "negativos"
    except ValueError:
        return False


def create_user(users, name, birth_date, cpf, address): #Função pra criar um usuário
    cpf = "".join(c for c in cpf if c.isdigit())  # Apenas os números do CPF
    if not any(user["cpf"] == cpf for user in users): #Valida se há algum cpf na lista de usários que seja identico ao cpf informado
        user = {"name": name, "birth_date": birth_date, "cpf": cpf, "address": address}
        users.append(user)
        return f"User {name} created successfully."
    else:
        return "User with the same CPF already exists."


def create_account(accounts, users, user_cpf):
    user = next((u for u in users if u["cpf"] == user_cpf), None)
    if user:
        account_number = len(accounts) + 1
        account = {
            "account_number": account_number,
            "user": user,
            "balance": 0,
            "agency": "0001",
            "amount_withdrawn": 0,
            "remaining_amount_withdrawal": 500,
            "daily_withdrawals": 0,
        }
        accounts.append(account)
        return f"Account {account_number} created successfully for user {user['name']}."
    else:
        return "User not found."


def list_accounts(accounts):
    header("List of Accounts")
    for account in accounts:
        print(f"Account Number: {account['account_number']}, User: {account['user']['name']}")
    print(lin())


def list_users(users):
    header("List of Users")
    for user in users:
        print(f"Name: {user['name']}, CPF: {user['cpf']}")
    print(lin())


def deactivate_account(accounts, account_number):
    account_index = next((i for i, acc in enumerate(accounts) if acc["account_number"] == account_number), None)
    if account_index is not None:
        del accounts[account_index]
        return f"Account {account_number} deactivated successfully."
    else:
        return f"Account {account_number} not found."


def deposit(account, amount, /):
    if amount > 0:
        account["balance"] += amount
        account.setdefault("transactions", []).append(f"Deposit of ${amount}. Current balance: ${account['balance']}")
        return (f"Deposit of ${amount} successful. Current balance: ${account['balance']}")
    else:
        return f"Invalid deposit amount."


def withdraw(*, account, amount):
    if amount > account["balance"]:
        return f"The withdrawal amount is greater than the balance!"

    elif account["daily_withdrawals"] >= 3:
        return f"Maximum of withdrawals reached!"

    elif amount + account["amount_withdrawn"] > account["remaining_amount_withdrawal"]:
        return f"The amount is greater than the max daily amount withdrawal! Amount available for withdrawal: ${account['remaining_amount_withdrawal'] - account['amount_withdrawn']}!"

    elif amount > 0:
        account["balance"] -= amount
        account["daily_withdrawals"] += 1
        account["amount_withdrawn"] += amount
        account.setdefault("transactions", []).append(f"Withdrawal of ${amount}. Current balance: ${account['balance']}")
        return f"Withdrawal of ${amount} successful. Current balance: ${account['balance']}"

    else:
        return f"Withdrawal cannot be processed."


def statement(account):
    header("Bank Statement")
    print(f"User: {account['user']['name']}")
    print(f"Current balance: ${account['balance']}")
    print(f"Daily Withdrwals: {account['daily_withdrawals']}/3")
    print(f"Amount available for withdrawal: ${account['remaining_amount_withdrawal']}")
    print(lin())
    return f"User: {account['user']['name']}, Current balance: ${account['balance']}"


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
        print("Please enter a valid option.")


def lin(tam=15):
    return "=-=" * tam


def header(txt):
    print(lin())
    print(txt.center(45))
    print(lin())


users_list = []
accounts_list = []

while True:
    opt = dash(
        [
            "Create User",
            "Create Checking Account",
            "List Accounts",
            "List Users",
            "Deactivate Account",
            "Account Deposit",
            "Checking Account Withdrawal",
            "Bank Statement",
            "Exit",
        ]
    )
    if opt == 9:
        header("Exiting...")
        break
    
    elif opt == 1:
        name = input("Enter user name: ")
        birth_date = input("Enter birth date: ")
        cpf = get_valid_input("Enter CPF: ", lambda x: x.isdigit() and len(x) == 11, "Invalid CPF. Must be 11 digits.")
        address = input("Enter address: ")
        print(create_user(users_list, name, birth_date, cpf, address))
    
    elif opt == 2:
        user_cpf = get_valid_input("Enter user CPF: ", lambda x: x.isdigit() and len(x) == 11, "Invalid CPF. Must be 11 digits.")
        print(create_account(accounts_list, users_list, user_cpf))
   
    elif opt == 3:
        list_accounts(accounts_list)
    
    elif opt == 4:
        list_users(users_list)
    
    elif opt == 5:
        account_number = int(get_valid_input("Enter account number to deactivate: ", is_positive_number, "Invalid account number."))
        print(deactivate_account(accounts_list, account_number))
    
    elif opt == 6:
        user_name = input("Enter user name: ")
        account_number = int(get_valid_input("Enter account number: ", is_positive_number, "Invalid account number."))
        amount = float(get_valid_input("Please specify the amount to be deposited: ", is_valid_float, "Invalid deposit amount."))
        account = next((acc for acc in accounts_list if acc["user"]["name"] == user_name and acc["account_number"] == account_number), None)
        if account:
            print(deposit(account, amount))
        else:
            print("Account not found.")
   
    elif opt == 7:
        user_name = input("Enter user name: ")
        account_number = int(get_valid_input("Enter account number: ", is_positive_number, "Invalid account number."))
        amount = float(get_valid_input("Please specify the amount to be withdrawn: ", is_valid_float, "Invalid withdrawal amount.",))
        account = next((acc for acc in accounts_list if acc["user"]["name"] == user_name and acc["account_number"] == account_number), None)
        if account:
            print(withdraw(account=account, amount=amount))
        else:
            print("Account not found.")
   
    elif opt == 8:
        user_name = input("Enter user name: ")
        account_number = int(get_valid_input("Enter account number: ", is_positive_number, "Invalid account number."))
        account = next((acc for acc in accounts_list if acc["user"]["name"] == user_name and acc["account_number"] == account_number), None)
        if account:
            print(statement(account))
        else:
            print("Account not found.")
