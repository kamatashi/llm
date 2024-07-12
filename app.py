from flask import Flask, request, render_template
from transformers import pipeline
from deep_translator import GoogleTranslator
import numpy as np

app = Flask(__name__)

# Load the zero-shot classification pipeline
classifier = pipeline("zero-shot-classification")

# Define candidate labels for classification
candidate_labels = [
    "excellent performance", 
    "good performance", 
    "average performance", 
    "poor performance"
]

# Custom scoring function based on classification label
def custom_score(label, score):
    if label == "excellent performance":
        return score
    elif label == "good performance":
        return score * 0.75
    elif label == "average performance":
        return score * 0.5
    else:
        return score * 0.25

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Get the input text from the form
        text = request.form['text']

        if not text.strip():
            return render_template('index.html', result=None, error="Por favor insira uma descrição válida.")

        # Translate the text to English
        translated_text = GoogleTranslator(source='auto', target='en').translate(text)

        # Perform zero-shot classification on the translated text
        classification_result = classifier(translated_text, candidate_labels)
        label = classification_result['labels'][0]
        score = classification_result['scores'][0]

        # Convert the classification label to a custom score
        final_score = custom_score(label, score)

        # Prepare the result for rendering
        if label == "excellent performance":
            label = "Performance excelente"
        elif label == "good performance":
            label = "Performance boa"
        elif label == "average performance":
            label = "Performance média"
        else:
            label = "Performance ruim"

        result = {
            'description': text,
            'translated_description': translated_text,
            'label': label,
            'score': score,
            'final_score': final_score
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
