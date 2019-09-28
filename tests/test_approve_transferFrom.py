#!/usr/bin/python3

import pytest


def test_balance(token, accounts):
    assert token.balanceOf(accounts[0]) == "1000 ether"


def test_approval(token, accounts):
    '''Set approval'''
    token.approve(accounts[1], "10 ether", {'from': accounts[0]})
    assert token.allowance(accounts[0], accounts[1]) == "10 ether"
    assert token.allowance(accounts[0], accounts[2]) == 0

    token.approve(accounts[1], "6 ether", {'from': accounts[0]})
    assert token.allowance(accounts[0], accounts[1]) == "6 ether"


def test_transferFrom(token, accounts):
    '''Transfer tokens with transferFrom'''
    token.approve(accounts[1], "6 ether", {'from': accounts[0]})
    token.transferFrom(accounts[0], accounts[2], "5 ether", {'from': accounts[1]})

    assert token.balanceOf(accounts[2]) == "5 ether"
    assert token.balanceOf(accounts[1]) == 0
    assert token.balanceOf(accounts[0]) == "995 ether"
    assert token.allowance(accounts[0], accounts[1]) == "1 ether"


def test_transferFrom_reverts(token, accounts):
    '''transerFrom should revert'''
    with pytest.reverts("Insufficient allowance"):
        token.transferFrom(accounts[0], accounts[2], "1 ether", {'from': accounts[1]})

    with pytest.reverts("Insufficient allowance"):
        token.transferFrom(accounts[0], accounts[2], "1 ether", {'from': accounts[0]})
