"""Main application file initializing Flask and managing configuration."""

from flask import Flask
import secrets
from dotenv import dotenv_values
import os
import openai

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)

CONFIG = dotenv_values(".env")

OPEN_AI_KEY = CONFIG.get("KEY") or os.environ.get("OPEN_AI_KEY")
OPEN_AI_ORG = CONFIG.get("ORG") or os.environ.get("OPEN_AI_ORG")

openai.api_key = OPEN_AI_KEY
openai.organization = OPEN_AI_ORG

from routes import *  # noqa

if __name__ == "__main__":
    app.run(debug=True)
