"""
Object representation of a player
"""
from sqlalchemy import Column, Integer, String
from forge.models import Base


class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    dci = Column(Integer, unique=True)
    username = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(120), unique=True)
    phone = Column(Integer)

    @property
    def serialize(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'dci': self.dci,
            'username': self.username
        }

    def __init__(self, first_name=None,
                 last_name=None, email=None,
                 phone=None, dci=None, username=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.dci = dci
        self.username = username

    def __repr__(self):
        return '<Player %r>' % (self.first_name)

