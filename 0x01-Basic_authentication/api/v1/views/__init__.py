#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import index_app_views
from api.v1.views.users import users_app_views

# Import views after the Blueprint creation to avoid circular import issues
from api.v1.views import views



User.load_from_file()
