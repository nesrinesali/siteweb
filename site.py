from flask import Flask, render_template, request
import random
app = Flask(__name__)

# Liste de questions
questions = [
    {
        'question': 'Quelle est la capitale de la France ?',
        'answer': 'Paris'
    },
    {
        'question': 'Quelle est la capitale de l\'Espagne ?',
        'answer': 'Madrid'
    },
]

# Page d'accueil
@app.route('/')
def home():
    return render_template('index.html', question=random.choice(questions)['question'])

# Évaluation de la réponse
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
