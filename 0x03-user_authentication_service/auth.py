#!/usr/bin/env python3
'''
authintication file
'''
import bcrypt


def _hash_password(password: str) -> bytes:
    '''
    Hashing function
    '''
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
