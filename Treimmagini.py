from flask import Flask, render_template
import random
import datetime
app = Flask(__name__)


@app.route('/', methods=['GET'])
def TreImmagi():
    return render_template('IndexTreImag.html')


@app.route('/meteo', methods=['GET'])
def Casuale():
    rand = random.randint(0, 8)
    if rand < 2:
        mete = "pioggia"
        immag = "static/pioggia.jpg"
    elif rand > 3 & rand < 5:
        mete = "nuvoloso"
        immag = "static/nuvoloso.jpg"
    else:
        mete = "soleggiato"
        immag = "static/soleggiato.jpg"
    return render_template("meteo.html", meteo=mete, immagine=immag)


@app.route('/frasi', methods=['GET'])
def Fras():
    frasi = [
        {"frase": "“Thinking you are no-good and worthless is the worst thing you can do",
            "autore": "Nobito"},
        {"frase": "Don’t give up, there’s no shame in falling down! True shame is to not stand up again!", "autore": "Shintaro"},
        {"frase": "If you don’t like your destiny, don’t accept it.", "autore": "Naruto"},
        {"frase": "bum bum bakuda", "autore": "Klee"},
        {"frase": "osmanthus wine taste the same as i remember but where are those who share the memory", "autore": "Zhongli"},
        {"frase": "potato", "autore": "Razor"},
        {"frase": "Inazuma no tameni", "autore": "Raiden"},
        {"frase": "Hehe", "autore": "Venti"},
        {"frase": "Hehe te nandayo", "autore": "Paimon"}
    ]
    rando = random.randint(0, len(frasi)-1)

    frase = frasi[rando]['frase']
    autore = frasi[rando]['autore']
    return render_template("frasi.html", fra=frase, aut=autore)


@app.route('/calendario', methods=['GET'])
def Calendario():

    now = datetime.datetime.now()
    school = datetime.datetime(2022, 6, 8)
    return render_template("calendario.html", data=(school - now).days)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
