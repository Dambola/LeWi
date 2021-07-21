from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.permission.model import PermissionManager

class PermissionController(Resource):
    """Permission resource for restful api."""

    @jwt_required
    def get(self):
        login = get_jwt_identity()
        manager = PermissionManager()
        response = manager.load(login)
        return response, 200
