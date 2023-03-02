from os import environ
from random import choice, shuffle

from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource

from utils import fail, success

load_dotenv('.env')

DEBUG = bool(int(environ.get('DEBUG')))
ORIGINS = environ.get('CORS_ORIGIN_WHITELIST').split(',')


app = Flask('main')
app.config['CORS_ORIGINS']=ORIGINS
api = Api(app)
cors = CORS(app)


class Home(Resource):
    def post(self):
        form_data = request.get_json()
        ALLOWED_KEYS = {
            'password-length', 'upper-case',
            'lower-case', 'numeric', 'symbols'
        }
        if not True in form_data.values():
            return fail('Select atleast one')
        if set(form_data.keys()).issubset(ALLOWED_KEYS) and 'password-length' in form_data.keys():
            SYMBOLS = tuple(range(33, 48))
            DIGITS = tuple(range(48, 58))
            UPPPER_CASE = tuple(range(65, 91))
            LOWER_CASE = tuple(range(97, 123))
            password = ''
            while len(password) < form_data.get('password-length'):
                if form_data.get('upper-case'):
                    password += chr(choice(UPPPER_CASE))
                if form_data.get('lower-case'):
                    password += chr(choice(LOWER_CASE))
                if form_data.get('numeric'):
                    password += chr(choice(DIGITS))
                if form_data.get('symbols'):
                    password += chr(choice(SYMBOLS))
            password = password[:form_data.get('password-length')]
            password_list = list(password)
            shuffle(password_list)
            return success(''.join(password_list))
        return fail('Invalid keys')


api.add_resource(Home, '/')
if __name__ == '__main__':
    app.run(debug=DEBUG, load_dotenv=True)
