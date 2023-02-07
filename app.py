# -*- coding: utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup
from flask_cors import CORS, cross_origin
from flask import render_template, Flask

app = Flask(__name__)
CORS(app)


@app.route("/obtener-url", methods=["GET", "POST"])
@cross_origin()
def busqueda():
    r = requests.get("https://sendadepaz77.radio12345.com")
    soup = BeautifulSoup(r.content)
    url = soup.find("div", {"id": "urladdress"})
    if url:
        return {
            "url": url.text.strip(),
            "status": "success",
            "message": "URL obtenida con éxito",
        }
    return {"status": "failed", "message": "No se pudo obtener la URL"}


if __name__ == "__main__":
    # app.run()
    app.run(debug=True, threaded=True)
