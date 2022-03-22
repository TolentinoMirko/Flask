# realizzare un sito web che restituisca la mappa dei quartieri di milano.
# ci deve essere una home page con un link "Quartieri di milano":
# cliccado su questo link si deve visualizzare la mappa dei quartieri di milano



from flask import Flask, render_template, send_file, make_response, url_for, Response,request
app = Flask(__name__)

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import contextily
import geopandas as gpd
import io
import pandas as pd

matplotlib.use('Agg')


quartieri = gpd.read_file("/workspace/Flask/static/files/ds964_nil_wm.zip")


@app.route('/', methods=['GET'])
def home():

    return render_template('/appes6/appes6home.html')


@app.route('/plot.png', methods=['GET'])
def quar():
     
    fig, ax = plt.subplots(figsize=(12, 8))

    QuartOttenuto.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/plot', methods=['GET'])
def districs():
    global QuartOttenuto
    inserisce = request.args['Quarti']
    QuartOttenuto = quartieri[quartieri['NIL']==inserisce]
    return render_template("appes6/appes6plot.html",nome = inserisce)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
