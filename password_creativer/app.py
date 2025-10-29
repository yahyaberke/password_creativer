import random
import string   

kucuk_harfler = string.ascii_lowercase 
BUYUK_HARFLER = string.ascii_uppercase
rakamlar = string.digits
ozel_karakterler = string.punctuation

def sifre_uret():
    while True:
        try:
            uzunluk =int(input("Lütfen şifrenizin kaç haneli olması gerektiğini ve ya kaç haneden oluşmasını istediğinizi belirtiniz sistem otomatik olarak sizin istediğiniz uzunlukta bir şifre oluşturacaktır: "))
            if uzunluk <=0 :
             print("Negatif bir sayı giremezsiniz siz hiç bir şifre hanesinin sıfırdan küçük olduğunu gördünüz mü ... göremezsiniz tabii ki olamaz çünkü anlayışınız için teşekkür ederiz lütfen pozitif bir tam sayı girelim teşekkür ederim")
             continue
            break
        except ValueError:
            print("Geçersiz giriş lütfen bir giriş işlemi gerçekleştiriniz teşekkür")
    karakter_havuzu=""
    while not karakter_havuzu:
       print("\nŞifrede bulunmasını istediğiniz karakter türlerini lütfen belirtiniz") 
       if input("Harf (küçük ve büyük) kullansın mı? (e/h): ").lower() == 'e':
          karakter_havuzu += kucuk_harfler + BUYUK_HARFLER
       if input("Rakam kullansın mı? (e/h): ").lower() == 'e':
            karakter_havuzu += rakamlar   
       if input("Özel karakter (!, @, #, vb.) kullansın mı? (e/h): ").lower() == 'e':
            karakter_havuzu += ozel_karakterler
       if not karakter_havuzu:
            print("\n🚨 Uyarı: Lütfen en az bir karakter türü seçin.")

    sifre = ""
    for _ in range(uzunluk):
        rastgele_karakter = random.choice(karakter_havuzu)
        sifre += rastgele_karakter
    return sifre

if __name__ == "__main__":
    yeni_sifre = sifre_uret()
    print("-" * 40)  
    print("✅ Üretilen Güçlü Şifre:")
    print(f"   {yeni_sifre}")
    print(f"   Uzunluk: {len(yeni_sifre)}")
    print("-" * 40)
    