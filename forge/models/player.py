"""
Object representation of a player
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship 
from forge.models import Base, db_session
from forge.models.character import Character
from forge.models.exceptions import NotFoundException
import ast

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(120))
    phone = Column(Integer)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'username': self.username,
            'characters':  [character.serialize for character in self.characters]
        }

    def __init__(self, first_name=None,
                 last_name=None, email=None,
                 phone=None, username=None, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.username = username

    def __repr__(self):
        return '<Player %r>' % (self.first_name)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter((cls.username == username)).first()

    @classmethod
    def get_by_id(cls, id):
        player = cls.query.filter((cls.id == id)).first()
        if player == None:
            raise NotFoundException('Player %s was not found.' % id)
        return player

    @classmethod
    def update(cls, id, attrs):
        player = Player.get_by_id(id)
        for key, value in attrs.iteritems():
            if key == 'id':
                continue
            if key == 'characters':
                cs = ast.literal_eval(value)
                chars = []
                for char in cs:
                    chars.append(Character(char['first_name'],
                                           char['last_name']))
                player.characters = chars
                continue
            setattr(player, key, value)
        db_session.commit()
        return player

    @classmethod
    def create(cls, attrs):
        player = Player.get_by_username(attrs['username'])
        if player == None:
            try:
                player = Player(attrs['first_name'], attrs['last_name'],
                                attrs['email'], attrs['phone'],
                                attrs['username'])
                db_session.add(player)
                db_session.commit()
            except IntegrityError as e:
                raise Exception('Username already exist.')
        return player

    @classmethod
    def delete(cls, id):
        player = Player.get_by_id(id)
        db_session.delete(player)
        db_session.commit()
