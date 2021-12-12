# Init blockchain list
MINING_REWARD = 10
GENESIS_BLOCK = {
    "previous_hash": "",
    "index": 0,
    "transactions": []
}
blockchain = [GENESIS_BLOCK]
open_transactions = []
owner = "Michael"
participants = {"Michael"}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx["amount"] for tx in block['transactions'] if tx["sender"] == participant]
                 for block in blockchain]
    tx_recipient = [[tx["amount"] for tx in block['transactions'] if tx["recipient"] == participant]
                    for block in blockchain]

    open_tx_sender = [tx["amount"]
                      for tx in open_transactions if tx["sender"] == participant]
    tx_sender.append(open_tx_sender)

    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]

    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]

    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Returns last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(tx):
    sender_balance = get_balance(tx["sender"])
    return sender_balance >= tx["amount"]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append new value as well as last blockchain value to the blockchain.

      Arguments:
        :sender: send of the transaction
        :receipient: recipient of the transaction
        :amount: the amount of coin to send with transaction
    """
    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    """ Process open transactions"""
    last_block = blockchain[-1]
    hashed_block = '-'.join([str(last_block[key]) for key in last_block])
    reward_transaction = {
        "sender": "Minding",
        "recipient": owner,
        "amount": MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": copied_transactions,
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    """ Returns user input for recipient and amount as a tuple with string and float. """
    recipient = input('Recipient: ')
    amount = float(input('Transaction amount: '))
    return recipient, amount


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print(block)
    else:
        print('-' * 50)


def verify_chain():
    """ Verify current blockchain """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])
    # is_valid = True
    # for tx in open_transactions:
    #     if verify_transaction(tx):
    #         is_valid = True
    #     else:
    #         is_valid = False
    # return is_valid


waiting_for_input = True

while waiting_for_input:
    print("Please choose")
    print("1. Add a new transaction value")
    print("2. Mine block")
    print("3. Output the blockchain blocks")
    print("4. Output participents")
    print("5. Check transaction validity")
    print("h. Manipulate the chain")
    print("q. Quit")
    user_choice = get_user_choice()

    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Added transaction')
        else:
            print('Transaction failed')
        print(open_transactions)
    elif user_choice == "2":
        if mine_block():
            open_transactions = []
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "4":
        print(participants)
    elif user_choice == "5":
        if verify_transactions():
            print('All transactions are valid')
        else:
            print("Contains invalid transactions")
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = {
                "previous_hash": "",
                "index": 0,
                "transactions": [{
                    "sender": "Chris",
                    "recipeint": "Michael",
                    "amount": 999
                }]
            }
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Invalid input.")

    if not verify_chain():
        print('Invalid blockchain')
        break

    print(get_balance("Michael"))

print("See you soon!")
