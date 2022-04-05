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
print('quartiere')
print('stazioniquartiere')
print('stazionigeo')

@app.route('/', methods=['GET'])
def home():
    return render_template("verificaa/home1.html")


@app.route('/selezione', methods=['GET'])
def selezione():
    scelta = request.args["scelta"]
    if scelta == "es1":
        return redirect(url_for("numero"))
    elif scelta == "es2":
        return redirect(url_for("input"))
    else:
        return redirect(url_for("dropdown"))

#_______________________________________________________________________________________________es_1

@app.route('/numero', methods=['GET'])
def numero():
#numero stazioni per ogni munnicipio
    global risultato
    risultato = stazioni.groupby("MUNICIPIO")["OPERATORE"].count().reset_index()

    return render_template("verificaa/link1.html",risultato = risultato.to_html())

@app.route('/grafico', methods=['GET'])
def grafico():
    #costruzione del grafico
    fig, ax = plt.subplots(figsize = (6,4))

    x = risultato.MUNICIPIO
    y = risultato.OPERATORE

    ax.bar(x, y, color = "#304C89")
    #visualizzazione del grafico
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
    

#_______________________________________________________________________________________________es_2

@app.route('/input', methods=['GET'])
def input():
    return render_template("verificaa/input.html")

@app.route('/ricerca', methods=['GET'])
def ricerca():
    global quartiere, stazioniquartiere
    
    nomequartiere = request.args["quartiere"]
    quartiere = quartieri[quartieri['NIL']==nomequartiere]
    #quartiere = quartieri[quartieri.NIL.str.contains(quartiere)]
    stazioniquartiere = stazionigeo[stazionigeo.within(quartiere.geometry.squeeze())]
    return render_template("verificaa/elenco1.html",risultato = stazioniquartiere.to_html())

@app.route('/mappa', methods=['GET'])
def mappa():

    fig, ax = plt.subplots(figsize=(12, 8))

    stazioniquartiere.to_crs(epsg=3857).plot(ax=ax,color="k")
    quartiere.to_crs(epsg=3857).plot(ax=ax, alpha=0.5,edgecolor='k')
    contextily.add_basemap(ax=ax)
    
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
 
#_______________________________________________________________________________________________es 3

@app.route('/dropdown', methods=['GET'])
def dropdown():
    nomistazioni = stazioni.OPERATORE.to_list()
    nomistazioni = list(set(nomistazioni))
    nomistazioni.sort()

    #to_list() trasforma in una lista
    
    return render_template('verificaa/dropdown.html',stazioni = nomistazioni)


@app.route('/sceltastazione', methods=['GET'])
def sceltastazione():
    global quartiere1, stazioneutente
    stazione = request.args['dropdown']
    stazioneutente = stazionigeo[stazionigeo['OPERATORE']==stazione]
    quartiere1 = quartieri[quartieri.contains(stazioneutente.geometry.squeeze())]


    return render_template("verificaa/vistastazione.html",quartiere=quartiere1)

@app.route('/mappaquart', methods=['GET'])
def mappaquart():

    fig, ax = plt.subplots(figsize=(12, 8))

    stazioneutente.to_crs(epsg=3857).plot(ax=ax,color="k")
    quartiere1.to_crs(epsg=3857).plot(ax=ax, alpha=0.5,edgecolor='k')
    contextily.add_basemap(ax=ax)
    
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)