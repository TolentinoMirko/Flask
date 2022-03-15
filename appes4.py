# si vuole realizzare un sito web che permetta di visualizzare alcune informazioni sull'andamento dell'epidemia di covid
#  nel nostro paese a partire dai dati presenti nel
# file 'https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv'
# l'utente sceglie la regione da un elenco (menu a tendina),
# clicca su un bottone e il sito deve visualizzare una tabella contenente
#  le informazioni relative a quella regione

# i dati da inserire nel menu a tendina devono essere caricati automaticamente dalla pagina


from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)
df = pd.read_csv('https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv')


@app.route('/', methods=['GET'])
def home():
    reg = df['nome_area'].drop_duplicates().to_list()
    return render_template('appes4/appes4home.html',reg=reg)


@app.route('/data', methods=['GET'])
def data():
    scelta = request.args['Regioni']
    df_result = df[df['nome_area'] == scelta]
    return render_template('appes4/appes4table.html', tables=[df_result.to_html()], titles=[''])

# @app.route('/table', methods=['GET'])
# def table():
    #data = pd.read_csv('https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv')
    # return render_template('appes4/appes4table.html',tables = [data.to_html()],titles = [''])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
