# server web che permetta di conoscere capoluoghi di regione
# l'utente inserisce il nome della regione e il programma restituisce il
# capoluogo di regione
# caricare i capoluoghi di regione e le regioni in una opportuna
# struttura dati

# modificare poi l'es precedente per permettere all'utente di inserire
# un capoluogo e di avere la regione in cui si trova
# l'utente sceglie se avere il capoluogo o la regione selezionando un
# radio button

from flask import Flask, render_template, request
app = Flask(__name__)
CapoluoghiRegioni = {'Abruzzo': 'LAquila', 'Basilicata': 'Potenza', 'Calabria': 'Catanzaro', 'Campania': 'Napoli', 'EmiliaRomagna': 'Bologna', 'Friuli': 'Trieste', 'Lazio': 'Roma', 'Liguria': 'Genova', 'Lombardia': 'Milano',
                     'Marche': 'Ancona', 'Molise': 'Campobasso', 'Piemonte': 'Torino', 'Puglia': 'Bari', 'Sardegna': 'Cagliari', 'Sicilia': 'Palermo', 'Toscana': 'Firenze', 'Trentino': 'Trento', 'Umbria': 'Perugia', 'ValledAosta': 'Aosta', 'Veneto': 'Venezia'}


@app.route('/', methods=['GET'])
def home():

    return


@app.route('/trcapoluogo', methods=['GET'])
def capoluogo():
    regione = request.args['Regione']

    for reg in CapoluoghiRegioni:
         if reg == regione:
           namcapoluogo = utente.values
    return render_template('appes3/trcapoluogo.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
