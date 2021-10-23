from flask import Flask, render_template
from peewee import SqliteDatabase, PostgresqlDatabase, MySQLDatabase

import models
from models import Tax, Status

app = Flask(__name__)

############################# todo: change to env variables
DB_TYPE = 'sqlite'
DB_USER = 'invoice'
DB_PASSWORD = ''
DB_TABLE = ''
DB_HOST = 'localhost'

############################## end env variables

############################# site info todo: change to normal way
site_info = {
    'site_title': 'INPvoice',
    'site_language': 'de',
    'site_name': 'INProduct',
    'site_author': 'INProduct',
    'site_description': 'A Invoice Tracking Software',

}




############################# end site info

if DB_TYPE == 'sqlite':
    db = SqliteDatabase('database.db')
    models.db.initialize(db)

with db:
    db.create_tables([Tax, Status])


@app.route('/')
def index_handler():
    return render_template('index.html', site_info=site_info, site_title='Dashboard')


@app.route('/dashboard')
def dashboard_handler():
    return 'dashboard'


@app.route('/idebit')
def idebit_handler():
    return 'idebit'


if __name__ == '__main__':
    app.run(debug=True)
