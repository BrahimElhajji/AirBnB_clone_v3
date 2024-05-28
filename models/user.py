#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.password = self.hash_password(kwargs['password'])

    @staticmethod
    def hash_password(password):
        """Hashes the password using MD5"""
        return hashlib.md5(password.encode()).hexdigest()

    @property
    def password(self):
        """Getter for password"""
        return self._password

    @password.setter
    def password(self, value):
        """Setter for password, hashes the value before storing it"""
        self._password = self.hash_password(value)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, include_password=False):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = super().to_dict(include_password)
        if include_password and "password" not in new_dict:
            new_dict["password"] = self._password
        return new_dict
