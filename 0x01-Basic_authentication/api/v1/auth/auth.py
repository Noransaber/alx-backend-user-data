#!/usr/bin/env python3
""" 3. Auth class
"""

from flask import Flask, request
from typing import List, TypeVar
import fnmatch


class Auth:
    """
    3. Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        4. require_auth function"""
        # Check if the exculded_paths list is empty, or None
        if not excluded_paths or excluded_paths is None:
            return True

        # Check if the path is none or has a value
        if path is None:
            return True

        # Check if the path is in the exculded_paths list
        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        5. authorization_header function"""
        # If request is None, returns None
        if request is None:
            return None
        # If request doesn’t contain the header key Authorization, returns None
        if request.headers.get('Authorization') is None:
            return None
        # return the value of the header request Authorization
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        6. current_user function"""
        return None
