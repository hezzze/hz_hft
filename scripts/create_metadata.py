from brownie import M2NFT, network
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os


DEFAULT_NAME_PREFIX = "m2_nft_v1"
DEFAULT_DESCRIPTION = "Some random creation from years ago"


def main():
    m2nft = M2NFT[-1]
    number_of_m2nfts = m2nft.totalSupply()
    print(f"You have created {number_of_m2nfts} items")
    for token_id in range(number_of_m2nfts):
        metadata_file_name = f"./metadata/{network.show_active()}/{token_id}.json"
        collectible_metadata = metadata_template
        print(metadata_file_name)
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwrite")
        else:
            print(f"Creating Metadata file: {metadata_file_name}")
            collectible_metadata["name"] = f"{DEFAULT_NAME_PREFIX}-{token_id}"
            collectible_metadata["description"] = DEFAULT_DESCRIPTION
            image_path = "./img/" + f"{token_id}.png"

            image_uri = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_uri = upload_to_ipfs(image_path)

            image_uri = image_uri if image_uri else ""
            collectible_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)
                print(f"Uploaded {metadata_file_name} to ipfs")


# curl -X POST -F file=@metadata/rinkeby/0-SHIBA_INU.json http://localhost:5001/api/v0/add


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        file_binary = fp.read()
        # upload stuff..
        ipfs_url = "http://192.168.199.231:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": file_binary})
        ipfs_hash = response.json()["Hash"]

        # "./img/0.png" -> "0.png"
        filename = filepath.split("/")[-1:][0]
        file_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        # https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0.json
        print(file_uri)
        return file_uri
