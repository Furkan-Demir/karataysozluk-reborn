from flask import Flask, render_template, request, redirect, url_for, session ,Blueprint
from controller import Ara, VeritabaniEkle, UserVarmi

auth = Blueprint('auth', __name__)

@auth.route('/giris',methods = ["POST","GET"])
def login():
    if request.method == 'POST':
        nick = request.form['nick']
        password = request.form['password']
        print(nick,password)
        sorgum = "user_nick = " +"'"+nick +"'"+" AND user_password = " + "'"+ password + "'"
        user = Ara("users",sorgum)
        if user:
            if user["password"] == password:
                session['nick'] = user['nick']
                session['email'] = user['email']
                session['name'] = user['name']
                session['id'] = user['id']
                return redirect(url_for('sozluk.sozlukanasayfa'))
            else:
                bildirim = "Kullanıcı adı veya Şifre yanlış"
                return render_template("giris.html",bildirim = bildirim)
        else:
            return render_template("giris.html",bildirim = "Giriş Bilgileri Hatalı!")
    else:
            return render_template('giris.html')

@auth.route('/kayit',methods = ["POST","GET"])
def register():
    if 'id' in session:
        return redirect(url_for('sozluk.sozlukanasayfa'))
    else:
        if request.method == 'GET':
            return render_template("kayit.html")
        else:
            nick = request.form['nick']
            email = request.form['email']
            password = request.form['password']
            bilgim = UserVarmi(nick)
            if bilgim == True:
                if len(nick) < 2:
                    return render_template("kayit.html", hata = "Kullanıcı Adınız 2 Karakterden Fazla Olmalıdır")
                else:
                    yer = "users(user_nick,user_password,user_email)"
                    veri = (nick,password,email)
                    VeritabaniEkle(yer,veri)
                    return redirect(url_for('auth.login'))
            else:
                return render_template("kayit.html", hata = "Kullanıcı Adı kullanılıyor.")