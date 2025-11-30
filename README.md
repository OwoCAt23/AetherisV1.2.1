# AetherisV1.2.1
AETHERIS 
Genel Bakış

Aetheris Script (ASS), basit ve anlaşılır bir programlama dili olarak tasarlanmıştır. Türkçe komut seti ile kullanıcı dostu bir arayüz sunar.

Temel Yapı

Her Aetheris Script kodu main_code; ifadesi ile sonlanmalıdır. Kodlar satır satır işlenir ve her komut noktalı virgül ile bitmelidir.

Syntax Kuralları

· Komutlar büyük/küçük harf duyarlıdır
· Her komut noktalı virgül ile bitmelidir
· Değişkenler Input komutu ile oluşturulur
· Yorum satırları // ile başlar

Temel Komutlar

Ekran Çıktısı

```aetheris
Printitle("Merhaba Dunya");
Printcolor("mavi");
Printitle("Mavi renkli metin");
```

Kullanıcı Girdisi

```aetheris
Input("isim:");
Intask("Merhaba {isim}");
```

Matematik İşlemleri

```aetheris
math(15+27);
math(50-18);
math(8×9);
math(100÷4);
```

Kontrol Yapıları

```aetheris
// Seçim yapısı
Or();
Printitle("A: Secenek 1");
Printitle("B: Secenek 2");
Input("secim:");
Or.choose();

Order();
Printitle("Secenek 1 secildi"); (A)
Printitle("Secenek 2 secildi"); (B)
```

Fonksiyonlar

```aetheris
func<Selamla>(isim);
    f.Printitle("Merhaba {isim}");
end.func

Call.func<Selamla>("Ahmet");
```

Diğer Komutlar

```aetheris
wait(3);           // 3 saniye bekle
Clear();           // Ekranı temizle
List("elma,armut"); // Liste oluştur
```

Örnek Program

```aetheris
Printcolor("mavi");
Printitle("Hesap Makinesi");
Input("sayi1:");
Input("sayi2:");
math({sayi1}+{sayi2});
main_code;
```

Hata Kodları

· A101: Printitle sözdizimi hatası
· A110: Input sözdizimi hatası
· A301: wait sözdizimi hatası
· A401: math sözdizimi hatası
· A900: main_code eksik
(daha fazla...)
Sistem Gereksinimleri

· Python 3.x
· Renk desteği olan terminal
· Internet bağlantısı (öğretici metin için) *Öğretici metin eskidir*

Sürüm Bilgisi

· Versiyon: 1.2.1C
· Kod Adı: Celestial
· Build: ASS-20241129-C

