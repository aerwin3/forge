"""
Object representation of a player
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship, backref
from forge.models import Base, db_session
from forge.models.exceptions import NotFoundException


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

    #Connection to player
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship("Player", backref=backref('characters', order_by=id))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    def __init__(self, first_name=None,
                 last_name=None, **kwargs):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<Character %s, %s >' % (self.first_name, self.last_name)
