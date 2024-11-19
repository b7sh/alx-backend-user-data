#!/usr/bin/env python3
''' Testing '''
import requests


def register_user(email: str, password: str) -> None:
    '''
    a
    '''
    pass


def log_in_wrong_password(email: str, password: str) -> None:
    '''
    b
    '''
    pass


def log_in(email: str, password: str) -> str:
    '''
    c
    '''
    pass


def profile_unlogged() -> None:
    '''
    d
    '''
    pass


def profile_logged(session_id: str) -> None:
    '''
    e
    '''
    pass


def log_out(session_id: str) -> None:
    '''
    f
    '''
    pass


def reset_password_token(email: str) -> str:
    '''
    g
    '''
    pass


def update_password(email: str, reset_token: str, new_password: str) -> None:
    '''
    h
    '''
    pass
