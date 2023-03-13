from web3 import Web3

ganeshe_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganeshe_url))

# print(web3.isConnected())

# print(web3.eth.block_number)

account_1 = "0xBFC4B8575096F218564c1708A8d77812fA0bd5d6"
account_2 = "0xA9C9C19590eBb4Da4A961553A739cb0C375456C1"

private_key = "0xf686450a70b5d3a8ac8c53af863de67f62c259eea2e2dd990ce7ea47f7af9da6"

# get the nonce
nonce = web3.eth.getTransactionCount(account_1)
# build a trasaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50','gwei')
}

# sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key)
# send the transaction

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

# get the transaction

# balance dispalay
balance_1 = web3.eth.getBalance(account_1)
balance_2 = web3.eth.getBalance(account_2)

print(f"Account 1 balance:{web3.fromWei(balance_1, 'ether')} ether")
print(f"Account 2 balance:{web3.fromWei(balance_2, 'ether')} ether")