#!/usr/bin/env python3
'''
  a class to manage the API authentication
'''
from typing import List, TypeVar
from flask import request


class Auth:
    '''
      public methods:
        require_auth
        authorization_header
        current_user
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' return False '''
        if (path is None or excluded_paths is None or
                not len(excluded_paths)):
            return True
        if excluded_paths[-1] != '/':
            excluded_paths += '/'
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        ''' return None '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' return None '''
        return None
