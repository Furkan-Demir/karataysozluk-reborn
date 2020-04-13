from flask import Flask, render_template, request, redirect, url_for, session , Blueprint
from controller import VeritabaniEkle, Ara
import datetime

sozluk = Blueprint('sozluk', __name__)

@sozluk.route('/baslik/')
def profil():
    return render_template("basliklar.html")

@sozluk.route('/',methods = ["POST","GET"])
def sozlukanasayfa():
    if request.method == "GET":
        if 'id' in session:
            sorgum = "duvar.duvar_onay = 1 AND duvar.duvar_sahip_id = users.user_id ORDER BY duvar_id asc"
            duvar_postlar = Ara("duvar, users",sorgum)
            
            print(duvar_postlar)
            # 0 = duvar_id
            # 1 = user_id
            # 2 = duvar_yazi
            # 3 = duvar_puan
            # 4 = duvar_tarih
            # 5 = duvar_onay
            # 7 = user_nick
            return render_template("anasayfa.html",duvar_postlar = duvar_postlar)
        else:
            return redirect(url_for("auth.login"))
    elif request.method == "POST":
        print(request.form)
        duvar_yazisi = request.form["duvaryazi"]
        duvar_onay = 0
        duvar_from = session['id']
        duvar_puan = 0
        duvar_tarih = datetime.datetime.now()
        duvar_tarih = duvar_tarih.strftime("%d.%m.%Y")
        yer = "duvar(duvar_text,duvar_sahip_id,duvar_onay,duvar_puan,duvar_tarih)"
        veri = (duvar_yazisi,duvar_from,duvar_onay,duvar_puan,duvar_tarih)
        VeritabaniEkle(yer,veri)
        return redirect(url_for("sozluk.sozlukanasayfa"))


@sozluk.route("/sozluk")
def sozlukhome():
    return render_template("sozluk.html")