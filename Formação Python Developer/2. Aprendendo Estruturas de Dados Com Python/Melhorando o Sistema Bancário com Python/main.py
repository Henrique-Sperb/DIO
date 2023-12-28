def get_valid_input(prompt, validation_func, error_message):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print(error_message)
    """
    Solicita uma entrada ao usuário e valida-a de acordo com a função de validação fornecida.

    Parâmetros:
    - prompt (str): Mensagem para solicitar a entrada.
    - validation_func (function): Função de validação que retorna True se a entrada é válida, False caso contrário.
    - error_message (str): Mensagem a ser exibida em caso de entrada inválida.

    Retorna:
    - user_input (str): Entrada do usuário válida.
    """

def is_positive_number(value):
    return value.isdigit() and int(value) > 0
    """
    Verifica se o valor é um número positivo.

    Parâmetros:
    - value (str): Valor a ser verificado.

    Retorna:
    - bool: True se for um número positivo, False caso contrário.
    """"""
    Verifica se o valor é um número positivo.

    Parâmetros:
    - value (str): Valor a ser verificado.

    Retorna:
    - bool: True se for um número positivo, False caso contrário.
    """


def is_valid_float(value):
    try:
        float_value = float(value)
        return float_value >= 0
    except ValueError:
        return False
    """
    Verifica se o valor é um float não negativo.

    Parâmetros:
    - value (str): Valor a ser verificado.

    Retorna:
    - bool: True se for um float não negativo, False caso contrário.
    """


def create_user(users, name, birth_date, cpf, address):
    cpf = "".join(c for c in cpf if c.isdigit())  # Apenas os números do CPF
    if not any(user["cpf"] == cpf for user in users):
        user = {"name": name, "birth_date": birth_date, "cpf": cpf, "address": address}
        users.append(user)
        return f"User {name} created successfully."
    else:
        return "User with the same CPF already exists."
    """
    Cria um novo usuário e adiciona-o à lista de usuários, se o CPF ainda não estiver em uso.

    Parâmetros:
    - users (list): Lista de usuários existentes.
    - name (str): Nome do novo usuário.
    - birth_date (str): Data de nascimento do novo usuário.
    - cpf (str): CPF do novo usuário.
    - address (str): Endereço do novo usuário.

    Retorna:
    - str: Mensagem indicando se o usuário foi criado com sucesso ou se já existe um usuário com o mesmo CPF.
    """


def create_account(accounts, users, user_cpf):
    user = next((u for u in users if u["cpf"] == user_cpf), None)
    if user:
        account_number = len(accounts) + 1
        account = {"account_number": account_number, "user": user, "balance": 0}
        accounts.append(account)
        return f"Account {account_number} created successfully for user {user['name']}."
    else:
        return "User not found."
    """
    Cria uma nova conta vinculada a um usuário existente.

    Parâmetros:
    - accounts (list): Lista de contas existentes.
    - users (list): Lista de usuários existentes.
    - user_cpf (str): CPF do usuário ao qual a nova conta será vinculada.

    Retorna:
    - str: Mensagem indicando se a conta foi criada com sucesso ou se o usuário não foi encontrado.
    """


def list_accounts(accounts):
    header("List of Accounts")
    for account in accounts:
        print(f"Account Number: {account['account_number']}, User: {account['user']['name']}")
    print(lin())
    """
    Exibe uma lista de todas as contas existentes.

    Parâmetros:
    - accounts (list): Lista de contas existentes.
    """"""
    Exibe uma lista de todas as contas existentes.

    Parâmetros:
    - accounts (list): Lista de contas existentes.
    """


def list_users(users):
    header("List of Users")
    for user in users:
        print(f"Name: {user['name']}, CPF: {user['cpf']}")
    print(lin())
    """
    Exibe uma lista de todos os usuários existentes.

    Parâmetros:
    - users (list): Lista de usuários existentes.
    """


def deactivate_account(accounts, account_number):
    account_index = next((i for i, acc in enumerate(accounts) if acc['account_number'] == account_number), None)
    if account_index is not None:
        del accounts[account_index]
        return f"Account {account_number} deactivated successfully."
    else:
        return f"Account {account_number} not found."
    """
    Desativa uma conta com base no número da conta.

    Parâmetros:
    - accounts (list): Lista de contas existentes.
    - account_number (int): Número da conta a ser desativada.

    Retorna:
    - str: Mensagem indicando se a conta foi desativada com sucesso ou se a conta não foi encontrada.
    """


def deposit(account, amount):
    if amount > 0:
        account['balance'] += amount
        return f"Deposit of ${amount} successful. Current balance: ${account['balance']}"
    else:
        return "Invalid deposit amount."
    """
    Realiza um depósito em uma conta.

    Parâmetros:
    - account (dict): Dicionário representando a conta.
    - amount (float): Valor a ser depositado.

    Retorna:
    - str: Mensagem indicando se o depósito foi bem-sucedido ou se o valor do depósito é inválido.
    """


