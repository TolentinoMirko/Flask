#realizzare un server web che permetter di effettuare il login
#l'utente inserisce l'username e la password
#se l'usuername è admin e la password è xxx123## il sito ci saluta con un messggio di benvenuto
#altrimenti ci da un messaggio di errore

from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
 return render_template("login.html")

@app.route('/data', methods=['GET'])
def data():
    ad = request.args['Username']
    pas = request.args['Password']
    if ad == "admin" and pas =='xxx123##':
      return render_template("welcome.html",admin = ad)
    else:
        return ('<h1>Error</h1>')




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)