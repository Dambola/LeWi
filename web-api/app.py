from src.type.model import TypeManager
from src.setup import createApplication

import os

user = os.environ.get('MYSQL_USER', 'lamapi')
password = os.environ.get('MYSQL_PASSWORD', 
    'ajZ88Xi2ojnxq9baEUhZDEqhaEPDxpJvkXcest6bkvEiH8fLnI')
host = os.environ.get('MYSQL_HOST', 'localhost')
port = os.environ.get('MYSQL_PORT', '3306')
database = os.environ.get('MYSQL_DATABASE', 'lewi')

database_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
app = createApplication(database_string)

def main():
    app.run(debug=True, port=8390)

if __name__ == '__main__':
    main()