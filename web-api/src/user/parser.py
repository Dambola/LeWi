from flask_restful.reqparse import RequestParser

class userparser(object):
    put = RequestParser()
    put.add_argument('name', location = 'json', required = True,
        help = 'Name is required')
    put.add_argument('nickname', location = 'json', required = True,
        help = 'Nickname is required')
    put.add_argument('login', location = 'json', required = True,
        help = 'Login is required')
    put.add_argument('email', location = 'json', required = True,
        help = 'Email is required')
    put.add_argument('password', location = 'json', required = True,
        help = 'Password is required')

    post = RequestParser()
    post.add_argument('login', location = 'json', required = True,
        help = 'Name is required')
    post.add_argument('name', location = 'json')
    post.add_argument('nickname', location = 'json')
    post.add_argument('email', location = 'json')
    post.add_argument('password', location = 'json')

    delete = RequestParser()
    delete.add_argument('login', location = 'json', required = True,
        help = 'Login is required')
    
    get = RequestParser()
    get.add_argument('login', location = 'json')

class authparser(object):
    post = RequestParser()
    post.add_argument('login', location = 'json', required = True,
        help = 'Login is required')
    post.add_argument('password', location = 'json', required = True,
        help = 'Login is required')
    