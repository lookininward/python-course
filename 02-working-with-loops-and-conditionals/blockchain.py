# Init blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction_value):
    """ Append new value as well as last blockchain value to the blockchain.

      Arguments:
        :transaction_amount: amount that should be added
        :last_transaction_value: the last blockchain transaction. default [1].
    """
    if last_transaction_value == None:
        last_transaction_value = [1]
    blockchain.append([last_transaction_value, transaction_amount])


def get_transaction_value():
    """ Returns input of the user (new transaction amount) as a float. """
    return float(input('Transaction amount: '))


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print(block)
    else:
        print('-' * 50)


def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print("Please choose")
    print("1. Add a new transaction value")
    print("2. Output the blockchain blocks")
    print("h. Manipulate the chain")
    print("q. Quit")
    user_choice = get_user_choice()

    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Invalid input.")

    if not verify_chain():
        print('Invalid blockchain')
        break


print("See you soon!")
