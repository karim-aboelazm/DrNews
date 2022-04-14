from flask import (Flask, 
                  jsonify, 
                  render_template, 
                    )
from prediction_model import PredictionModel
import pandas as pd
from random import randrange
from forms import OriginalTextForm


app = Flask(__name__)

app.config['SECRET_KEY'] = '4c99e0361905b9f941f17729187afdb9'


@app.route("/", methods=['POST', 'GET'])
def home():
    form = OriginalTextForm()

    if form.generate.data:
        data = pd.read_csv("random_dataset.csv")
        index = randrange(0, len(data)-1, 1)
        original_text = data.loc[index].text
        form.original_text.data = str(original_text)
        return render_template('index.html', form=form, output=False)

    elif form.predict.data:
        if len(str(form.original_text.data)) > 10:
            model = PredictionModel(form.original_text.data)
            return render_template('index.html', form=form, output=model.predict())

    return render_template('index.html', form=form, output=False)


if __name__ == '__main__':
   app.run(debug=True,port=5000)
