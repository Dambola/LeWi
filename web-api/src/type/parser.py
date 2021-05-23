from flask_restful.reqparse import RequestParser

class typeparser(object):
    post = RequestParser()
    post.add_argument('name', location='json', required = True,
        help = 'Este campo é obrigatório')

    delete = RequestParser()
    delete.add_argument('name', location='json', required = True,
        help = 'Este campo é obrigatório')