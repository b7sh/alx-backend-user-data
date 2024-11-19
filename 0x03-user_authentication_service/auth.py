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

    def create_session(self, email: str) -> str:
        '''
        ctreate new session for the user
        '''
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(session_id: str) -> (User | None):
        '''
        getting the user using the session id
        '''
        if session_id is None:
            return None
        try:
            user = self._db.fund_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(user_id: int) -> None:
        '''
        destroy sesision
        '''
        if user_id:
            self._db.update_user(user_id, session_id=None)
            return
        return None
