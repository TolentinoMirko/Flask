from flask import Flask, render_template
app = Flask(__name__)
from datetime import datetime
now = datetime.now()
@app.route('/', methods=['GET'])
def time():
  now = datetime.now()
  if now.hour < 7:
        return render_template("indexOrario.html", time=f"{now.hour}:{now.minute}:{now.second}", color="cyan")
  elif now.hour < 13:
      return render_template("indexOrario.html", time=f"{now.hour}:{now.minute}:{now.second}", color="yellow")
  elif now.hour < 18:
      return render_template("indexOrario.html", time=f"{now.hour}:{now.minute}:{now.second}", color="orange")
  else:
      return render_template("indexOrario.html", time=f"{now.hour}:{now.minute}:{now.second}", color="blue")
      
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
