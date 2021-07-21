from src.db import database
from src.permission.api import PERMISSIONS
from src.utils.api import SingletonMeta

from sqlalchemy.exc import IntegrityError

class PermissionManager(metaclass=SingletonMeta):
    """This class is a Singleton that manager the permissions.
    """    

    class __Permission(database.Model):
        __tablename__ = 'permissions'
        login = database.Column(database.String(50), primary_key = True)
        permission = database.Column(database.String(50), primary_key = True)
    __model = __Permission

    # ---- Public methods

    def assign(self, login: str, permission: str) -> (bool, str):
        """This method will assign a permission to an user.

        Args:
            login (str): The login of the user.
            permission (str): The permission to assign.

        Returns:
            (bool, str): Return a tuple of (done, error). The argument
            done will be True if the permission was assigned otherwise False
            and the argument error will be the error as string.
        """

        if len(login) > 50:
            return False, 'Login must be less than 50 characters long'

        if len(permission) > 50:
            return False, 'Permission must be less than 50 characters long'

        done = True
        error = None

        object = self.__model(login=login, permission=permission)
        database.session.add(object)
        
        try:
            database.session.flush()
            database.session.commit()

        except IntegrityError:
            database.session.rollback()
            error = 'Permission already assigned to the User'
            done = False

        except:
            database.session.rollback()
            error = 'An error occoured'
            done = False

        return done, error

    def revoke(self, login: str, permission: str) -> (bool, str):
        """This method will revoke a permission to an user.

        Args:
            login (str): The login of the user.
            permission (str): The permission to assign.

        Returns:
            (bool, str): Return a tuple of (done, error). The argument
            done will be True if the permission was revoked otherwise False
            and the argument error will be the error as string.
        """  

        object = self.__model.query \
            .filter_by(login=login, permission=permission).first()

        if not object:
            return False, 'The user does not have the given permission'

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

    def load(self, login: str) -> list:
        """This method will return the list of permssions of an user.

        Returns:
            list: Permissions
        """
        permissions = {}
        for row in self.__model.query.filter_by(login=login).all():
            key = row.permission
            if key in PERMISSIONS:
                permissions[key] = PERMISSIONS[key]
        return permissions
