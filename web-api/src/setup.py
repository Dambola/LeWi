from flask import Flask, make_response
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager, \
    unset_access_cookies, unset_jwt_cookies

from src.db import database

import json

def createApplication(database_string):
    application = Flask(__name__)

    application.config['CORS_HEADERS'] = 'Content-Type'

    application.config['JWT_SECRET_KEY'] = 'super-secret'
    application.config['JWT_TOKEN_LOCATION'] = ['cookies']
    application.config['JWT_COOKIE_CSRF_PROTECT'] = False
    application.config['JWT_CSRF_CHECK_FORM'] = False
    
    application.config['SESSION_COOKIE_SECURE'] = True

    application.config['SECRET_KEY'] = 'kjqOQXTvEgd1Aj2JyZ5x7SRgS49J60n0qF0w3u'
    application.config['ALGORITHM'] = 'HS256'
    
    application.config['SQLALCHEMY_DATABASE_URI'] = database_string 
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    restful_api = Api(application)
    database.init_app(application)

    @application.before_first_request
    def create_tables():
        database.create_all()
    
    from src.type.controller import TypeController
    from src.user.controller import UserController, AuthController
    from src.music.controller import MusicController

    restful_api.add_resource(TypeController, '/type')
    restful_api.add_resource(UserController, '/user')
    restful_api.add_resource(AuthController, '/auth')
    restful_api.add_resource(MusicController, '/music')

    cors_policy = CORS(application, resources={r"/*": {"origins": "*"}}, 
        supports_credentials=True)
    jwt_policy = JWTManager(application)

    @jwt_policy.revoked_token_loader
    @jwt_policy.needs_fresh_token_loader
    @jwt_policy.invalid_token_loader
    @jwt_policy.unauthorized_loader
    def invalid_token_callback(callback):
        response = make_response(json.dumps({ 'message': 'Invalid JWT Token.', 'mustReload': True }))
        unset_jwt_cookies(response)
        return response, 401

    @jwt_policy.expired_token_loader
    def expired_token_callback(callback):
        response = make_response(json.dumps({ 'message': 'Expired JWT Token.', 'mustReload': True }))
        unset_access_cookies(response)
        return response, 401

    return application