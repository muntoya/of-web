# -*- coding: utf-8 -*-

from web import db


class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    creator = db.Column(db.Integer, default=0, nullable=False)
    created = db.Column(db.TIMESTAMP, nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)

    @classmethod
    def new(cls, name='', creator=''):
        return cls(id=None, name=name, creator=creator, created=None)

    @classmethod
    def get_by_name(cls, name):
        pass

    @classmethod
    def get_by_id(cls, id):
        pass

    def __init__(self, id, name, creator, created):
        self.id = id
        self.name = name
        self.creator = creator
        self.created = created

    def save(self):
        db.session.add(self)
        db.session.commit()
