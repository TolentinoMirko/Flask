from flask import Flask, render_template, request, Response
app = Flask(__name__)


import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import contextily
import geopandas as gpd
import io
import pandas as pd

stazioni = pd.read_csv("/workspace/Flask/static/files/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv",sep= ";")


@app.route('/', methods=['GET'])
def home():
    return render_template("verificaa/home.html")

@app.route('/numero', methods=['GET'])
def numero():
#numero stazioni per ogni munnicipio
    risultato = stazioni.groupby("MUNICIPIO")["OPERATORE"].count().reset_index()

    return render_template("verificaa/link1.html",risultato = risultato.to_html())








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)