from web3 import Web3

from signer.utilities import get_provider


def test_get_provider():
    assert isinstance(get_provider(""), Web3.EthereumTesterProvider)
    assert isinstance(get_provider("http://localhost:8545"), Web3.HTTPProvider)
