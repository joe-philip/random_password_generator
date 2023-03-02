from os import environ

from dotenv import load_dotenv

load_dotenv('.env')

DEBUG = bool(int(environ.get('DEBUG')))
ORIGINS = environ.get('CORS_ORIGIN_WHITELIST').split(',')
