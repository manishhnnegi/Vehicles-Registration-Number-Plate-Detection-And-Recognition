from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin  # for multiple ip eroror
from com_in_ai_utils.utils import decodeImage
from predict import dogcat
import cv2
import time
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')
PEOPLE_FOLDER = os.path.join('static', 'uploads')

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = dogcat(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
#def home():
    #return render_template('index.html')
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'img.png')
    #return render_template('index.html')
    return render_template("index.html",user_image = full_filename)

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result, img = clApp.classifier.predictiondogcat()
    return jsonify(result)



# port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    # app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=8000, debug=True)
