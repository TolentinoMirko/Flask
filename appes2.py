# realizzare un sito web che permetta la registrazione degli utenti
# l'utente inserisce il nome ,un username una password,la conferma della password e
# il sesso. se le info  sono corrette il sito salva le info in una struttura dati opportuna

# prevedere la possibilità di fare il login
# inserendo l'username e password
# se sono correte fornire un messaggio di benvenuto diverso a seconda del sesso

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template("appes2/registeres2.html")


@app.route('/data', methods=['GET'])
def regi():
    name = request.args['Name']
    user = request.args['Username']
    pasw = request.args['Password']
    conpasw = request.args['ConfPassword']
    gender = request.args["Sex"]

    lst = []

    if name == '' or user == '' or pasw == '' or conpasw == '' :
        return('<h1>Error</h1>')
    else:
        lst.append({'nome': name,'username': user,'password': pasw,'gender': gender})

        return render_template("appes2/welcomees2.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
