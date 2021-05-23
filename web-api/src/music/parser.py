from flask_restful.reqparse import RequestParser

class musicparser(object):
    put = RequestParser()
    put.add_argument('name', location = 'json', required = True,
        help = 'Este campo é obrigatório')
    put.add_argument('author', location = 'json', required = True,
        help = 'Este campo é obrigatório')
    put.add_argument('type1', location = 'json', required = True, 
        help = 'Este campo é obrigatório')
    put.add_argument('type2', location='json')
    put.add_argument('type3', location='json')

    post = RequestParser()
    post.add_argument('id', location='json', required = True,
        help = 'Este campo é obrigatório')
    post.add_argument('name', location='json', required = True,
        help = 'Este campo é obrigatório')
    post.add_argument('author', location='json', required = True,
        help = 'Este campo é obrigatório')
    post.add_argument('type1', location='json', required = True,
        help = 'Este campo é obrigatório')
    post.add_argument('type2', location='json')
    post.add_argument('type3', location='json')

    delete = RequestParser()
    delete.add_argument('id', location='json', required = True,
        help = 'Este campo é obrigatório')
