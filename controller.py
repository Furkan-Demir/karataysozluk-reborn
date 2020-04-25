import sqlite3


veritabani=sqlite3.connect('database.db',check_same_thread=False)
if(veritabani):
    print('Baglanti Başarılı!')
else:
    print('Bağlantı Başarısız!')

def VeritabaniKur():
    try:
        with veritabani:
            _cursor = veritabani.cursor()
            sorgu = """CREATE TABLE IF NOT EXISTS duvar(
            duvar_id INTEGER PRIMARY KEY,
            duvar_sahip_id VARCHAR(50),
            duvar_text VARCHAR(255),
            duvar_puan VARCHAR(255),
            duvar_tarih VARCHAR(255),
            duvar_onay VARCHAR(255)
            )"""
            _cursor.execute(sorgu)

            _cursor = veritabani.cursor()
            sorgu = """CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            user_nick VARCHAR(50),
            user_password VARCHAR(255),
            user_email VARCHAR(255),
            user_bio VARCHAR(255),
            user_face VARCHAR(255),
            user_twitter VARCHAR(255),
            user_insta VARCHAR(255)
            )"""
            _cursor.execute(sorgu)
            print("User Basarili!")

            _cursor = veritabani.cursor()
            sorgu = """CREATE TABLE IF NOT EXISTS baslik(
            baslik_id INTEGER PRIMARY KEY,
            baslik_sahip_id VARCHAR(50),
            baslik_name VARCHAR(255),
            baslik_link_name VARCHAR(255),
            baslik_tarih VARCHAR(255)
            )"""
            _cursor.execute(sorgu)

            _cursor = veritabani.cursor()
            sorgu = """CREATE TABLE IF NOT EXISTS entry(
            entry_id INTEGER PRIMARY KEY,
            entry_sahip_id VARCHAR(50),
            entry_entry TEXT,
            entry_tarih VARCHAR(255),
            entry_puan VARCHAR(255)
            )"""
            _cursor.execute(sorgu)

            veritabani.commit()
        
    except:
        print("User Basarisiz!")


def VeritabaniEkle(yer,bilgi):## injection fixlenicek 
    ## yer = "users(user_nick,user_password,user_email)"
    ## bilgi = ("test","userpass","useremail")
    with veritabani:
        _cursor = veritabani.cursor()
        _cursor.execute("INSERT INTO "+ yer +" VALUES "+ str(bilgi))
        veritabani.commit()

    


def UserVarmi(nick):
    ## injection fixlenicek
    with veritabani:
        im = veritabani.cursor()
        im.execute("""SELECT * FROM users WHERE user_nick = ?""",(nick,))
        verilerx = im.fetchone()
        print("verilerx : ",verilerx)
        if verilerx == None:
            return True
        else:
            return False

def baslikvarmi(nick):
    ## injection fixlenicek
    with veritabani:
        im = veritabani.cursor()
        im.execute("""SELECT * FROM baslik WHERE baslik_name = ?""",(nick,))
        verilerx = im.fetchone()
        print("verilerx : ",verilerx)
        if verilerx == None:
            return True
        else:
            return False


def Ara_detayli(cekilecek,yer,sorgu): ## injection fixlenicek
    ## yer = users
    ## sql_yeri = user_nick
    ## sorgu = nick
    with veritabani:
        im = veritabani.cursor()
        im.execute("SELECT "+ cekilecek +" FROM " + yer + " WHERE " + sorgu)
        veriler = im.fetchall()
        return veriler

def Basliklar(yer,sorgu): ## injection fixlenicek
    ## yer = users
    ## sql_yeri = user_nick
    ## sorgu = nick
    with veritabani:
        im = veritabani.cursor()
        im.execute("SELECT baslik_link_name,baslik_name,baslik_puan FROM " + yer + " ORDER BY " + sorgu)
        veriler = im.fetchall()
        return veriler

def Ara(yer,sorgu): ## injection fixlenicek
    ## yer = users
    ## sql_yeri = user_nick
    ## sorgu = nick
    with veritabani:
        im = veritabani.cursor()
        im.execute("SELECT * FROM " + yer + " WHERE " + sorgu)
        veriler = im.fetchall()
        return veriler

def Aratek(yer,sorgu): ## injection fixlenicek
    ## yer = users
    ## sql_yeri = user_nick
    ## sorgu = nick
    with veritabani:
        im = veritabani.cursor()
        im.execute("SELECT * FROM " + yer + " WHERE " + sorgu)
        veriler = im.fetchone()
        return veriler

def nick_kontrol(nick):
    liste = ["'","!","^","+","#","$","½","%","&","/","{","(","[",")","]","=","}","?","*","-","_",'"',".",",","ı","ğ","ü","ç","ö"]
    for i in liste:
        if nick.find(i) != -1:
            print(nick,i)
            return False
    
    return True


VeritabaniKur()
