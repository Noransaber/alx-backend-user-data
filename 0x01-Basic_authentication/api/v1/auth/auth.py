#!/usr/bin/env python3
""" 3. Auth class
"""

import request from flask

class Auth:
  """
  3. Auth class
  """
  def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
    """
    4. require_auth function"""
    return False

  def authorization_header(self, request=None) -> str:
    """
    5. authorization_header function"""
    return None
  
  def current_user(self, request=None) -> TypeVar('User'):
    """
    6. current_user function"""
    return None
