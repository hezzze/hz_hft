from brownie import network, M2NFT
from scripts.helpful_scripts import OPENSEA_URL, get_account


def main():
    print(f"Wokring on {network.show_active()}")
    m2nft = M2NFT[-1]
    number_of_m2nfts = m2nft.totalSupply()
    token_id = input("token id: ")
    uri = input("uri: ")
    print(f"You have {number_of_m2nfts} items")
    if not m2nft.tokenURI(token_id).startswith("https://"):
        print(f"Setting tokenURI of {token_id} to {uri}")
        set_tokenURI(token_id, m2nft, uri)


def set_tokenURI(token_id, nft_contract, tokenURI):
    account_id = input("account id: ")
    account = get_account(id=account_id)
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! you can view your nft at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Please wait up to 20mins, and hit refresh metadata button")
