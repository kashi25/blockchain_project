from web3 import Web3

infura_url = "Enter your infura_url eg:https://mainnet.infura.io/v3/8fe6ad0ce7444393b2fde3a"

web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.block_number)

balance = web3.eth.get_balance("0x7390b5Youraddress")
print(web3.fromWei(balance, "ether")) 