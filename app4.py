import json
from web3 import Web3

ganeshe_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganeshe_url))

obj = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"myNumber","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_number","type":"uint256"}],"name":"setNumber","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

adress = web3.toChecksumAddress('0xd9145CCE52D386f254917e481eB44e9943F39135')

contract = web3.eth.contract(address=adress, abi=obj)

print(contract.functions.myNumber().call())