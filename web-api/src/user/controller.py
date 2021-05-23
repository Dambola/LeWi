from flask import request, make_response
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, \
    get_jwt_identity, set_access_cookies

from src.user.model import UserManager
from src.user.parser import userparser, authparser

import json

class UserController(Resource):
    """User resource for restful api."""

    def get(self):
        manager = UserManager()
        data = userparser.get.parse_args()
        login = data.get('login')
        if login:
            response = manager.searchByLogin(login)
        else:
            response = manager.search()
        return response, 200

    def post(self):
        manager = UserManager()
        data = userparser.post.parse_args()
        done, error = manager.edit(**data)
        return { 'done': done, 'error': error }, 200

    def put(self):
        manager = UserManager()
        data = userparser.put.parse_args()
        done, error = manager.add(**data)
        return { 'done': done, 'error': error }, 200

    def delete(self):
        manager = UserManager()
        data = userparser.delete.parse_args()
        done, error = manager.remove(data['login'])
        return { 'done': done, 'error': error }, 200

class AuthController(Resource):
    """Auth resource for restful api."""

    def post(self):
        manager = UserManager()
        data = authparser.post.parse_args()
        user = manager.authenticate(**data)

        access_token = create_access_token(
            identity = user['login'], 
            headers = { 
                'email' : user['email'],
                'name' : user['name'],
                'nickname' : user['nickname']
            }
        )
        
        response = make_response(json.dumps(user))
        set_access_cookies(response, access_token)
        return response
        