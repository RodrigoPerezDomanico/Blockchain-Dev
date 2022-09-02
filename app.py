import json
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/45dc72255b3f4075913d38d1a48fb146"
wallet_address = "0x5c577102DEf8D34fA77E7C0D481c1a7B62181Cb3"

web3 = Web3(Web3.HTTPProvider(infura_url))
balance = web3.eth.get_balance(wallet_address)*10**-18

print(balance)