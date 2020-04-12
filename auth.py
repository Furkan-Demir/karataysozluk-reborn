from flask import Flask, render_template, request, redirect, url_for, session ,Blueprint
from controller import Ara, VeritabaniEkle, UserVarmi, nick_kontrol

auth = Blueprint('auth', __name__)

@auth.route('/giris',methods = ["POST","GET"])
def login():
    if request.method == 'POST':
        nick = request.form['nick']
        password = request.form['password']
        nick = nick.lower()
        print(nick,password)
        sorgum = "user_nick = " +"'"+nick +"'"+" AND user_password = " + "'"+ password + "'"
        user = Ara("users",sorgum)
        print(user)
        if user:
            if user[0][2] == password:
                session['nick'] =  user[0][1]
                session['email'] = user[0][4]
                session['id'] = user[0][0]
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
            nick = nick.lower()
            print("request form= ", request.form)
            bilgim = UserVarmi(nick)
            if bilgim == True and nick_kontrol(nick) == True:
                
                if len(nick) < 2:
                    return render_template("kayit.html", hata = "Kullanıcı Adınız 2 Karakterden Fazla Olmalıdır")
                else:
                    yer = "users(user_nick,user_password,user_email)"
                    veri = (nick,password,email)
                    VeritabaniEkle(yer,veri)
                    return redirect(url_for('auth.login'))
            else:
                return render_template("kayit.html", hata = "Kullanıcı Adı kullanılıyor veya özel karakter içeriyor.")



@auth.route('/cikis')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))