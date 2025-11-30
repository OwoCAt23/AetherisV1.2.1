import time
import sys
import re
import webbrowser
from datetime import datetime

class AetherisScriptInterpreter:
    def __init__(self):
        self.variables = {}
        self.list_data = []
        self.current_color = "beyaz"
        self.screen_lines = []
        self.loop_active = False
        self.program_running = True
        self.functions = {}
        self.or_mode = False
        self.or_options = []
        self.or_input_value = None
        self.or_choices = {}
        self.or_choose_called = False
        self.time_go_repeat = 0
        
        # Aetheris bilgileri
        self.version = "1.2.1C"
        self.code_name = "Celestial"
        self.creator = "Anonim"
        self.build_id = "ASS-20241129-C"
        self.update_notes = [
            "v1.2.1C - Ayarlar menüsü eklendi",
            "v1.2.1C - CUI tasarımı yenilendi",
            "v1.2.1C - Kod modunda Help eklendi",
            "v1.2.1C - 20 örnek kod eklendi",
            "v1.2 - Order() komutu eklendi",
            "v1.1Q - Or() seçim yapısı eklendi",
            "v1.1 - Fonksiyon desteği eklendi"
        ]
        
        # Desteklenen renkler
        self.colors = {
            "beyaz": "\033[97m",
            "siyah": "\033[30m",
            "gri": "\033[90m",
            "sarı": "\033[93m",
            "mavi": "\033[94m",
            "kırmızı": "\033[91m",
            "yeşil": "\033[92m",
            "turuncu": "\033[38;5;208m",
            "pembe": "\033[95m",
            "mor": "\033[95m",
            "reset": "\033[0m"
        }
        
        # Tema ayarları
        self.theme_color = "beyaz"
    
    def clear_screen(self):
        """Ekranı temizler"""
        print("\033[2J\033[H", end="")
    
    def show_main_menu(self):
        """Ana menüyü gösterir - Yeni CUI Tasarımı"""
        self.clear_screen()
        
        
        print("\033[92m┌─────────────────────────────────────────────────────────────────────┐\033[0m")
        print("\033[92m│                                                                                                                    AETHERIS   SCRIPT MAIN MENU                               \033[0m")
        print("\033[92m└─────────────────────────────────────────────────────────────────────┘\033[0m")
        print()
        
        print(f"  \033[96m[ENTER]\033[0m  ▶  \033[97mKod Yazma Modunu Başlat\033[0m")
        print(f"  \033[96m[S]\033[0m      ▶  \033[97mSenaryolar & Örnek Kodlar\033[0m")
        print(f"  \033[96m[Q]\033[0m      ▶  \033[97mÖğretici Metin (Google Drive)\033[0m")
        print(f"  \033[96m[HELP]\033[0m   ▶  \033[97mKomut Referansı\033[0m")
        print(f"  \033[96m[SET]\033[0m    ▶  \033[97mAyarlar\033[0m")
        print(f"  \033[96m[EXIT]\033[0m   ▶  \033[97mProgramdan Çık\033[0m")
        print()
        print("\033[90m" + "─" * 70 + "\033[0m")
    
    def show_settings_menu(self):
        """Ayarlar menüsü"""
        while True:
            self.clear_screen()
            print("\033[93m")
            print("╔════════════════════════════════════════════════════════════════╗")
            print("║                         ⚙️  AYARLAR                           ║")
            print("╚════════════════════════════════════════════════════════════════╝")
            print("\033[0m")
            print()
            print(f"  \033[96m[1]\033[0m  → Tema Ayarları")
            print(f"  \033[96m[2]\033[0m  → Aetheris Hakkında")
            print(f"  \033[96m[B]\033[0m  → Ana Menüye Dön")
            print()
            
            choice = input("\033[96mAetheris SC: \033[0m").strip().upper()
            
            if choice == '1':
                self.show_theme_settings()
            elif choice == '2':
                self.show_about()
            elif choice == 'B':
                break
    
    def show_theme_settings(self):
        """Tema ayarları - Yazı rengi değiştirme"""
        self.clear_screen()
        print("\033[93m")
        print("╔════════════════════════════════════════════════════════════════╗")
        print("║                      🎨 TEMA AYARLARI                         ║")
        print("╚════════════════════════════════════════════════════════════════╝")
        print("\033[0m")
        print()
        print("Mevcut Yazı Renkleri:")
        print()
        
        available_colors = ["Beyaz", "Kırmızı", "Sarı", "Yeşil", "Turuncu", "Mor"]
        for idx, color in enumerate(available_colors, 1):
            color_code = self.colors[color.lower()]
            current = " ✓" if self.theme_color.lower() == color.lower() else ""
            print(f"  \033[96m[{idx}]\033[0m  {color_code}{color}{current}\033[0m")
        
        print()
        print(f"  \033[96m[B]\033[0m  Geri Dön")
        print()
        
        choice = input("\033[96mRenk seçin (1-6) veya [B]: \033[0m").strip()
        
        if choice.upper() == 'B':
            return
        
        try:
            idx = int(choice)
            if 1 <= idx <= len(available_colors):
                selected = available_colors[idx - 1].lower()
                self.theme_color = selected
                self.current_color = selected
                print(f"\n\033[92m✓ Tema rengi {available_colors[idx - 1]} olarak ayarlandı!\033[0m")
                time.sleep(1.5)
        except:
            pass
    
    def show_about(self):
        """Aetheris Hakkında"""
        self.clear_screen()
        print("\033[96m")
        print("╔════════════════════════════════════════════════════════════════╗")
        print("║                    ℹ️  AETHERIS HAKKINDA                      ║")
        print("╚════════════════════════════════════════════════════════════════╝")
        print("\033[0m")
        print()
        print(f"  \033[93m📌 Kod Adı:\033[0m        {self.code_name}")
        print(f"  \033[93m📌 Versiyon:\033[0m       {self.version}")
        print(f"  \033[93m📌 Yapımcı:\033[0m        {self.creator}")
        print(f"  \033[93m📌 Build ID:\033[0m       {self.build_id}")
        print()
        print("\033[92m" + "─" * 64 + "\033[0m")
        print("\033[93m📋 Güncelleme Notları:\033[0m")
        print("\033[92m" + "─" * 64 + "\033[0m")
        for note in self.update_notes:
            print(f"  • {note}")
        print()
        
        input("\n\033[93m[ENTER] tuşuna basarak geri dönün...\033[0m")
    
    def show_examples_menu(self):
        """Örnek kodlar menüsü"""
        examples = {
            "1": ("Merhaba Dünya", '''Printcolor("mavi");
Printitle("Merhaba Dünya!");
main_code;'''),
            
            "2": ("Kullanıcı Karşılama", '''Printcolor("yeşil");
Input("isim:");
Intask("Merhaba {isim}, hoş geldin!");
main_code;'''),
            
            "3": ("Basit Hesap Makinesi", '''Printcolor("sarı");
Printitle("Hesap Makinesi");
math(10+5);
math(20-8);
math(6×7);
math(100÷4);
main_code;'''),
            
            "4": ("Liste Oluşturma", '''Printcolor("turuncu");
List("Elma,Armut,Portakal,Muz");
Printitle("Liste oluşturuldu!");
main_code;'''),
            
            "5": ("Bekleme Örneği", '''Printcolor("pembe");
Printitle("3 saniye bekleniyor...");
wait(3)
Printitle("Bekleme tamamlandı!");
main_code;'''),
            
            "6": ("Tekrarlı Mesaj", '''Printcolor("mavi");
Printitle("Bu mesaj 3 kez tekrarlanır");
time.go(3)
main_code;'''),
            
            "7": ("Fonksiyon Kullanımı", '''func<Selamla>(isim);
    f.Printcolor("yeşil");
    f.Intask("Selam {isim}!");
end.func

Call.func<Selamla>("Ahmet");
Call.func<Selamla>("Ayşe");
main_code;'''),
            
            "8": ("Seçim Menüsü (Or)", '''Printcolor("mavi");
Or();
Printitle("A: Seçenek 1");
Printitle("B: Seçenek 2");
Input("secim:");
Or.choose();

main_code;'''),
            
            "9": ("Order Komutu", '''Or();
Printitle("A: Merhaba");
Printitle("B: Günaydın");
Input("A-B:");
Or.choose();

Order();
Printitle("Merhaba seçildi!"); (A)
Printitle("Günaydın seçildi!"); (B)
main_code;'''),
            
            "10": ("Renkli Çıktı", '''Printcolor("kırmızı");
Printitle("Kırmızı");
Printcolor("yeşil");
Printitle("Yeşil");
Printcolor("mavi");
Printitle("Mavi");
main_code;'''),
            
            "11": ("Çoklu Fonksiyon", '''func<Topla>(a,b);
    f.math(5+3);
end.func

func<Carpma>(x,y);
    f.math(4×6);
end.func

Call.func<Topla>("5","3");
Call.func<Carpma>("4","6");
main_code;'''),
            
            "12": ("Satır Taşıma", '''Printitle("$/İlk satır");
wait(1)
Printitle("$/İkinci satır");
wait(1)
Printitle("$/Üçüncü satır");
main_code;'''),
            
            "13": ("Anket Sistemi", '''Printcolor("sarı");
Printitle("Anket: En sevdiğiniz renk?");
Or();
Printitle("1: Kırmızı");
Printitle("2: Mavi");
Printitle("3: Yeşil");
Input("1-3:");
Or.choose();

Order();
Printitle("Kırmızı harika bir seçim!"); (1)
Printitle("Mavi çok güzel!"); (2)
Printitle("Yeşil muhteşem!"); (3)
main_code;'''),
            
            "14": ("Zamanlayıcı", '''Printcolor("kırmızı");
Printitle("5 saniye sayacı başlıyor...");
wait(1)
Printitle("4...");
wait(1)
Printitle("3...");
wait(1)
Printitle("2...");
wait(1)
Printitle("1...");
wait(1)
Printitle("Süre doldu!");
main_code;'''),
            
            "15": ("Çoklu Seçim", '''Or();
Printitle("A: Kahve");
Printitle("B: Çay");
Printitle("C: Su");
Printitle("D: Meyve Suyu");
Input("A-B-C-D:");
Or.choose();

Order();
Printitle("Kahve hazırlanıyor..."); (A)
Printitle("Çay demleniyor..."); (B)
Printitle("Su getiriliyor..."); (C)
Printitle("Meyve suyu hazırlanıyor..."); (D)
main_code;'''),
            
            "16": ("Liste İşlemleri", '''List("Pazartesi,Salı,Çarşamba");
wait(1)
List("Perşembe,Cuma");
wait(1)
Printitle("Hafta listesi tamamlandı!");
main_code;'''),
            
            "17": ("Matematik Sınav", '''Printcolor("mavi");
Printitle("Matematik Soruları");
Printitle("Soru 1:");
math(15+27);
wait(1)
Printitle("Soru 2:");
math(50-18);
wait(1)
Printitle("Soru 3:");
math(8×9);
main_code;'''),
            
            "18": ("Fonksiyon + Order", '''func<Bilgi>(mesaj);
    f.Printcolor("yeşil");
    f.Intask("Bilgi: {mesaj}");
end.func

Or();
Printitle("1: Hakkında");
Printitle("2: Yardım");
Input("1-2:");
Or.choose();

Order();
Call.func<Bilgi>("Aetheris Script v1.2"); (1)
Call.func<Bilgi>("Yardım için HELP yazın"); (2)
main_code;'''),
            
            "19": ("Ekran Temizleme", '''Printitle("Eski mesajlar...");
wait(2)
Clear();
Printitle("Ekran temizlendi!");
main_code;'''),
            
            "20": ("Kapsamlı Örnek", '''func<Menu>(baslik);
    f.Printcolor("mavi");
    f.Printitle("$/=== MENÜ ===");
    f.Intask("{baslik}");
end.func

Call.func<Menu>("Ana Menü");

Or();
Printitle("A: Başla");
Printitle("B: Ayarlar");
Printitle("C: Çıkış");
Input("A-B-C:");
Or.choose();

Order();
Printitle("Program başlatılıyor..."); (A)
Printitle("Ayarlar açılıyor..."); (B)
Printitle("Çıkış yapılıyor..."); (C)

wait(2)
Printcolor("yeşil");
Printitle("İşlem tamamlandı!");
main_code;''')
        }
        
        while True:
            self.clear_screen()
            print("\033[92m")
            print("╔════════════════════════════════════════════════════════════════╗")
            print("║                  📚 ÖRNEK KOD KÜTÜPHANESİ                    ║")
            print("╚════════════════════════════════════════════════════════════════╝")
            print("\033[0m")
            print()
            
            # Her 10 örneği grupla
            for i in range(1, 21):
                title = examples[str(i)][0]
                print(f"  \033[96m[{i:2d}]\033[0m  {title}")
                if i == 10:
                    print()
            
            print()
            print(f"  \033[96m[B]\033[0m   Ana Menüye Dön")
            print()
            
            choice = input("\033[96mÖrnek kodu görüntüle (1-20) veya [B]: \033[0m").strip().upper()
            
            if choice == 'B':
                break
            
            if choice in examples:
                self.show_example_code(examples[choice][0], examples[choice][1])
    
    def show_example_code(self, title, code):
        """Tek bir örnek kodu gösterir"""
        self.clear_screen()
        print("\033[93m")
        print("╔════════════════════════════════════════════════════════════════╗")
        print(f"║  📄 {title:^57} ║")
        print("╚════════════════════════════════════════════════════════════════╝")
        print("\033[0m")
        print()
        print("\033[90m" + "─" * 64 + "\033[0m")
        print("\033[97m" + code + "\033[0m")
        print("\033[90m" + "─" * 64 + "\033[0m")
        print()
        print("\033[92m💡 İpucu: Bu kodu kopyalayıp Kod Yazma Modunda kullanabilirsiniz\033[0m")
        print()
        
        input("\033[93m[ENTER] tuşuna basarak geri dönün...\033[0m")
    
    def show_code_mode_help(self):
        """Kod yazma modu için yardım"""
        self.clear_screen()
        print("\033[96m")
        print("╔════════════════════════════════════════════════════════════════╗")
        print("║                   📖 KOD MODU YARDIM                          ║")
        print("╚════════════════════════════════════════════════════════════════╝")
        print("\033[0m")
        print()
        print("\033[93mTEMEL KOMUTLAR:\033[0m")
        print("  • Printitle(\"metin\");     - Ekrana yazdır")
        print("  • Input(\"etiket:\");       - Kullanıcıdan girdi al")
        print("  • wait(saniye)             - Bekle (1-100)")
        print("  • math(sayı+sayı);         - Matematik işlemi")
        print("  • Clear();                 - Ekranı temizle")
        print()
        print("\033[93mDÖNGÜ:\033[0m")
        print("  • Go();                    - Sonsuz döngü")
        print("  • Stop();                  - Döngüyü durdur")
        print("  • time.go(n)               - n kez tekrarla")
        print()
        print("\033[93mFONKSİYON:\033[0m")
        print("  • func<isim>(param);       - Fonksiyon tanımla")
        print("  • end.func                 - Fonksiyonu kapat")
        print("  • Call.func<isim>(param);  - Fonksiyonu çağır")
        print()
        print("\033[93mSEÇİM:\033[0m")
        print("  • Or();                    - Seçim başlat")
        print("  • Or.choose();             - Seçimi kaydet")
        print("  • Order();                 - Seçime göre çıktı")
        print()
        print("\033[93mBİTİRME:\033[0m")
        print("  • main_code;               - Kodu bitir")
        print()
        print("\033[92m💡 Detaylı bilgi için ana menüden [HELP] seçin\033[0m")
        print()
        
        input("\033[93m[ENTER] ile devam edin...\033[0m")
    
    def show_tutorial_link(self):
        """Öğretici link sayfasını gösterir ve linki açar"""
        self.clear_screen()
        print("\033[96m")
        print("╔════════════════════════════════════════════════════════════════╗")
        print("║                    📚 ÖĞRETİCİ METİN                          ║")
        print("╚════════════════════════════════════════════════════════════════╝")
        print("\033[0m")
        print("\033[92m")
        print("📚 Detaylı öğretici metin Google Drive'da açılıyor...")
        print("Uyarı:Bu Öğretici metin V1 Versiyonunu kapsar!")
        print("🔗 Link: https://drive.google.com/file/d/1i-Ux1XCVPDWNnb3WH3EYqG74T-vMON5u/view")
        print("\033[0m")
        
        try:
            webbrowser.open("https://drive.google.com/file/d/1i-Ux1XCVPDWNnb3WH3EYqG74T-vMON5u/view")
            print("\033[92m✓ Tarayıcınızda açıldı!\033[0m")
        except:
            print("\033[91m✗ Tarayıcı açılamadı. Lütfen linki manuel kopyalayın.\033[0m")
        
        input("\n\033[93m[ENTER] tuşuna basarak ana menüye dönün...\033[0m")
    
    def show_help(self):
        """Yardım menüsünü gösterir"""
        self.clear_screen()
        help_text = """╔════════════════════════════════════════════════════════════════╗
║          AETHERIS SCRIPT (ASS) - KOMUT REFERANSI v1.2.1C      ║
╚════════════════════════════════════════════════════════════════╝

📝 TEMEL KOMUTLAR:
─────────────────────────────────────────────────────────────────
  Printitle("metin");           - Ekrana metin yazdırır
  Input("etiket:");             - Kullanıcıdan girdi alır
  Intask("Mesaj {etiket}");     - Girdi ile birlikte metin yazdırır
  Clear();                      - Ekranı temizler

⏱️ BEKLEME:
─────────────────────────────────────────────────────────────────
  wait(saniye)                  - Belirtilen süre bekler (1-100)

🔢 MATEMATİK İŞLEMLERİ:
─────────────────────────────────────────────────────────────────
  math(sayı + sayı);            - Toplama
  math(sayı - sayı);            - Çıkarma
  math(sayı × sayı);            - Çarpma
  math(sayı ÷ sayı);            - Bölme
  ⚠️ DİKKAT: 0 ile işlem yapılamaz!

📋 LİSTE İŞLEMLERİ:
─────────────────────────────────────────────────────────────────
  List("eleman1,eleman2");      - Liste oluşturur/günceller
  List("eleman");               - Elemanı listeden siler

🎨 RENK AYARLARI:
─────────────────────────────────────────────────────────────────
  Printcolor("renk");           - Yazı rengini değiştirir
  
  Desteklenen: Beyaz, Kırmızı, Sarı, Yeşil, Turuncu, Mor

🔄 DÖNGÜ KONTROLÜ:
─────────────────────────────────────────────────────────────────
  Go();                         - Sonsuz döngü başlatır
  Stop();                       - Döngüyü/programı durdurur
  time.go(n)                    - Önceki kodu n kez tekrarlar

⚙️ FONKSİYON:
─────────────────────────────────────────────────────────────────
  func<isim>(param);            - Fonksiyon tanımlar
      f.Printitle("metin");     - Fonksiyon içi komutlar
  end.func                      - Fonksiyon bitişi
  Call.func<isim>(param);       - Fonksiyonu çalıştırır

🎯 SEÇİM YAPISI:
─────────────────────────────────────────────────────────────────
  Or();                         - Menü başlatır
  Printitle("A: Seçenek");
  Input("secim:");
  Or.choose();                  - Seçimi kaydeder
  
  Order();                      - Seçime göre çıktı
  Printitle("Metin"); (A)       - A için çıktı

🎯 PROGRAM YAPISI:
─────────────────────────────────────────────────────────────────
  main_code;                    - Kodun bitiş işaretleyicisi

╚════════════════════════════════════════════════════════════════╝
"""
        print(help_text)
        input("\n\033[93m[ENTER] tuşuna basarak ana menüye dönün...\033[0m")
    
    def error(self, code, message, line_num=None):
        """Hata mesajı gösterir"""
        if line_num:
            print(f"\033[91m❌ HATA {code}: (Satır {line_num}) {message}\033[0m")
        else:
            print(f"\033[91m❌ HATA {code}: {message}\033[0m")
        return False
    
    def parse_printitle(self, line, line_num, is_func=False):
        """Printitle komutunu işler"""
        prefix = "f." if is_func else ""
        
        # Order() içinde parantez kontrolü
        if "(" in line and ")" in line and line.count("(") == 2:
            match = re.search(rf'{prefix}Printitle\("(.+?)"\);\s*\((.+?)\)', line)
            if match:
                text = match.group(1)
                choice = match.group(2).strip()
                
                if not self.or_choose_called:
                    return self.error("A402", "Order() kullanmak için önce Or.choose() çağrılmalı", line_num)
                
                self.or_choices[choice] = text
                return True
        
        # Normal Printitle
        pattern = f'{prefix}Printitle\\("(.+?)"\\);'
        match = re.search(pattern, line)
        
        if not match:
            return self.error("A101", f"Printitle sözdizimi hatası. Doğru kullanım: {prefix}Printitle(\"metin\");", line_num)
        
        text = match.group(1)
        
        if text.startswith("$/"):
            content = text[2:]
            if not content:
                return self.error("A102", "$/metin formatında metin boş olamaz", line_num)
            self.screen_lines.append(content)
            print(f"{self.colors[self.current_color]}{content}{self.colors['reset']}")
        else:
            print(f"{self.colors[self.current_color]}{text}{self.colors['reset']}")
        
        if self.or_mode:
            self.or_options.append(text)
        
        return True
    
    def parse_input(self, line, line_num, is_func=False):
        """Input komutunu işler"""
        prefix = "f." if is_func else ""
        pattern = f'{prefix}Input\\("(.+?):?"\\);'
        match = re.search(pattern, line)
        
        if not match:
            return self.error("A110", f"Input sözdizimi hatası. Doğru kullanım: {prefix}Input(\"etiket:\");", line_num)
        
        label = match.group(1)
        user_input = input(f"{label}: ")
        self.variables[label] = user_input
        
        if self.or_mode:
            self.or_input_value = user_input
        
        return True
    
    def parse_intask(self, line, line_num, is_func=False):
        """Intask komutunu işler"""
        prefix = "f." if is_func else ""
        pattern = f'{prefix}Intask\\("(.+?)"\\);'
        match = re.search(pattern, line)
        
        if not match:
            return self.error("A202", f"Intask sözdizimi hatası", line_num)
        
        text = match.group(1)
        
        if '{' not in text or '}' not in text:
            return self.error("A120", "Intask içinde değişken kullanımı hatalı", line_num)
        
        for var_name, var_value in self.variables.items():
            text = text.replace(f"{{{var_name}}}", str(var_value))
        
        print(f"{self.colors[self.current_color]}{text}{self.colors['reset']}")
        return True
        
        
    def parse_wait(self, line, line_num, is_func=False):
        	
        	
        """wait komutunu işler"""
        prefix = "f." if is_func else ""
        pattern = f'{prefix}wait\\((\\d+)\\)'
        match = re.search(pattern, line)
        
        if not match:
            return self.error("A301", f"wait sözdizimi hatası. Doğru kullanım: {prefix}wait(saniye)", line_num)
        
        seconds = int(match.group(1))
        
        if seconds <= 0 or seconds > 100:
            return self.error("A130", "wait değeri 1-100 arasında olmalıdır", line_num)
        
        time.sleep(seconds)
        return True
    
    def parse_math(self, line, line_num, is_func=False):
        """math komutunu işler"""
        prefix = "f." if is_func else ""
        pattern = f'{prefix}math\\((\\d+)\\s*([+\\-×÷])\\s*(\\d+)\\);'
        match = re.search(pattern, line)
        
        if not match:
            return self.error("A401", f"math sözdizimi hatası", line_num)
        
        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))
        
        if num1 == 0 or num2 == 0:
            return self.error("A140", "0 ile matematik işlemi yapılamaz!", line_num)
        
        result = 0
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '×':
            result = num1 * num2
        elif operator == '÷':
            result = num1 / num2
        else:
            return self.error("A141", f"Geçersiz operatör", line_num)
        
        print(f"{self.colors[self.current_color]}Sonuç: {result}{self.colors['reset']}")
        return True
    
    def parse_clear(self, line, line_num, is_func=False):
        """Clear komutunu işler"""
        prefix = "f." if is_func else ""
        
        if f"{prefix}Clear();" in line or f"{prefix}Clear()" in line:
            self.clear_screen()
            self.screen_lines.clear()
            return True
        return self.error("A150", f"Clear sözdizimi hatası", line_num)
    
    def parse_list(self, line, line_num, is_func=False):
        """List komutunu işler"""
        prefix = "f." if is_func else ""
        pattern = f'{prefix}List\\("(.+?)"\\);'
        match = re.search(pattern, line)
        
        if not match:
            return self.error("A601", f"List sözdizimi hatası", line_num)
        
        content = match.group(1)
        
        if not content.strip():
            return self.error("A161", "Liste içeriği boş olamaz", line_num)
        
        if content.endswith(','):
            return self.error("A160", "Liste tanımında son elemandan sonra virgül olamaz", line_num)
        
        if ',' in content:
            elements = [e.strip() for e in content.split(',')]
            if any(not e for e in elements):
                return self.error("A161", "Listede boş öğe olamaz", line_num)
            self.list_data.extend(elements)
            print(f"{self.colors[self.current_color]}Liste güncellendi: {self.list_data}{self.colors['reset']}")
        else:
            if content in self.list_data:
                self.list_data.remove(content)
                print(f"{self.colors[self.current_color]}'{content}' listeden silindi{self.colors['reset']}")
            else:
                print(f"{self.colors[self.current_color]}'{content}' listede bulunamadı{self.colors['reset']}")
        
        return True
    
    def parse_printcolor(self, line, line_num, is_func=False):
        """Printcolor komutunu işler"""
        prefix = "f." if is_func else ""
        pattern = f'{prefix}Printcolor\\("(.+?)"\\);'
        match = re.search(pattern, line)
        
        if not match:
            return self.error("A701", f"Printcolor sözdizimi hatası", line_num)
        
        color = match.group(1).lower()
        
        if color not in self.colors or color == "reset":
            return self.error("A170", f"Desteklenmeyen renk: {color}", line_num)
        
        self.current_color = color
        print(f"{self.colors[color]}Renk değiştirildi: {color}{self.colors['reset']}")
        return True
    
    def parse_or(self, line, line_num):
        """Or() komutunu işler"""
        if "Or();" in line or "Or()" in line:
            self.or_mode = True
            self.or_options = []
            self.or_input_value = None
            self.or_choose_called = False
            self.or_choices = {}
            return True
        return False
    
    def parse_or_choose(self, line, line_num):
        """Or.choose(); komutunu işler"""
        if "Or.choose();" in line or "Or.choose()" in line:
            if not self.or_mode:
                return self.error("A401", "Or.choose() çağrıldı ama Or() başlatılmamış", line_num)
            
            if self.or_input_value is None:
                return self.error("A400", "Or() kullanıldı ama Input alınmadı", line_num)
            
            print(f"{self.colors[self.current_color]}Seçim kaydedildi: {self.or_input_value}{self.colors['reset']}")
            
            self.or_choose_called = True
            self.or_mode = False
            return True
        return False
    
    def parse_order(self, line, line_num, prev_line_empty):
        """Order(); komutunu işler"""
        if "Order();" in line or "Order()" in line:
            if not self.or_choose_called:
                return self.error("A403", "Order() kullanmak için önce Or(), Input(), Or.choose() kullanılmalı", line_num)
            
            if not prev_line_empty:
                return self.error("A404", "Or.choose() ile Order() arasında 1 boş satır olmalı", line_num)
            
            return True
        return False
    
    def execute_order(self):
        """Order() sonrası seçime göre çıktı verir"""
        if self.or_input_value in self.or_choices:
            selected_text = self.or_choices[self.or_input_value]
            print(f"{self.colors[self.current_color]}{selected_text}{self.colors['reset']}")
        else:
            available = ", ".join(self.or_choices.keys())
            print(f"\033[91m❌ HATA A405: Seçenek '{self.or_input_value}' tanımlı değil. Mevcut: {available}\033[0m")
    
    def parse_time_go(self, line, line_num):
        """time.go(n) komutunu işler"""
        match = re.search(r'time\.go\((\d+)\)', line)
        if not match:
            return False
        
        repeat_count = int(match.group(1))
        
        if repeat_count <= 0 or repeat_count > 100:
            return self.error("A510", "time.go değeri 1-100 arasında olmalıdır", line_num)
        
        if self.loop_active:
            return self.error("A500", "time.go() ve Go() aynı anda kullanılamaz", line_num)
        
        self.time_go_repeat = repeat_count
        return True
    
    def parse_function_definition(self, lines, start_idx):
        """Fonksiyon tanımını parse eder"""
        line = lines[start_idx].strip()
        
        match = re.search(r'func<(.+?)>\((.*?)\);', line)
        if not match:
            return self.error("F001", "Fonksiyon sözdizimi hatası", start_idx + 1), start_idx
        
        func_name = match.group(1)
        params_str = match.group(2).strip()
        params = [p.strip() for p in params_str.split(',')] if params_str else []
        
        if func_name in self.functions:
            return self.error("A301", f"'{func_name}' fonksiyonu zaten tanımlanmış", start_idx + 1), start_idx
        
        func_body = []
        i = start_idx + 1
        found_end = False
        
        while i < len(lines):
            current_line = lines[i].strip()
            
            if current_line == "end.func":
                found_end = True
                break
            
            if current_line and not current_line.startswith('//'):
                if not current_line.startswith('f.') and current_line not in ['end.func']:
                    return self.error("A302", f"Fonksiyon içinde komutlar f. ile başlamalı", i + 1), i
                func_body.append(current_line)
            
            i += 1
        
        if not found_end:
            return self.error("F003", f"Fonksiyon '{func_name}' end.func ile kapatılmamış", start_idx + 1), start_idx
        
        self.functions[func_name] = {
            'params': params,
            'body': func_body
        }
        
        return True, i
    
    def parse_function_call(self, line, line_num):
        """Fonksiyon çağrısını işler"""
        match = re.search(r'Call\.func<(.+?)>\((.*?)\);', line)
        if not match:
            return self.error("F101", "Fonksiyon çağırma sözdizimi hatası", line_num)
        
        func_name = match.group(1)
        args_str = match.group(2).strip()
        
        if func_name not in self.functions:
            return self.error("F102", f"'{func_name}' fonksiyonu tanımlanmamış", line_num)
        
        func_def = self.functions[func_name]
        
        args = []
        if args_str:
            for arg in re.findall(r'"([^"]*)"', args_str):
                args.append(arg)
        
        if len(args) != len(func_def['params']):
            return self.error("A303", f"Fonksiyon '{func_name}' {len(func_def['params'])} parametre bekliyor", line_num)
        
        old_vars = self.variables.copy()
        for i, param in enumerate(func_def['params']):
            self.variables[param] = args[i]
        
        for i, func_line in enumerate(func_def['body'], 1):
            if not self.parse_line(func_line, line_num, is_func=True):
                self.variables = old_vars
                return False
        
        self.variables = old_vars
        
        return True
    
    def parse_line(self, line, line_num, is_func=False, prev_line_empty=False):
        """Tek bir satırı işler"""
        line = line.strip()
        
        if not line or line.startswith('//'):
            return True
        
        if line == "main_code;":
            return True
        
        if self.parse_or(line, line_num):
            return True
        
        if self.parse_or_choose(line, line_num):
            return True
        
        if self.parse_order(line, line_num, prev_line_empty):
            return True
        
        if self.parse_time_go(line, line_num):
            return True
        
        prefix = "f." if is_func else ""
        if f"{prefix}Go();" in line or f"{prefix}Go()" in line:
            if self.time_go_repeat > 0:
                return self.error("A500", "Go() ve time.go() aynı anda kullanılamaz", line_num)
            self.loop_active = True
            return True
        
        if f"{prefix}Stop();" in line or f"{prefix}Stop()" in line:
            self.program_running = False
            return True
        
        if f"{prefix}Printitle(" in line:
            return self.parse_printitle(line, line_num, is_func)
        elif f"{prefix}Input(" in line:
            return self.parse_input(line, line_num, is_func)
        elif f"{prefix}Intask(" in line:
            return self.parse_intask(line, line_num, is_func)
        elif f"{prefix}wait(" in line:
            return self.parse_wait(line, line_num, is_func)
        elif f"{prefix}math(" in line:
            return self.parse_math(line, line_num, is_func)
        elif f"{prefix}Clear(" in line:
            return self.parse_clear(line, line_num, is_func)
        elif f"{prefix}List(" in line:
            return self.parse_list(line, line_num, is_func)
        elif f"{prefix}Printcolor(" in line:
            return self.parse_printcolor(line, line_num, is_func)
        elif "Call.func<" in line and not is_func:
            return self.parse_function_call(line, line_num)
        else:
            return self.error("A001", f"Bilinmeyen komut veya sözdizimi hatası", line_num)
    
    def execute(self, code):
        """Kodu çalıştırır"""
        lines = code.strip().split('\n')
        
        if not lines or lines[-1].strip() != "main_code;":
            return self.error("A900", "Kod 'main_code;' ile bitmelidir")
        
        if len(lines) > 1:
            for i in range(len(lines)-1, -1, -1):
                if lines[i].strip() == "main_code;":
                    if i < len(lines) - 1:
                        return self.error("A181", f"(Satır {i+2}) main_code; sonrasında kod yazılamaz", i+2)
                    break
        
        lines = lines[:-1]
        
        i = 0
        executable_lines = []
        
        while i < len(lines):
            line = lines[i].strip()
            
            if line.startswith('func<'):
                result, end_idx = self.parse_function_definition(lines, i)
                if not result:
                    return False
                i = end_idx + 1
            else:
                executable_lines.append((line, i + 1))
                i += 1
        
        max_iterations = 1
        if self.time_go_repeat > 0:
            max_iterations = self.time_go_repeat
        
        iteration = 0
        order_mode = False
        order_started_line = -1
        prev_line_empty = False
        
        while self.program_running and iteration < max_iterations:
            for idx, (line, line_num) in enumerate(executable_lines):
                if not self.program_running:
                    break
                
                if idx > 0:
                    prev_line = executable_lines[idx - 1][0]
                    prev_line_empty = (not prev_line or prev_line.startswith('//'))
                else:
                    prev_line_empty = False
                
                if "Order();" in line or "Order()" in line:
                    if not self.parse_line(line, line_num, is_func=False, prev_line_empty=prev_line_empty):
                        return False
                    order_mode = True
                    order_started_line = idx
                    continue
                
                if order_mode:
                    if "Printitle(" in line and "(" in line and ")" in line:
                        if line.count("(") >= 2:
                            if not self.parse_line(line, line_num, is_func=False, prev_line_empty=prev_line_empty):
                                return False
                            continue
                        else:
                            if not self.or_choices:
                                return self.error("A405", "Order() kullanıldı ama hiç seçenek tanımlanmadı", line_num)
                            
                            if self.or_input_value not in self.or_choices:
                                available = ", ".join(self.or_choices.keys())
                                return self.error("A405", f"Seçenek '{self.or_input_value}' tanımlı değil. Mevcut: {available}", order_started_line + 1)
                            
                            self.execute_order()
                            order_mode = False
                            
                            if not self.parse_line(line, line_num, is_func=False, prev_line_empty=prev_line_empty):
                                return False
                    else:
                        if not self.or_choices:
                            return self.error("A405", "Order() kullanıldı ama hiç seçenek tanımlanmadı", line_num)
                        
                        if self.or_input_value not in self.or_choices:
                            available = ", ".join(self.or_choices.keys())
                            return self.error("A405", f"Seçenek '{self.or_input_value}' tanımlı değil. Mevcut: {available}", order_started_line + 1)
                        
                        self.execute_order()
                        order_mode = False
                        
                        if not self.parse_line(line, line_num, is_func=False, prev_line_empty=prev_line_empty):
                            return False
                else:
                    if not self.parse_line(line, line_num, is_func=False, prev_line_empty=prev_line_empty):
                        return False
            
            if order_mode:
                if not self.or_choices:
                    return self.error("A405", "Order() kullanıldı ama hiç seçenek tanımlanmadı", order_started_line + 1)
                
                if self.or_input_value not in self.or_choices:
                    available = ", ".join(self.or_choices.keys())
                    return self.error("A405", f"Seçenek '{self.or_input_value}' tanımlı değil. Mevcut: {available}", order_started_line + 1)
                
                self.execute_order()
                order_mode = False
            
            iteration += 1
            
            if self.loop_active:
                max_iterations = float('inf')
            else:
                if iteration >= max_iterations:
                    break
        
        return True


