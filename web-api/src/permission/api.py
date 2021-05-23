PERMS = {}

def permission(cls):
    PERMS[cls.NAME] = cls
    return cls

@permission
class ADD_MUSIC(object):
    ALIAS = 'Add Music'
    NAME = 'ADD_MUSIC'
    DESCRIPTION = 'Permission to Add a Music'

@permission
class EDIT_MUSIC(object):
    ALIAS = 'Edit Music'
    NAME = 'EDT_MUSIC'
    DESCRIPTION = 'Permission to Edit a Music'

@permission
class REM_MUSIC(object):
    ALIAS = 'Remove Music'
    NAME = 'REM_MUSIC'
    DESCRIPTION = 'Permission to Remove a Music'
