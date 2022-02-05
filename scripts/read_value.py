from brownie import accounts, config, SimpleStorage


def read_contract():
    simpleStorage = SimpleStorage[-1]
    # ABI
    # Address
    print(simpleStorage.retrieve())


def main():
    read_contract()