def withdraw(account, amount):
    if (
        amount > 0
        and amount <= account['balance']
    ):
        account['balance'] -= amount
        return f"Withdrawal of ${amount} successful. Current balance: ${account['balance']}"
    else:
        return "Withdrawal cannot be processed. Check the withdrawal amount or balance."
    """
    Realiza um saque de uma conta.

    Parâmetros:
    - account (dict): Dicionário representando a conta.
    - amount (float): Valor a ser sacado.

    Retorna:
    - str: Mensagem indicando se o saque foi bem-sucedido ou se o valor do saque é inválido.
    """


def statement(account):
    header("Bank Statement")
    print(f"User: {account['user']['name']}")
    print(f"Current balance: ${account['balance']}")
    print(lin())
    return f"User: {account['user']['name']}, Current balance: ${account['balance']}"
    """
    Exibe o extrato bancário de uma conta.

    Parâmetros:
    - account (dict): Dicionário representando a conta.

    Retorna:
    - str: Mensagem contendo o extrato bancário.
    """


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
    """
    Exibe um menu interativo e solicita ao usuário que escolha uma opção.

    Parâmetros:
    - options (list): Lista de opções disponíveis.

    Retorna:
    - int: Opção escolhida pelo usuário.
    """


def lin(tam=15):
    return "=-=" * tam
    """
    Retorna uma linha decorativa para melhorar a apresentação na interface do usuário.

    Parâmetros:
    - tam (int): Tamanho da linha (número de repetições).

    Retorna:
    - str: Linha decorativa.
    """


def header(txt):
    print(lin())
    print(txt.center(45))
    print(lin())
    """
    Exibe um cabeçalho decorativo para melhorar a apresentação na interface do usuário.

    Parâmetros:
    - txt (str): Texto a ser exibido no cabeçalho.
    """"""
    Exibe um cabeçalho decorativo para melhorar a apresentação na interface do usuário.

    Parâmetros:
    - txt (str): Texto a ser exibido no cabeçalho.
    """


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
        account = next((acc for acc in accounts_list if acc['user']['name'] == user_name and acc['account_number'] == account_number), None)
        if account:
            print(deposit(account, amount))
        else:
            print("Account not found.")
    elif opt == 7:
        user_name = input("Enter user name: ")
        account_number = int(get_valid_input("Enter account number: ", is_positive_number, "Invalid account number."))
        amount = float(get_valid_input("Please specify the amount to be withdrawn: ", is_valid_float, "Invalid withdrawal amount."))
        account = next((acc for acc in accounts_list if acc['user']['name'] == user_name and acc['account_number'] == account_number), None)
        if account:
            print(withdraw(account, amount))
        else:
            print("Account not found.")
    elif opt == 8:
        user_name = input("Enter user name: ")
        account_number = int(get_valid_input("Enter account number: ", is_positive_number, "Invalid account number."))
        account = next((acc for acc in accounts_list if acc['user']['name'] == user_name and acc['account_number'] == account_number), None)
        if account:
            statement(account)
        else:
            print("Account not found.")
    """"
    Loop Principal:

    Descrição: Este é o loop principal do programa que permite ao usuário interagir com o sistema bancário.
    Entrada: As opções do usuário para criar usuários, contas, listar contas, listar usuários, desativar contas, fazer depósitos, fazer saques, visualizar extratos ou sair do programa.
    Saída: Execução das funções correspondentes com base na escolha do usuário.
    
    Opções do Usuário:

    1: Criar Usuário
        Solicita informações do usuário (nome, data de nascimento, CPF, endereço).
        Chama a função create_user para criar um novo usuário.
    2: Criar Conta Corrente
        Solicita o CPF do usuário.
        Chama a função create_account para criar uma nova conta vinculada ao usuário.
    3: Listar Contas
        Chama a função list_accounts para exibir informações sobre todas as contas.
    4: Listar Usuários
        Chama a função list_users para exibir informações sobre todos os usuários.
    5: Desativar Conta
        Solicita o número da conta a ser desativada.
        Chama a função deactivate_account para desativar a conta.
    6: Depósito em Conta
        Solicita o nome do usuário, número da conta e valor a ser depositado.
        Chama a função deposit para realizar o depósito.
    7: Saque em Conta
        Solicita o nome do usuário, número da conta e valor a ser retirado.
        Chama a função withdraw para realizar o saque.
    8: Extrato Bancário
        Solicita o nome do usuário e número da conta.
        Chama a função statement para exibir o extrato bancário.
    9: Sair do Programa
        Exibe a mensagem de saída e encerra o loop principal.
        Funções Auxiliares:

    get_valid_input: Solicita uma entrada válida ao usuário com base em uma função de validação.
    is_positive_number: Verifica se um valor é um número inteiro positivo.
    is_valid_float: Verifica se um valor é um número float não negativo.
    Funções do Sistema Bancário:

    create_user: Cria um novo usuário e adiciona à lista de usuários.
    create_account: Cria uma nova conta corrente vinculada a um usuário existente.
    list_accounts: Exibe informações sobre todas as contas.
    list_users: Exibe informações sobre todos os usuários.
    deactivate_account: Desativa uma conta com base no número da conta.
    deposit: Realiza um depósito em uma conta corrente.
    withdraw: Realiza um saque em uma conta corrente.
    statement: Exibe o extrato bancário de uma conta corrente.
    Funções de Interface:

    dash: Exibe um menu interativo para o usuário escolher uma op
"""
