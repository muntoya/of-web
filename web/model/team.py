# -*- coding: utf-8 -*-
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
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
        team = cls(id=None, name=name, creator=creator, created=None)
        db.session.add(team)
        try:
            db.session.commit()
            return team
        except IntegrityError:
            return None

    @classmethod
    def get_by_name(cls, name):
        query = db.session.query(Team).filter(Team.name == name)
        try:
            team = query.one()
            return team
        except NoResultFound:
            return None

    @classmethod
    def get_by_id(cls, id):
        query = db.session.query(Team).filter(Team.id == id)
        try:
            team = query.one()
            return team
        except NoResultFound:
            return None

    @classmethod
    def get_all(cls):
        query = db.session.query(cls)
        return query.all()
    
    def __init__(self, id, name, creator, created):
        self.id = id
        self.name = name
        self.creator = creator
        self.created = created

    def save(self):
        db.session.add(self)
        db.session.commit()
