### NFT PFP

Setup virtual env with 
```bash
$ virtualenv venv
```

Commnd to create NFT on Rinkeby

```bash
$ source venv/bin/activate
$ brownie run scripts/deploy.py --network rinkeby
$ brownie run scripts/mint.py --network rinkeby
$ brownie run scripts/create_metadata.py --network rinkeby # need to have a IPFS server opened at url http://192.168.199.231:5001
$ brownie run scripts/set_tokenuri.py --network rinkeby # set the token uri (IPFS url) for the NFT with the token id

```

