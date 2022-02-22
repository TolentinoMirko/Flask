from flask import Flask, render_template,request
import time
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("indexOrario.html")

@app.route('/GetTime', methods=['GET'])
def GetTime():
    print('browser time: ', request.args.get("time"))
    print('server time:' time.strftime('%A %B, %d %Y %H:%M:%S'));
    return "Done")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)