from distutils.log import debug
import imp
from flask import Flask, render_template,request,jsonify
import os
import prediction
import io
from base64 import b64encode, encode
from PIL import Image
from io import BytesIO
app = Flask(__name__)

data = {
    "resultAvail" : False,
     "img_data" : "",
     "result" : ""
}

@app.route("/")
def index():
    data = {
        "resultAvail" : False,
        "img_data" : "../static/upload.png",
        "result" : ""
    }
    data1 = "../static/upload.png"
    # im = Image.open()
    # data = io.BytesIO()
    # im.save(data, "JPEG")
    # encoded_img_data = base64.b64encode(data.getvalue())

    return render_template("index.html",data_param=data, image_preview =data1)

@app.route("/analyse",methods=["post"])
def result():
    
    if request.method == 'POST':
        image = request.files['fname']
        result = prediction.predict(image) 
        img = Image.open(image)
        
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        encoded = b64encode(buffered.getvalue())
        # print(encoded.decode('UTF-8'))
        # mime = "image/jpeg"
        # uri = "data:%s; base64,%s" %(mime,encoded.decode())
        uri = f"data:image/jpeg;base64,{encoded.decode('UTF-8')}"
        data = {
            "resultAvail" : True,
            "img_data" : uri,
            "result" : result
        }
        return render_template("index.html",data_param = data)
    return render_template("index.html")
    
    

if __name__ == "__main__":
    app.run(debug = True)