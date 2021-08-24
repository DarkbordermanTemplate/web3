# Web3
A web3 example template for signing smart contracts

![Integration](https://github.com/DarkbordermanTemplate/web3/workflows/Integration/badge.svg)

## Develop

### Prerequisitive

| Name | Version |
| --- | --- |
| Python | 3.8 |
| pipenv(Python module) | 2018.11.26 or up |

### Environment setup

0. Initialize environment variable

```
cp sample.env .env
```

1. Initialize Python environment

```
make init
```

2. Enter the environment and start developing

```
pipenv shell
```

3. Execute

```
python3 -m signer.main -h
python3 -m signer.main --contract $PWD/solidity/keyvalue.sol
```
