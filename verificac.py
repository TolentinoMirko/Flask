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

lineeurbane['lung_km'] = lineeurbane['lung_km'].astype(float)#per cambiare tipo la colonna
lineeurbane['linea'] = lineeurbane['linea'].astype(int)

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
    valoreminimo = float(request.args['valmin'])
    valoremassimo = float(request.args['valmax'])

    lineeconvalori = lineeurbane[(lineeurbane['lung_km']<valoremassimo) & (lineeurbane['lung_km']>valoreminimo)]
    print(lineeconvalori)
    return render_template("verificac/elenco.html", lineeconval = lineeconvalori.to_html())

#________________________________________________________________________


@app.route('/inserisci', methods=['GET'])
def inserisci():
    return render_template("verificac/inserisci.html")

@app.route('/lineenelquartiere', methods=['GET'])
def lineenelquartiere():
    quartuser = request.args['quartiereinserito']
    quartiereutente = quartieri[quartieri['NIL']==quartuser] 
    lineepassanti = lineeurbane[lineeurbane.intersects(quartiereutente.geometry.squeeze())]
    lineepassanti = lineepassanti.sort_values(by=['nome'])

    return render_template("verificac/lista.html",linee = lineepassanti.to_html())

#_________________________________________________________________________


@app.route('/dropdown', methods=['GET'])
def dropdown():
    listadropdown = list(set(lineeurbane.linea))
    listadropdown.sort()
    print(listadropdown)
    return render_template("verificac/dropdown.html",lista2 = listadropdown )



@app.route('/sceltanumerolinea', methods=['GET'])
def sceltanumerolinea():
    global numeroutente
    numerouser = request.args['dropdown']
    numeroutente = lineeurbane[lineeurbane.linea == numerouser]
    return render_template("verificac/mappa.html")




@app.route('/mappa', methods=['GET'])
def mappa():

    fig, ax = plt.subplots(figsize=(12, 8))

    numeroutente.to_crs(epsg=3857).plot(ax=ax,color="red")
    quartieri.to_crs(epsg=3857).plot(ax=ax, alpha=0.5,edgecolor='k')
    contextily.add_basemap(ax=ax)
    
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
    





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)