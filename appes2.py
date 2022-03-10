# realizzare un sito web che permetta la registrazione degli utenti
# l'utente inserisce il nome ,un username una password,la conferma della password e
# il sesso. se le info  sono corrette il sito salva le info in una struttura dati opportuna

# prevedere la possibilità di fare il login
# inserendo l'username e password
# se sono correte fornire un messaggio di benvenuto diverso a seconda del sesso

from flask import Flask, render_template, request
app = Flask(__name__)
lista = []


@app.route('/', methods=['GET'])
def home():
    return render_template("appes2/registeres2.html")                                                                              


@app.route('/data', methods=['GET'])
def regi():
    name = request.args["Name"]
    user = request.args["Username"]
    pasw = request.args["Password"]
    conpasw = request.args["ConfPassword"]
    gender = request.args["Sex"]
    print(request.args["Name"])
    if pasw ==conpasw:
      lista.append({'name':name,'username':user,'password':pasw,'sex':gender})
      print(lista)
      return render_template("appes2/logines2.html")
    else:
      return ('<h1>Errore</h1>')

@app.route('/login', methods=['GET'])
def log():
    user_log = request.args['Username']
    pasw_log = request.args['Password']
    
    for utente in lista:
        if utente['username'] == user_log and utente['password'] == pasw_log:
            if utente['sex'] == 'M':
                return render_template('appes2/welcomees2.html',nome_user = utente['name'])
            else:
                return render_template('appes2/welcomees2.html',nome_user = utente['name'])
                
    return ('<h1>Username or password is registered</h1>')    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
