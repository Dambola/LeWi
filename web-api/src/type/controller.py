from flask import request
from flask_restful import Resource

from src.type.model import TypeManager
from src.type.parser import typeparser

class TypeController(Resource):
    """Type resource for restful api."""

    def get(self):
        manager = TypeManager()
        return manager.search(), 200

    def post(self):
        manager = TypeManager()
        data = typeparser.post.parse_args()
        done, error = manager.add(data['name'])
        return { 'done': done, 'error': error }, 200
    
    def delete(self):
        manager = TypeManager()
        data = typeparser.delete.parse_args()
        done, error = manager.remove(data['name'])
        return { 'done': done, 'error': error }, 200
        