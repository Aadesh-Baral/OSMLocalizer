from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from backend.config import EnvironmentConfig

db = SQLAlchemy()


def create_app(config=EnvironmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    CORS(app)

    @app.route("/")
    def system():
        return {"system": "healthy"}, 200

    from backend.models.sqlalchemy.translate import Translate, TranslateDTO
    from backend.models.dtos.translate_dto import UpdateTextDTO

    @app.route("/translate", methods=["GET", "POST"])
    def translate():
        if request.method == "GET":
            text = Translate.get_to_translate_text()
            if not text:
                return {"message": "No text to translate"}, 404
            return TranslateDTO.from_orm(text).dict()
        elif request.method == "POST":
            data = request.get_json()
            translate_dto = UpdateTextDTO(**data)
            Translate.update_from_dto(translate_dto)
            return translate_dto.dict(), 200

    return app
