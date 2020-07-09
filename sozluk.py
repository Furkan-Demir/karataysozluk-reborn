from flask import Flask, render_template, request, redirect, url_for, session , Blueprint
from controller import VeritabaniEkle, Ara, Aratek, baslikvarmi, Ara_detayli, Basliklar
import datetime
import sqlite3
sozluk = Blueprint('sozluk', __name__)

@sozluk.route('/baslik/')
def baslikk():
    return render_template("basliklar.html")

@sozluk.route('/baslik/<idim>',methods = ["POST","GET"])
def baslik_idli(idim):
    if 'id' in session:
        if request.method == "GET":
            verilerim = Aratek("baslik","baslik_link_name = '"+idim+"'")
            baslik_id = verilerim[0]
            baslik_name = verilerim[2]
            
            entryler = Ara_detayli("entry.entry_entry,entry.entry_tarih,entry_puan,users.user_nick,users.user_pp","users,entry","entry_baslik = '"+str(baslik_id)+"' AND user_id = entry_sahip_id")
            return render_template("baslik.html",entryler = entryler,baslik_name = baslik_name,idim=idim)
        elif request.method == "POST":
            entry = request.form["entrygir"]
            entry = entry.lower()
            entry = entry.replace("\r\n", " ")
            if len(entry) > 5:
                sorgu = "entry (entry_entry,entry_tarih,entry_sahip_id,entry_baslik,entry_puan)"
                verilerim = Aratek("baslik","baslik_link_name = '"+idim+"'")
                baslik_id = verilerim[0]                
                tarihim = datetime.datetime.now()
                tarihim = tarihim.strftime("%H:%M %d.%m.%Y")
                veri = (entry,tarihim,session["id"],baslik_id,"0")
                VeritabaniEkle(sorgu,veri)
                return redirect(url_for("sozluk.baslik_idli",idim = idim))
            return redirect(url_for("sozluk.baslik_idli",idim = idim))

@sozluk.route('/baslik/yeni',methods = ["POST","GET"])
def yenibaslikac():
    if request.method == "GET":
        return render_template("baslikac.html")
    elif request.method == "POST":
        baslik = request.form["baslik"]
        baslik = baslik.lower()
        ilkentry = request.form["ilkentry"]
        print(baslik,ilkentry)
        ilkentry = ilkentry.replace("\r\n", " ")
        baslik = baslik.replace("\r\n", "")
        baslik_link_name = baslik.replace(" ", "-")
        baslik_link_name = baslik_link_name.replace("ğ", "g")
        baslik_link_name = baslik_link_name.replace("ı", "i")
        baslik_link_name = baslik_link_name.replace("ç", "c")
        baslik_link_name = baslik_link_name.replace("ö", "o")
        baslik_link_name = baslik_link_name.replace("ü", "u")
        baslik_link_name = baslik_link_name.replace("ş", "s")
        baslik_tarih = datetime.datetime.now()
        baslik_tarih = baslik_tarih.strftime("%d.%m.%Y")
        if len(baslik) < 3 or len(ilkentry) < 5 or baslikvarmi(baslik) == False:
            return render_template("baslikac.html",hata = "Başlık 3 karakter veya Entry 5 karakterden az olamaz.")
        else:
            yer = "baslik(baslik_sahip_id,baslik_name,baslik_link_name,baslik_tarih)"
            veri = (session['id'],baslik,baslik_link_name,baslik_tarih)
            VeritabaniEkle(yer,veri)
            verilerim = Aratek("baslik","baslik_link_name = '"+baslik_link_name+"'")

            yer2 = "entry(entry_sahip_id,entry_entry,entry_tarih,entry_puan,entry_baslik)"
            veri2 = (session['id'],ilkentry,baslik_tarih,"0",verilerim[0],)
            VeritabaniEkle(yer2,veri2)

            return redirect(url_for("sozluk.baslik_idli",idim = verilerim[3]))
        return render_template("baslikac.html")


@sozluk.route('/',methods = ["POST","GET"])
def sozlukanasayfa():
    if request.method == "GET":
        if 'id' in session:
            sorgum = "duvar.duvar_onay = 1 AND duvar.duvar_sahip_id = users.user_id ORDER BY duvar_id desc"
            duvar_postlar = Ara("duvar, users",sorgum)
            gundem = Basliklar("baslik","baslik_puan DESC")
            yeni = Basliklar("baslik","baslik_id DESC")
            # 0 = duvar_id
            # 1 = user_id
            # 2 = duvar_yazi
            # 3 = duvar_puan
            # 4 = duvar_tarih
            # 5 = duvar_onay
            # 7 = user_nick
            return render_template("anasayfa.html",duvar_postlar = duvar_postlar,gundem=gundem,yeni=yeni)
        else:
            return redirect(url_for("auth.login"))
            
    elif request.method == "POST":
        print("request formum: ",request.form["duvaryazi"])
        duvar_yazisi = request.form["duvaryazi"]        
        duvar_yazisi = duvar_yazisi.replace("\r\n", " ")
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
