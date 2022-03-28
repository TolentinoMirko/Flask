from flask import Flask, render_template, request, Response
app = Flask(__name__)


import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import contextily
import geopandas as gpd
import io


matplotlib.use('Agg')


regioni = gpd.read_file("/workspace/Flask/static/files/drive-download-20220328T191711Z-001.zip")
province = gpd.read_file("/workspace/Flask/static/files/ProvCM01012021_g_WGS84.zip")
comuni = gpd.read_file("/workspace/Flask/static/files/drive-download-20220328T192228Z-001.zip")


@app.route('/', methods=['GET'])
def home():
    return render_template('appes7/radioreg.html',regioni = regioni["DEN_REG"])


@app.route('/RadioReg', methods=['GET'])
def radioreg():
    regione = request.args['regione']
    regioneUtente = regioni[regioni['DEN_REG']==regione]
    provincedellareg = province[province.within(regioneUtente.geometry.squeeze())]
    return render_template('appes7/elencoProv.html',reg = regione,province = province['DEN_UTS'])

@app.route("/elencoprov", methods=["GET"])
def elncoprov():
    provincia = request.args["provincia"]
    provinciaUtente = province[province["DEN_UTS"] == provincia]
    comProv = comuni[comuni.within(provinciaUtente.geometry.squeeze())]["COMUNE"].reset_index()
    return render_template("result.html", provincia = provincia, tabella = comProv.to_html())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
