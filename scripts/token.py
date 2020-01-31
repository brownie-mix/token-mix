#!/usr/bin/python3

from brownie import *

def main():
    Token.deploy("Test Token", "TST", 18, 1e21, {'from': accounts[0]})
