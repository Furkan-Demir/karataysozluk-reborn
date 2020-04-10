from flask import Flask, render_template, request, redirect, url_for, session , Blueprint


profile = Blueprint('profile', __name__)

@profile.route('/<user_id>')
def profil(user_id):
    return user_id

@profile.route('/profile')
def tete():
    return render_template("profil.html")