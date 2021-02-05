# app/__init__.py
# coding: utf-8

from flask import Flask, request, render_template
from random import randint
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('db/patients.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/transb/')
def index():
    id = 1
    conn = get_db_connection()
    chambres = conn.execute('SELECT N_ch, nom, age FROM chambres WHERE id=?', (id,)).fetchone()
    conn.close()
    return render_template('trans.html', posts=chambres)


@app.route('/')
def my_form():
    return render_template('myform.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    # processed_text = text.upper()
    return text


@app.route('/transX/')
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

    citation2 = str(characters[get_random_item(characters)].capitalize() + " à dit: " +
                    (quotes[get_random_item(quotes)]))

    # user_answer = input("Appuyer sur la touche ENTER pour continuer ou \"F\" pour quitter")
    return render_template('trans.html', citation=citation, citation2=citation2, title='MyQuote')


@app.route('/trans/')
def homepage2():

    characters = [
        "Alvin",
        "Joe",
        "Siegfried",
        "babar",
        "casper",
        "Kirikou",
    ]

    quotes = [
        "IDS",
        "TS",
        "TSM",
        "HOR",
        "SLG",
        "TPC",
    ]

    comm1 = [
        "Aller Potiron",
        "Allergie Carotte",
    ]

    comm2 = [
        "Test",
        "",
    ]

    info = [
        "",
        "",
    ]

    ch1_name = str(characters[0].capitalize())
    ch1_hospi = str(quotes[0])
    ch1_comm1 = str(comm1[0])
    ch1_comm2 = str(comm2[0])
    ch1_info = str(info[0])
    ch2_name = str(characters[1].capitalize())
    ch2_hospi = str(quotes[1])
    return render_template('trans.html',
                           ch1_name=ch1_name, ch1_hospi=ch1_hospi, ch1_comm1=ch1_comm1, ch1_comm2=ch1_comm2,
                           ch1_info=ch1_info,
                           ch2_name=ch2_name, ch2_hospi=ch2_hospi, ch2_comm1=ch1_comm1, ch2_comm2=ch1_comm2,
                           ch2_info=ch1_info,
                           title='MyQuote')


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
