# -*- coding: utf-8 -*-
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
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
        user = cls(id=None, name=name, passwd=passwd, cnname=cnname,
            email=email, phone=phone, role=role, created=None)
        db.session.add(user)
        try:
            db.session.commit()
            return user
        except IntegrityError:
            return None

    @classmethod
    def get_all(cls):
        query = db.session.query(cls)
        return query.all()

    @classmethod
    def get_by_id(cls, id):
        query = db.session.query(User).filter(User.id == id)
        try:
            user = query.one()
            return user
        except NoResultFound:
            return None

    @classmethod
    def get_by_name(cls, name):
        query = db.session.query(User).filter(User.name == name)
        try:
            user = query.one()
            return user
        except NoResultFound:
            return None

    def __init__(self, id, name, passwd, cnname, email, phone, role, created):
        self.id = id
        self.name = name
        self.passwd = passwd
        self.cnname = cnname
        self.email = email
        self.phone = phone
        self.role = role
        self.created = created

