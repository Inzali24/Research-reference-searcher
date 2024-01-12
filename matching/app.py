from flask import Flask
from flask import request
import testMT
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:4200"])

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/getdata', methods=['GET', 'POST'])
def getThesisList():
    print("request accepted")
    if request.method == 'POST':
        return "False"
    else:
        keywords = request.args.get("keywords")
        title = request.args.get("title")
        print(title)
        data = testMT.RunAutomation(title,keywords)
        return data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) # port for docker
    #app.run(host="127.0.0.9", port=8080, debug=True) # port for local