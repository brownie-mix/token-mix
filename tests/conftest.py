#!/usr/bin/python3

import pytest


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    pass


@pytest.fixture(scope="module")
def token(Token, accounts):
    return accounts[0].deploy(Token, "Test Token", "TST", 18, 1e21)
