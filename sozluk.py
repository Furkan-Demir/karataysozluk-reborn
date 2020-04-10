from flask import Flask, render_template, request, redirect, url_for, session , Blueprint


sozluk = Blueprint('sozluk', __name__)

@sozluk.route('/baslik/')
def profil():
    return render_template("basliklar.html")

@sozluk.route('/')
def sozlukanasayfa():
    return render_template("anasayfa.html")