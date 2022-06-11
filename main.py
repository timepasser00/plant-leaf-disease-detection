from distutils.log import debug
from flask import Flask, render_template,request,redirect,url_for
import os
import prediction

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",data = "Nhi hai kcho")
@app.route("/", methods = ['POST', 'GET'])
def uploader():
    if request.method == 'GET':
        return "ok"
    if request.method == 'POST':
        image = request.files['fname']
        # prediction.predict(image)
    return prediction.predict(image)

@app.route("/result",methods=["post"])
def result():
    if request.method == 'POST':
        image = request.files['fname']
        # prediction.predict(image)
        result = prediction.predict(image)
        return render_template("index.html",data = result)
    return render_template("index.html",data = "Error")
    
    

if __name__ == "__main__":
    app.run(debug = True)