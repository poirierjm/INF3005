# coding: utf8

from flask import Flask, render_template

app = Flask(__name__, static_url_path="", static_folder="static") #Ou le css, les images et le js sont entreposer, tout ce qui est static


@app.route('/')
def page_accueil():
    return render_template('accueil.html')


@app.route('/inf3005/')
def page_prog_web_avancee():
    return render_template('inf3005.html')