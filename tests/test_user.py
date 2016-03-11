# -*- coding: utf-8 -*-

from flask import Flask
from web.model.user import User
import pytest

app = Flask(__name__)

@pytest.fixture
def user1():
    return User("user1", "asfdg", "heihei")


def test_save():
    user1 = User(name='haha')
    user1.save()

