# -*- coding: utf-8 -*-

import pytest
from web.model.user import User


@pytest.fixture
def user1():
    u = User.get_by_name('user1')
    if u is None:
        u = User.new('user1', 'asfdg', 'heihei')
    return u


@pytest.fixture
def user2():
    u = User.get_by_name('user2')
    if u is None:
        u = User.new('user2', '123456', 'haha')
    return u


def test_query_all_and_compare(user1):
    users = User.get_all()
    for user in users:
        if user.id == user1.id:
            assert user == user1


def test_query_by_id(user1, user2):
    user = User.get_by_id(user1.id)
    assert user == user1
    user = User.get_by_id(user2.id)
    assert user == user2

