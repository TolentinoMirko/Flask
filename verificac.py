from flask import Flask, render_template, request, Response, redirect,url_for
app = Flask(__name__)


import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import contextily
import geopandas as gpd
import io
import pandas as pd

quartieri = gpd.read_file("/workspace/Flask/static/files/ds964_nil_wm.zip")
lineeurbane = gpd.read_file("/workspace/Flask/static/files/percorsi.geojson")


@app.route('/', methods=['GET'])
def home():
    return render_template("verificac/home.html")

@app.route('/selezione', methods=['GET'])
def selezione():
    scelta = request.args['scelta']
    if scelta == "es1":
        return redirect(url_for("valori"))
    elif scelta == "es2":
        return redirect(url_for("inserisci"))
    else:
        return redirect(url_for("dropdown"))
    
@app.route('/valori', methods=['GET'])
def valori():
    return render_template("verificac/valori.html")


@app.route('/minemax', methods=['GET'])
def minemax():
    valoreminimo = request.args['valmin']
    valoremassimo = request.args['valmax']

    lineeconvalori = lineeurbane[(lineeurbane['lung_km']<valoremassimo) & (lineeurbane['lung_km']>valoreminimo)]
    print(lineeconvalori)
    return render_template("verificac/elenco.html", lineeconval = lineeconvalori.to_html())









if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)