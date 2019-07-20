#!/usr/bin/python3

def test_transfer(token, accounts):
    assert token.totalSupply() == "1000 ether"
    token.transfer(accounts[1], "0.1 ether", {'from': accounts[0]})
    assert token.balanceOf(accounts[1]) == "0.1 ether"
    assert token.balanceOf(accounts[0]) == "999.9 ether"
