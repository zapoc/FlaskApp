# app/__init__.py
# coding: utf-8

from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('myform.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    # processed_text = text.upper()
    return text


@app.route('/result/')
def homepage():
    quotes = [
        "Salut, comment va??",
        "Bsartek ca va pas mal!!!",
        "Je suis une fougere",
        "Astalavista baybay oO",
        "Cache moi ce \"Q\" que je ne saurais voir...!!!",
        "Colonel Satori, au rwaport!!!!",
    ]
    characters = [
        "Alvin",
        "Joe",
        "Siegfried",
        "babar",
        "casper",
        "Kirikou",
    ]

    def get_random_item(my_list):
        rand_numb = randint(0, len(my_list) - 1)
        return rand_numb

    citation = str(characters[get_random_item(characters)].capitalize() + " à dit: " +
                   (quotes[get_random_item(quotes)]))

    # user_answer = input("Appuyer sur la touche ENTER pour continuer ou \"F\" pour quitter")
    return render_template('result.html', citation=citation, title='MyQuote')


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
