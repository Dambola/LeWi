from src.db import database
from src.utils.api import SingletonMeta
from src.user.utils import encryptPassword

from sqlalchemy.exc import IntegrityError

class UserManager(metaclass=SingletonMeta):
    """This class is a Singleton that manager the user.
    """    

    class __User(database.Model):
        __tablename__ = 'users'
        name = database.Column(database.String(100))
        nickname = database.Column(database.String(25))
        login = database.Column(database.String(50), primary_key = True)
        email = database.Column(database.String(50), unique = True)
        password = database.Column(database.String(50))
    __model = __User

    # ---- Public methods

    def add(self, name: str, nickname: str, 
        login: str, email: str, password: str) -> (bool, str):
        """This method will insert an new user.

        Args:
            name (str): The name of the user.
            nickname (str): The nickname of the user.
            login (str): The login of the user. Must be unique.
            email (str): The email of the user. Must be unique.
            password (str): The password of the user.

        Returns:
            (bool, str): Return a tuple of (done, error). The argument
            done will be True if the new user was inserted otherwise False
            and the argument error will be the error as string.
        """

        if len(name) > 100:
            return False, 'Name must be less than 100 characters long'

        elif len(nickname) > 25:
            return False, 'Nickname must be less than 25 characters long'
        
        elif len(login) > 50:
            return False, 'Login must be less than 50 characters long'
        
        elif len(email) > 50:
            return False, 'Email must be less than 50 characters long'
        
        elif len(password) > 20:
            return False, 'Password must be less than 20 characters long'

        done = True
        error = None

        password = encryptPassword(password)
        object = self.__model(
            name=name, 
            nickname=nickname, 
            login=login, 
            email=email, 
            password=password
        )

        database.session.add(object)
        
        try:
            database.session.flush()
            database.session.commit()

        except IntegrityError:
            database.session.rollback()
            error = 'Login and Email must be Unique'
            done = False

        except Exception as e:
            database.session.rollback()
            error = 'An error occoured'
            done = False

        return done, error

    def remove(self, login: str) -> (bool, str):
        """This method will remove an user.

        Args:
            login (str): The login of the user.

        Returns:
            (bool, str): Return a tuple of (done, error). The argument
            done will be True if the user was deleted otherwise False
            and the argument error will be the error as string.
        """

        object = self.__model.query.filter_by(login=login).first()

        if not object:
            return False, 'This user is not found'

        done = True
        error = None

        try:
            database.session.delete(object)
            database.session.commit()
        
        except:
            database.session.rollback()
            error = 'An error occoured'
            done = False

        return done, error

    def edit(self, login: str, name=None, nickname=None, 
        email=None, password=None) -> (bool, str):
        """This method will edit an user.

        Args:
            login (str): The login of the user.
            name (str): The name of the user. (Optional)
            nickname (str): The nickname of the user. (Optional)
            email (str): The email of the user. Must be unique. (Optional)
            password (str): The password of the user. (Optional)

        Returns:
            (bool, str): Return a tuple of (done, error). The argument
            done will be True if the user was edited otherwise False
            and the argument error will be the error as string.
        """

        if name and len(name) > 100:
            return False, 'Name must be less than 100 characters long'

        elif nickname and len(nickname) > 25:
            return False, 'Nickname must be less than 25 characters long'
        
        elif login and len(login) > 50:
            return False, 'Login must be less than 50 characters long'
        
        elif email and len(email) > 50:
            return False, 'Email must be less than 50 characters long'
        
        elif password and len(password) > 20:
            return False, 'Password must be less than 20 characters long'

        object = self.__model.query.filter_by(login=login).first()

        if not object:
            return False, 'This user is not found'

        done = True
        error = None

        if name: object.name = name
        if nickname: object.nickname = nickname
        if email: object.email = email
        if password: object.password = encryptPassword(password)
        
        try:
            database.session.commit()

        except IntegrityError:
            database.session.rollback()
            error = 'Login and Email must be Unique'
            done = False

        except:
            database.session.rollback()
            error = 'An error occoured'
            done = False

        return done, error

    def search(self) -> list:
        """This method will return the list of users.

        Returns:
            list: Users
        """
        
        return [ self.__toJSON(i) \
            for i in self.__model.query.all() ]
    
    def searchByLogin(self, login: str) -> dict:
        user = self.__model.query.filter_by(login=login).first()
        return self.__toJSON(user)

    def authenticate(self, login, password):
        password = encryptPassword(password)
        object = self.__model.query \
            .filter_by(login=login, password=password).first()

        if not object:
            return None
        return self.__toJSON(object)

    # ---- Private methods

    def __toJSON(self, user):
        return {
            'login': user.login,
            'name': user.name,
            'nickname': user.nickname,
            'email': user.email
        }