def main():
    """Ana program"""
    interpreter = AetherisScriptInterpreter()
    
    while True:
        interpreter.show_main_menu()
        choice = input("\n\033[96mSeçiminiz: \033[0m").strip().upper()
        
        if choice == 'Q':
            interpreter.show_tutorial_link()
        elif choice == 'S':
            interpreter.show_examples_menu()
        elif choice == 'HELP':
            interpreter.show_help()
        elif choice == 'SET':
            interpreter.show_settings_menu()
        elif choice == 'EXIT':
            interpreter.clear_screen()
            print("\033[96m")
            print("╔════════════════════════════════════════════════════════════════╗")
            print("║              Aetheris Script'i kullandığınız için             ║")
            print("║                      teşekkür ederiz! 👋                      ║")
            print("╚════════════════════════════════════════════════════════════════╝")
            print("\033[0m")
            print("Aetheris Script Kapatılıyor...")
            print("\033[0m")
            time.sleep(3)
            sys.exit(0)
        else:
            # Kod yazma moduna geç
            interpreter.clear_screen()
            print("\033[93m")
            print("╔════════════════════════════════════════════════════════════════╗")
            print("║                    KOD YAZMA MODU                             ║")
            print("║                  Yardım için [H] yazın                        ║")
            print("╚════════════════════════════════════════════════════════════════╝")
            print("\033[0m")
            print("\033[92mKodunuzu yazın (bitirmek için 'main_code;' yazın):\033[0m\n")
            
            code_lines = []
            line_number = 1
            
            while True:
                try:
                    line = input(f"\033[90m{line_number:3d} |\033[0m ")
                    
                    # Help kontrolü
                    if line.strip().upper() == 'H' and len(code_lines) == 0:
                        interpreter.show_code_mode_help()
                        interpreter.clear_screen()
                        print("\033[93m")
                        print("╔════════════════════════════════════════════════════════════════╗")
                        print("║                    KOD YAZMA MODU                             ║")
                        print("║                  Yardım için [H] yazın                        ║")
                        print("╚════════════════════════════════════════════════════════════════╝")
                        print("\033[0m")
                        print("\033[92mKodunuzu yazın (bitirmek için 'main_code;' yazın):\033[0m\n")
                        continue
                    
                    code_lines.append(line)
                    line_number += 1
                    
                    if line.strip() == "main_code;":
                        code = '\n'.join(code_lines)
                        print("\n\033[92m" + "="*64)
                        print("                      PROGRAM ÇIKTISI")
                        print("="*64 + "\033[0m\n")
                        
                        new_interpreter = AetherisScriptInterpreter()
                        new_interpreter.current_color = interpreter.theme_color
                        new_interpreter.execute(code)
                        
                        print("\n\033[92m" + "="*63)
                        print("                    PROGRAM SONA ERDİ")
                        print("="*63 + "\033[0m")
                        
                        input("\n\033[93m[ENTER] tuşuna basarak ana menüye dönün...\033[0m")
                        break
                        
                except KeyboardInterrupt:
                    print("\n\033[91m\n❌ Program kullanıcı tarafından iptal edildi\033[0m")
                    input("\n\033[93m[ENTER] tuşuna basarak ana menüye dönün...\033[0m")
                    break
                except EOFError:
                    print("\n\033[91m\n❌ Girdi hatası\033[0m")
                    input("\n\033[93m[ENTER] tuşuna basarak ana menüye dönün...\033[0m")
                    break


if __name__ == "__main__":
    main()
