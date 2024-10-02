from flask import Flask
from dotenv import dotenv_values
import os


def create_app():
    app = Flask(__name__)

    # Load API credentials from .env file
    CONFIG = dotenv_values(".env")
    app.config["OPEN_AI_KEY"] = CONFIG.get("KEY") or os.environ.get("OPEN_AI_KEY")
    app.config["OPEN_AI_ORG"] = CONFIG.get("ORG") or os.environ.get("OPEN_AI_ORG")

    # Initialize API credentials
    import openai

    openai.api_key = app.config["OPEN_AI_KEY"]
    openai.organization = app.config["OPEN_AI_ORG"]

    # Register routes
    from app.routes import main

    app.register_blueprint(main)

    return app
