# -*- coding: utf-8 -*-

from frame.store import db2 as db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64), default='')
    cnname = db.Column(db.String(128), default='')
    email = db.Column(db.String(255), default='')
    phone = db.Column(db.String(16), default='')
    role = db.Column(db.Integer(16), default=0)
    created = db.Column(db.TIMESTAMP)

