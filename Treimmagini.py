from flask import Flask,render_template
import random
app = Flask(__name__)

@app.route('/', methods=['GET'])
def TreImmagi():
    return render_template ('IndexTreImag.html')

@app.route('/meteo', methods=['GET'])
def Casuale():
    rand = random.randint(0,8)
    if rand < 2:
        mete = "pioggia"
        immag = "static/pioggia.jpg"
    elif rand > 3 & rand < 5:
        mete = "nuvoloso"
        immag = "static/nuvoloso.jpg"
    else:
        mete="soleggiato"
        immag = "static/soleggiato.jpg"
    return render_template("meteo.html",meteo=mete,immagine=immag)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)