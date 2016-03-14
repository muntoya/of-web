# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/' \
                                        'falcon_portal_test?charset=utf8'

import sys
sys._called_from_test = True