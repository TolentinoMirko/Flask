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


stazioni = pd.read_csv("/workspace/Flask/static/files/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv",sep= ";")
stazionigeo =gpd.read_file("/workspace/Flask/static/files/ds710_coordfix_ripetitori_radiofonici_milano_160120_loc_final.geojson",sep= ";")
quartieri = gpd.read_file("/workspace/Flask/static/files/ds964_nil_wm.zip")



@app.route('/', methods=['GET'])
def home():
    return render_template("verificab/home.html")

@app.route('/ricerca', methods=['GET'])
def ricerca():
    quartierilista = quartieri.NIL.to_list()
    quartierilista.sort()

    return render_template("verificab/ricerca.html",quart = quartierilista)

@app.route('/risultato', methods=['GET'])
def elenco():
    quartiereutente = request.args["opzioni"]

    quartierescelto = quartieri[quartieri['NIL']==quartiereutente]
    stazioniquart = stazionigeo[stazionigeo.within(quartierescelto.geometry.squeeze())]
    
    return render_template("verificab/risultato.html",nomistazioni = stazioniquart.to_html())

#_______________________________________________________________________________________________________________________________

@app.route('/inserire', methods=['GET'])
def inserire():
    
    
    return render_template("verificab/inserire.html")

@app.route('/contenuto', methods=['GET'])
def contenuto():
    global stazioninelquartiere,quartiereutente1
    
    nomequartiere = request.args["nomequart"]
    quartiereutente1 = quartieri[quartieri['NIL']==nomequartiere]
    stazioninelquartiere = stazionigeo[stazionigeo.within(quartiereutente1.geometry.squeeze())]
    return render_template("verificab/mappa.html")

@app.route('/compmappa', methods=['GET'])
def compmappa():

    fig, ax = plt.subplots(figsize=(12, 8))

    stazioninelquartiere.to_crs(epsg=3857).plot(ax=ax,color="k")
    quartiereutente1.to_crs(epsg=3857).plot(ax=ax, alpha=0.5,edgecolor='k')
    contextily.add_basemap(ax=ax)
    
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
#______________________________________________________________________________________________________
@app.route('/grafico', methods=['GET'])
def grafico():
    global risultato
    risultato = stazioni.groupby("MUNICIPIO")["OPERATORE"].count().reset_index()

    return render_template("verificab/grafico.html",risultato = risultato.to_html())


@app.route('/graficoimmagine', methods=['GET'])
def graficoimmagine():
    fig, ax = plt.subplots(figsize = (6,4))

    x = risultato.MUNICIPIO
    y = risultato.OPERATORE

    ax.bar(x, y, color = "#304C89")
    #visualizzazione del grafico
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
   



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)