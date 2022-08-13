from flask import Blueprint, jsonify
from app import engine
from sqlalchemy.orm import Session
from app.models.models import Palette
from app.schemas.schemas import PaletteSchema


color_api_blueprint = Blueprint('color_api_blueprint', __name__)


@color_api_blueprint.route('/palette/<id>', methods=['GET'])
def show_palette(id):
    with Session(engine) as session:
        palette = session.query(Palette).filter_by(id=id).one()
        return jsonify(PaletteSchema().dump(palette))
