# Karatay Sözlük Reborn (WIP)

Karatay Sözlük Reborn versiyonu daha okunaklı, daha modüler olucak. Şuan geliştirilme aşamasındadır.

## Paketler

```bash
Python 3.x
pip install flask
pip install sqlite3

```

## Güncelleme Notları
V1.0.0 
- Taslak blueprint'ler oluşturuldu.
- Controller oluşturuldu ve temel fonksiyonları yazıldı.
- (Auth) Login / Register fonksiyonları basitçe yazıldı. Hash ve injectionlar ileride yazılacak.

V1.0.1
- Auth artık session döndürebiliyor. (İlk halinde unutmuşum :D)
- Login ve Register'da lowercase kullanıyorum. Ayrıca özel işaretler de engellendi.
- Controller'a birkaç ekleme yapıldı. (Auth'un kullanacağı fonksiyonlar)

V1.0.2
- Duvar post request. (anasayfa)
- Eğer duvar_onay = 1 anasayfada gözüküyor.