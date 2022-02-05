from brownie import accounts, config, SimpleStorage, network

# import os


def deploy_simple_storage():
    account = get_account()
    # account = accounts.load("rinkebyTestNet")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    simpleStorage = SimpleStorage.deploy({"from": account})
    storedVal = simpleStorage.retrieve()
    print(storedVal)
    transaction = simpleStorage.store(15, {"from": account})
    transaction.wait(1)
    updatedVal = simpleStorage.retrieve()
    print(updatedVal)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
