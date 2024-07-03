from web3 import Web3
from config import ETH_NODE_URL, WALLET_PRIVATE_KEY, WALLET_ADDRESS

web3 = Web3(Web3.HTTPProvider(ETH_NODE_URL))

def get_eth_balance(address: str) -> float:
    balance = web3.eth.get_balance(address)
    return web3.fromWei(balance, 'ether')

def send_eth(to_address: str, amount: float) -> str:
    nonce = {
        'nonce': nonce,
        'to': to_address,
        'value': web3.toWei(amount, 'ether'),
        'gas': 21000,
        'gasPrice': web3.toWei('50', 'gwei')
    }
    
    signed_tx = web3.eth.account.signTransaction(tx, WALLET_PRIVATE_KEY)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return web3.toHex(tx_hash)