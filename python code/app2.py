import json
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/8fe6ad0ce7444393b2fde3a8b2b2c7d3"

web3 = Web3(Web3.HTTPProvider(infura_url))

abi = ""
address = "0x7390b5b827D5AD3D968Fc446D55B25f84E83C7d5"

contract= web3.eth.contract(address=address,abi=abi)

totelSupply = contract.functions.totalSupply().call()
print(web3.fromWei(totelSupply, 'ether'))
print(contract.functions.name().call())
print(contract.functions.symbol().call())