from flask import Flask, render_template, request
from methods import *

file = ""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/uploadFile', methods=['POST'])
def upload_file():
    global file
    file = request.form['fileUpload']
    response = read_csv(file)
    df = response.head()
    return render_template("uploadFile.html", tables=[df.to_html(classes='data', header="true")], titles=df.columns.values)

@app.route('/message', methods=['POST'])
def meessage():
    columnName = request.form['columnName']
    option = request.form['option']
    nameGraph = request.form['nameGraph']
    graph_dataframe(file, columnName, option, nameGraph)
    return render_template("message.html")

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Página no encontrada</h1>"

if __name__ == '__main__':
    app.run(port=80, debug=True)