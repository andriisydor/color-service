from app import flask_app
from app.rest.color_api import color_api_blueprint

flask_app.register_blueprint(color_api_blueprint)

if __name__ == '__main__':
    flask_app.run(debug=True)
