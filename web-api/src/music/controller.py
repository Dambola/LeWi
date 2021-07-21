from flask import request
from flask_restful import Resource

from src.music.model import MusicManager
from src.music.parser import musicparser

class MusicController(Resource):
    """Music resource for restful api."""

    def get(self):
        manager = MusicManager()
        response = manager.search()
        return response, 200
    
    def put(self):
        manager = MusicManager()
        data = musicparser.put.parse_args()
        done, error = manager.add(**data)
        return { 'done': done, 'error': error }, 200
        
    def post(self):
        manager = MusicManager()
        data = musicparser.post.parse_args()
        done, error = manager.edit(**data)
        return { 'done': done, 'error': error }, 200

    def delete(self):
        manager = MusicManager()
        data = musicparser.delete.parse_args()
        done, error = manager.remove(**data)
        return { 'done': done, 'error': error }, 200
        