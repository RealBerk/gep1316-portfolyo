# datetime kütüphanesinden sadece 'datetime' sınıfını içe aktarıyoruz
# Bu sınıf sayesinde bilgisayarın o anki tarih ve saat bilgisine ulaşabiliriz
from datetime import datetime

# Kullanıcıdan adını istiyoruz
# input() fonksiyonu ekrana bir soru yazdırır ve kullanıcının klavyeden yazdığı cevabı metin (str) olarak döndürür
ad = input("Adınızı girin: ")

# Adın boş veya sadece boşluklardan oluşup oluşmadığını kontrol ediyoruz
# strip() metnin başındaki ve sonundaki boşlukları temizler; "   " -> "" olur
if ad.strip() == "":
    # Ad boşsa program devam etmesin, uyarı verip çıkalım
    print("Hata: Ad alanı boş bırakılamaz! Lütfen adınızı girin.")
else:
    # Bilgisayarın şu anki tarihinden sadece yıl bilgisini alıyoruz
    # datetime.now() şu anki tarih-saati verir, .year ise bunun sadece yıl kısmını (ör. 2026) verir
    simdiki_yil = datetime.now().year

    # Doğum yılı girişini geçersiz değerlere karşı koruyoruz
    # try bloğu: hata çıkabilecek kod buraya yazılır
    try:
        # Kullanıcıdan doğum yılını istiyoruz
        # input() her zaman metin döndürdüğü için int() ile bu metni tam sayıya çeviriyoruz
        dogum_yili = int(input("Doğum yılınızı girin: "))
    except ValueError:
        # int() çeviremezse (ör. "abc", "2000.5", boş giriş) ValueError hatası fırlatılır
        # Bu durumda program çökmez; kullanıcıya uyarı verip çıkıyoruz
        print("Hata: Lütfen doğum yılınızı tam sayı olarak girin (ör. 2000).")
    else:
        # int() başarılı olduysa burası çalışır
        # Doğum yılı gelecekte mi veya mantıksız mı (0 ya da negatif)?
        if dogum_yili > simdiki_yil:
            # Gelecekteyse yaş hesaplamaya gerek yok, uyarı veriyoruz
            print("Hata: Doğum yılı gelecekte olamaz! Lütfen geçerli bir yıl girin.")
        elif dogum_yili <= 0:
            # 0 veya negatif yıl mantıksızdır (ör. -5 veya 0)
            print("Hata: Doğum yılı 0'dan büyük olmalıdır.")
        else:
            # Doğum yılı geçerliyse yaşı hesaplıyoruz: şimdiki yıldan doğum yılını çıkarıyoruz
            yas = simdiki_yil - dogum_yili

            # Kişiye özel karşılama mesajını ekrana yazdırıyoruz
            # f-string (f"...") sayesinde {ad} ve {yas} gibi süslü parantez içindeki değişkenler metnin içine yerleştirilir
            print(f"Merhaba {ad.strip()}! {yas} yaşındasınız. Hoş geldiniz!")