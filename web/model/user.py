# -*- coding: utf-8 -*-

from web import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    passwd = db.Column(db.String(64), default='', nullable=True)
    cnname = db.Column(db.String(128), default='', nullable=True)
    email = db.Column(db.String(255), default='', nullable=True)
    phone = db.Column(db.String(16), default='', nullable=True)
    role = db.Column(db.SmallInteger, default=0, nullable=True)
    created = db.Column(db.TIMESTAMP, nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)

    @classmethod
    def new(cls, name='', passwd='', cnname='', email='', phone='', role=0):
        return cls(id=None, name=name, passwd=passwd, cnname=cnname,
                   email=email, phone=phone, role=role, created=None)

    def __init__(self, id, name, passwd, cnname, email, phone, role, created):
        self.id = id
        self.name = name
        self.passwd = passwd
        self.cnname = cnname
        self.email = email
        self.phone = phone
        self.role = role
        self.created = created

    def save(self):
        db.session.add(self)
        db.session.commit()

