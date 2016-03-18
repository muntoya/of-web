# -*- coding: utf-8 -*-

import pytest
from web.model.team import Team
from .test_user import user1, user2


@pytest.fixture
def team1(user1):
    team = Team.get_by_name('team1')
    if team is None:
        team = Team.new('team1', user1.id)
    return team


def test_query_all_and_compare(team1):
    teams = Team.get_all()
    for team in teams:
        if team.id == team.id:
            assert team == team1


def test_query_by_id(team1):
    team = Team.get_by_id(team1.id)
    assert team == team1

