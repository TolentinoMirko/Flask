# si vuole realizzare un sito web per memorizzare le squadre di uno sport a scelta
# l'utente deve poter inserire il nome della squadra e la data di fondazione e la
# città.

# deve inoltre poter effettuare delle ricerche inserendo uno dei valori delle colonne
# e ottenendo i dati presenti.

from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

#dfvuoto = pd.DataFrame(columns=['Squadra','Data Fondazione','Città'])


@app.route('/', methods=['GET'])
def home():

    return render_template('/appes5/appes5home.html')


@app.route('/inserisci', methods=['GET'])
def inserisci():

    return render_template('/appes5/appes5inserisci.html')


@app.route('/ricerca', methods=['GET'])
def ricerca():

    return render_template('/appes5/appes5ricerca.html')


@app.route('/dati', methods=['GET'])
def dati():
    team = request.args['Squadra']
    year = request.args['Anno']
    city = request.args['Citta']

    df1 = pd.read_csv('/workspace/Flask/templates/appes5/dati.csv')

    df2 = {'Squadra': team, 'Anno': year, 'Citta': city}
    df1 = df1.append(df2, ignore_index=True)
    df1.to_csv('/workspace/Flask/templates/appes5/dati.csv', index=False, )
    print(df2)
    return df1.to_html()


@app.route('/dati2', methods=['GET'])
def dati2():
    team2 = request.args['Squadra2']
    year2 = request.args['Anno2']
    city2 = request.args['Citta2']


    df3 = pd.read_csv('/workspace/Flask/templates/appes5/dati.csv')
    df4 = df3[df3['Squadra']==team2]
    return df4.to_html()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
