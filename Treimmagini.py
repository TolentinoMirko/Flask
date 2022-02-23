from flask import Flask,render_template
import random
app = Flask(__name__)

@app.route('/', methods=['GET'])
def TreImmagi():
    return render_template ('IndexTreImag.html')

@app.route('/', methods=['GET'])
def Casuale():
    rand = random.randint(0,8)
    if rand < 2:
        meteo = "pioggia"
    elif rand > 3 & rand < 5:
        meteo = "nuvoloso"
    else:
        meteo="sole"



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)