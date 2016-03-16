# -*- coding: utf-8 -*-

from web import db


class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    creator = db.Column(db.Integer, default=0, nullable=False)
    created = db.Column(db.TIMESTAMP, nullable=True)

    def __init__(self):
        pass
