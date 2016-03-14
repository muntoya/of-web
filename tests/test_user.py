# -*- coding: utf-8 -*-

from flask import Flask
from web.model.user import User
import pytest



@pytest.fixture
def user1():
    return User("user1", "asfdg", "heihei")


def test_save(user1):
    user1.save()

