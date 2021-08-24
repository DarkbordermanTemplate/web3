import argparse

from loguru import logger
from solcx import install_solc
from web3 import Web3
from web3.middleware import geth_poa_middleware

from .config import CONFIG
from .utilities import compile_contract, get_provider

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--contract",
        "-C",
        required=True,
        help="Contract path",
    )
    parser.add_argument("--solc", "-S", help="Solc version")
    args = parser.parse_args()
    if args.solc:
        install_solc(args.solc)

    w3 = Web3(get_provider(CONFIG.PROVIDER))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    w3.eth.default_account = w3.eth.accounts[0]
    w3.geth.personal.unlock_account(CONFIG.ACCOUNT, CONFIG.PASSWORD, 1000)
    abi, bytecode = compile_contract(f"{args.contract}")
    logger.info(f"abi {abi}")

    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    # Construct a empty contract and deploy
    tx_hash = contract.constructor().transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    for k, v in tx_receipt.items():
        if isinstance(v, bytes):
            logger.info(f"{k} {v.hex()}")
        else:
            logger.info(f"{k} {v}")
