from src.db import database
from src.utils.api import SingletonMeta

from sqlalchemy.exc import IntegrityError

class MusicManager(metaclass=SingletonMeta):

    class __Music(database.Model):
        __tablename__ = 'musics'
        name = database.Column(database.String(100), primary_key = True)
        author = database.Column(database.String(100), primary_key = True)
        type1 = database.Column(database.String(50), nullable = True)
        type2 = database.Column(database.String(50), nullable = True)
        type3 = database.Column(database.String(50), nullable = True)
    __model = __Music

    # ---- Public methods

    def add(self, name: str, author: str, 
        type1=None, type2=None, type3=None)-> (bool, str):
        """This method will insert a new music.

        Args:
            name (str): The name of the music.
            author (str): The author of the music.
            type1 (str): The first type of the music. (Optional)
            type2 (str): The second type of the music. (Optional)
            type3 (str): The third type of the music. (Optional)

        Returns:
            (bool, str): Return a tuple of (done, error). The argument
            done will be True if the new music was inserted otherwise False
            and the argument error will be the error as string.
        """

        if len(name) > 100:
            return False, 'Name must be less than 50 characters long'
        
        if len(author) > 100:
            return False, 'Name must be less than 50 characters long'
        
        if type1 and len(type1) > 50:
            return False, 'Type 1 must be less than 50 characters long'

        if type2 and len(type2) > 50:
            return False, 'Type 2 must be less than 50 characters long'

        if type3 and len(type3) > 50:
            return False, 'Type 3 must be less than 50 characters long'

        done = True
        error = None

        object = self.__model(
            name=name, 
            author=author, 
            type1=type1, 
            type2=type2, 
            type3=type3
        )

        database.session.add(object)
        
        try:
            database.session.flush()
            database.session.commit()

        except IntegrityError:
            database.session.rollback()
            error = 'The music already exist'
            done = False

        except Exception as e:
            database.session.rollback()
            error = 'An error occoured'
            done = False

        return done, error

    def remove(self, name: str, author: str):
        """This method will remove a music.

        Args:
            name (str): The name of the music.
            author (str): The author of the music.

        Returns:
            (bool, str): Return a tuple of (done, error). The argument
            done will be True if the music was deleted otherwise False
            and the argument error will be the error as string.
        """     

        object = self.__model.query.filter_by(name=name, author=author).first()

        if not object:
            return False, 'This music is not found'

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

    def edit(self, oldName: str, oldAuthor: str, name: str, author: str, 
        type1=None, type2=None, type3=None) -> (bool, str):
        """This method will edit a music.

        Args:
            oldName (str): The name of the music.
            oldAuthor (str): The author of the music.
            name (str): The new name of the music.
            author (str): The new author of the music.
            type1 (str): The new first type of the music. (Optional)
            type2 (str): The new second type of the music. (Optional)
            type3 (str): The newthird type of the music. (Optional)

        Returns:
            (bool, str): Return a tuple of (done, error). The argument
            done will be True if the music was edited otherwise False
            and the argument error will be the error as string.
        """

        object = self.__model.query \
            .filter_by(name=oldName, author=oldAuthor).first()

        if not object:
            return False, 'This music is not found'

        done = True
        error = None

        object.name = name
        object.author = author
        object.type1 = type1
        object.type2 = type2
        object.type3 = type3
        
        try:
            database.session.commit()

        except IntegrityError:
            database.session.rollback()
            error = 'Name and Author (Music) already exists'
            done = False

        except:
            database.session.rollback()
            error = 'An error occoured'
            done = False

        return done, error

    def search(self) -> list:
        """This method will return the list of musics.

        Returns:
            list: Musics
        """
        
        return [ self.__toJSON(i) \
            for i in self.__model.query.order_by("name", "author").all() ]
    
    # ---- Private methods

    def __toJSON(self, music):
        return {
            'name': music.name,
            'author': music.author,
            'type1': music.type1,
            'type2': music.type2,
            'type3': music.type3
        }
