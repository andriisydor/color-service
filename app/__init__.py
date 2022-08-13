from flask import Flask
from sqlalchemy import create_engine
from config import user, password, database

flask_app = Flask(__name__)
engine = create_engine(f'mysql://{user}:{password}@127.0.0.1:3306/{database}')
