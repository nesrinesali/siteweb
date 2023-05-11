from flask import Flask, render_template, request
import random
import json
app = Flask(__name__)

with open('questions.json') as json_file:
    questions = json.load(json_file)

@app.route('/')
def home():
    return render_template('index.html', question=random.choice(questions)['question'])

@app.route('/evaluate', methods=['POST'])
def evaluate():
    user_answer = request.form['answer']
    question = request.form['question']

    # Trouver la réponse attendue pour la question donnée
    for q in questions:
        if q['question'] == question:
            expected_answer = q['answer']
            break

    # Vérifier si la réponse de l'utilisateur est correcte ou non
    if user_answer.lower() == expected_answer.lower():
        result = 'Réponse validée !'
    else:
        result = 'Réponse incorrecte !'

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)
