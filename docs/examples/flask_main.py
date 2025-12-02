# https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application
from flask import Flask, jsonify

app = Flask(__name__)

async def hello_world(*args, **kwargs):
    return jsonify({'Hello': 'World!'})

app.route("/")(hello_world)
