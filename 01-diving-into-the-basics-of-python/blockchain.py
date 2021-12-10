# Init blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns last value of the current blockchain. """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction_value=[1]):
    """ Append new value as well as last blockchain value to the blockchain.

      Arguments:
        :transaction_amount: amount that should be added
        :last_transaction_value: the last blockchain transaction. default [1].
    """
    blockchain.append([last_transaction_value, transaction_amount])


def get_user_input():
    """ Returns input of the user (new transaction amount) as a float. """
    return float(input('Your transaction amount: '))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction_value=get_last_blockchain_value(),
          transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)
