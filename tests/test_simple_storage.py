from turtle import update
from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simpleStorage = SimpleStorage.deploy({"from": account})
    startVal = simpleStorage.retrieve()
    expected = 0
    # Assert
    assert startVal == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simpleStorage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    updatedVal = simpleStorage.store(15, {"from": account})
    # Assert
    assert expected == simpleStorage.retrieve()
