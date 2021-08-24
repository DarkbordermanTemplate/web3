from typing import List, Tuple, Union

from solcx import compile_source, install_solc_pragma
from web3 import Web3


def get_provider(
    connection: str,
) -> Union[Web3.EthereumTesterProvider, Web3.HTTPProvider]:
    """
        Acquire the context provider

    Args:
        connection (str): Connection string

    Returns:
        Union[Web3.EthereumTesterProvider, Web3.HTTPProvider]: Ethereum provider
    """
    if connection:
        return Web3.HTTPProvider(connection)
    return Web3.EthereumTesterProvider()


def get_contract(path: str) -> str:
    """
        Acquire contract content from storages.
        Currently only supports file storage

    Args:
        path (str): File path

    Returns:
        str: Context string
    """
    contract: str = ""
    # Storage Path
    with open(path, "r") as file:
        contract = file.read()
    return contract


def compile_contract(path: str) -> Tuple[List[dict], str]:
    """
        Compile the contract and return its abi and bin

    Args:
        path (str): file path

    Returns:
        Tuple[List[dict], str]: contract (abi, bin) tuple
    """
    contract = get_contract(path)
    install_solc_pragma(contract)
    compiled = compile_source(contract)
    _, contract_interface = compiled.popitem()
    return (contract_interface["abi"], contract_interface["bin"])
