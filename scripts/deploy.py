from brownie import M2NFT, config, network
from scripts.helpful_scripts import get_account


NAME = "M2NFT"
SYMBOL = "M2PFP"


def deploy():
    account_id = input("account id: ")
    account = get_account(id=account_id)
    # We want to be able to use the deployed contracts if we are on a test net
    # Otherwise, we want to deploy some mocks and use those
    m2nft = M2NFT.deploy(
        NAME,
        SYMBOL,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("M2NFT contract has been deployed")


def main():
    deploy()
