from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
from prediction_model import PredictionModel
import pandas as pd
from random import randrange
import os
from forms import  OriginalTextForm
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

UPLOAD_FOLDER = 'screenshots'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = '4c99e0361905b9f941f17729187afdb9'

def image_to_text(url):
    im = Image.open(url)
    text = pytesseract.image_to_string(im, lang = 'eng')
    return text

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET','POST'])
def home():
   return render_template('index.html')
	
@app.route('/image_check', methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      url = 'E:\\DR_NEWS\\src\\screenshots\\'+filename
      news = image_to_text(url)
      model = PredictionModel(news)
      return render_template('image_check.html', output=model.predict())
    
    return render_template('image_check.html',output=False)


@app.route("/text_check", methods=['POST', 'GET'])
def upload_text():
    form = OriginalTextForm()

    if form.generate.data:
        data = pd.read_csv("random_dataset.csv")
        index = randrange(0, len(data)-1, 1)
        original_text = data.loc[index].text
        form.original_text.data = str(original_text)
        return render_template('text_check.html', form=form, output=False)

    elif form.predict.data:
        if len(str(form.original_text.data)) > 10:
            model = PredictionModel(form.original_text.data)
            return render_template('text_check.html', form=form, output=model.predict())

    return render_template('text_check.html', form=form, output=False)


if __name__ == '__main__':
   app.run(debug=True,port=5000)
