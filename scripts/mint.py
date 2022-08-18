from brownie import M2NFT
from scripts.helpful_scripts import get_account
from web3 import Web3


def main():
    account_id = input("account id: ")
    account = get_account(id=account_id)
    m2nft = M2NFT[-1]
    creation_transaction = m2nft.safeMint(account, "", {"from": account})
    creation_transaction.wait(1)
    print("Collectible created!")
