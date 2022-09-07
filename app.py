import json
from web3 import Web3

infura_eth_url = "https://mainnet.infura.io/v3/45dc72255b3f4075913d38d1a48fb146"
infura_poly_url = 'https://polygon-mainnet.infura.io/v3/45dc72255b3f4075913d38d1a48fb146'
wallet_address = "0x2d6751f0f287085054EF49d0F3B67c7DeCa64CBA"

web3 = Web3(Web3.HTTPProvider(infura_poly_url))
balance = web3.eth.get_balance(wallet_address)*10**-18

print(balance)