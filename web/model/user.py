# -*- coding: utf-8 -*-

from web import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64), default='', nullable=True)
    cnname = db.Column(db.String(128), default='', nullable=True)
    email = db.Column(db.String(255), default='', nullable=True)
    phone = db.Column(db.String(16), default='', nullable=True)
    role = db.Column(db.SmallInteger, default=0, nullable=True)
    created = db.Column(db.TIMESTAMP, nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def save(self):
        db.session.add(self)
