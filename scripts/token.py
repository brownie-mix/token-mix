#!/usr/bin/python3

from brownie import BasicERC20, accounts


def main():
    return BasicERC20.deploy("Test Token", "TST", 18, 1e21, {'from': accounts[0]})
