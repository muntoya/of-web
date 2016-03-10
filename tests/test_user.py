# -*- coding: utf-8 -*-

import unittest
from web.model.user import User
from tests.utils import BaseTest

class UserTestCase(BaseTest):
    def saveTest(self):
        user1 = User(name='haha')
        user1.save()
