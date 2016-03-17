# -*- coding: utf-8 -*-

import pytest
from web.model.user import User
from .test_user import user1, user2


@pytest.fixture
def team1(user1):
    pass


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

