# si vuole realizzare un sito web per memorizzare le squadre di uno sport a scelta
# l'utente deve poter inserire il nome della squadra e la data di fondazione e la
# città.

# deve inoltre poter effettuare delle ricerche inserendo uno dei valori delle colonne
# e ottenendo i dati presenti.

from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

#dfvuoto = pd.DataFrame(columns=['Squadra','Data Fondazione','Città'])
df = pd.read_csv('/workspace/Flask/templates/appes5/dati.csv')


@app.route('/', methods=['GET'])
def home():

    return render_template('/appes5/appes5home.html')

@app.route('/data', methods=['GET'])
def data():
    team = request.args['Squadra']
    year = request.args['Anno']
    city = request.args['Citta']
    df= pd.read_csv('/workspace/Flask/templates/appes5/dati.csv')
    
    df2 = ({'Squadra':team},{'Anno':year},{'Citta':city})
    df = df.append(df2,ignore_index=True)
    return()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
