#!flask/bin/python

import json
from flask import Flask
from waitress import serve

# Fake CFP provider
app = Flask(__name__)


@app.route("/")
def home():
    return {"status": "running"}


@app.route("/generate")
def generate_cpf():
    return {"CPF": "12345678910"}


@app.route("/validate", methods=["POST"])
def validate_cfp():
    return {"status": "OK"}


if __name__ == "__main__":
    # run!
    print("Server running")
    serve(app, host="0.0.0.0", port=5001)
