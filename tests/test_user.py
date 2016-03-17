# -*- coding: utf-8 -*-

from web.model.user import User
import pytest


@pytest.fixture
def user1():
    return User.new("user1", "asfdg", "heihei")


def test_save(user1):
    user1.save()

def test_read():
    pass
