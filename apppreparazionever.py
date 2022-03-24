import pandas as pd
import io
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
import matplotlib.pyplot as plt
from flask import Flask, render_template, send_file, make_response, url_for, Response, request
app = Flask(__name__)

quartieri = gpd.read_file("/workspace/Flask/static/files/ds964_nil_wm.zip")
fontanelle = gpd.read_file("/workspace/Flask/static/files/Fontanelle.zip")

@app.route('/', methods=['GET'])
def home():

    return render_template('/appPrepVer/PrepVerHome.html')


@app.route('/visualizza', methods=['GET'])
def visualizza():
    fig, ax = plt.subplots(figsize=(12, 8))


    quartieri.to_crs(epsg=3857).plot(ax=ax, alpha=0.5,edgecolor="black")
    contextily.add_basemap(ax=ax)

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/rice', methods=['GET'])
def rice():
    return render_template('/appPrepVer/PrepVerRicerca.html')

@app.route('/plot.png', methods=['GET'])
def quar():
     
    fig, ax = plt.subplots(figsize=(12, 8))

    QuartOttenuto.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/ricerca', methods=['GET'])
def districs():
    global QuartOttenuto
    
    inserisce = request.args['Quartier']
    
    QuartOttenuto = quartieri[quartieri['NIL']==inserisce]
    
    return render_template("appPrepVer/PrepVerPlotRice.html",nomiquar=inserisce)
   

@app.route('/scelta', methods=['GET'])
def choose():
    inserisce = quartieri['NIL'].to_list()
    
    return render_template('/appPrepVer/PrepVerScelta.html',nomiquar=inserisce)

@app.route('/fontanelle', methods=['GET'])
def fonta():       
        global fontanelle
        tuttiquar = quartieri['NIL'].to_list()
        fontane = quartieri.sjoin(fontanelle,quartieri,op="within")
        return render_template('/appPrepVer/FontanelleScelta.html',tuttiquartieri=tuttiquar,fontanelle=fontane)
































if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
