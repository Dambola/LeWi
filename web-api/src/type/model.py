from src.db import database
from src.utils.api import SingletonMeta

from sqlalchemy.exc import IntegrityError

class TypeManager(metaclass=SingletonMeta):
    """This class is a Singleton that manager the type.
    """    

    class __Type(database.Model):
        __tablename__ = 'types'
        name = database.Column(database.String(50), primary_key = True)
    __model = __Type

    # ---- Public methods

    def add(self, name: str) -> (bool, str):
        """This method will insert a new type.

        Args:
            name (str): The name of the type. Must be unique.

        Returns:
            (bool, str): Return a tuple of (done, error). The argument
            done will be True if the new type was inserted otherwise False
            and the argument error will be the error as string.
        """

        if len(name) > 50:
            return False, 'Name must be less than 50 characters long'

        done = True
        error = None

        object = self.__model(name=name)
        database.session.add(object)
        
        try:
            database.session.flush()
            database.session.commit()

        except IntegrityError:
            database.session.rollback()
            error = 'Name must be Unique'
            done = False

        except:
            database.session.rollback()
            error = 'An error occoured'
            done = False

        return done, error

    def remove(self, name: str) -> (bool, str):
        """This method will remove a existing type.

        Args:
            name (str): The name of the type. Must exist.

        Returns:
            (bool, str): Return a tuple of (done, error). The argument
            done will be True if the type was deleted otherwise False
            and the argument error will be the error as string.
        """  

        object = self.__model.query.filter_by(name=name).first()

        if not object:
            return False, 'This type is not found'

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

    def search(self) -> list:
        """This method will return the list of types.

        Returns:
            list: Types
        """      
        return [ i.name for i in self.__model.query.all() ]
