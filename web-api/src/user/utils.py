from hashlib import md5

def encryptPassword(password):
    encryptedPassword = md5(password.encode())
    return encryptedPassword.hexdigest()
    