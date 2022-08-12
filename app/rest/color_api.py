from app import flask_app
from flask import Blueprint


color_api_blueprint = Blueprint('color_api_blueprint', __name__)


@color_api_blueprint.route('/', methods=['GET'])
def hello():
    return "Hello!"
