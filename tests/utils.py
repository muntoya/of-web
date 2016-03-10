# -*- coding: utf-8 -*-

import unittest
from web import app


class BaseTest(unittest.TestCase):
    def __init__(self):
        self.app_ctx = app.app_context()

    def setUp(self):
        self.app_ctx.push()

    def tearDown(self):
        self.app_ctx.pop()
