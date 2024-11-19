#!/usr/bin/env python3
'''
authintication file
'''
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    '''
    Hashing function
    '''
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    ''' return string representiation of uuid4 '''
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        method to register a new user
        if not exist
        '''
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            user = self._db.add_user(email, hashed)
            return user

        raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        '''
        check the user credintials
        '''
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(
                    password.encode('utf-8'),
                    user.hashed_password):
                return True
            return False
        except NoResultFound:
            return False
