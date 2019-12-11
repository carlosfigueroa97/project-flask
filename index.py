import os
from flask import Flask, render_template, request, send_from_directory
from werkzeug import secure_filename
from methods import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './pdfs/'
app.config['IMG_FOLDER'] = './img/'

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/uploadFile', methods=['POST'])
def upload_file():
    try:
        if(request.method == "POST"):
            file = request.files['fileUpload']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            f = open('filename.txt','w')
            f.write(filename)
            f.close()
            response = read_csv(filename)
            df = response.head()
        return render_template("uploadFile.html", tables=[df.to_html(classes='data', header="true")], titles=df.columns.values, filename = filename)
    except SystemError as err:
        print(err)

@app.route('/message', methods=['POST'])
def meessage():
    try:
        columnY = request.form['columnY']
        columnX = request.form['columnX']
        option = request.form['option']
        f = open('filename.txt', 'r')
        filename = f.read()
        f.close()
        nameGraph = request.form['nameGraph']
        graph_dataframe(filename, columnY, columnX, option, nameGraph, app)
        return render_template("message.html", url = nameGraph + ".png")
    except SystemError as err:
        print(err)

@app.route('/plot/<filename>')
def send_file(filename):
    return send_from_directory(app.config['IMG_FOLDER'], filename)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Página no encontrada</h1>"

if __name__ == '__main__':
    app.run(debug=True)
    