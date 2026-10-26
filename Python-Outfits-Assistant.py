import tkinter as tk
from tkinter import messagebox
import random


# 1. GARDIROP VERİ YAPISI (Üst, Alt, Elbise, Ayakkabı ve Çantalar)

gardrop = [
    # --- ÜST GİYİM (ust) ---
    {"id": 1, "isim": "Beyaz Oversize Tişört", "kategori": "ust", "renk": "beyaz", "hava": ["sicak", "ilik"], "ortam": ["gunluk", "rahat"], "mevcut": True},
    {"id": 2, "isim": "Siyah Askılı Crop", "kategori": "ust", "renk": "siyah", "hava": ["sicak"], "ortam": ["gunluk", "rahat"], "mevcut": True},
    {"id": 3, "isim": "Pembe Kısa Kollu Crop", "kategori": "ust", "renk": "pembe", "hava": ["sicak", "ilik"], "ortam": ["gunluk"], "mevcut": True},
    {"id": 4, "isim": "Beyaz Fitilli Atlet", "kategori": "ust", "renk": "beyaz", "hava": ["sicak", "ilik"], "ortam": ["gunluk", "rahat"], "mevcut": True},
    {"id": 5, "isim": "Yeşil İnce Triko Kazak", "kategori": "ust", "renk": "yesil", "hava": ["soguk", "ilik"], "ortam": ["gunluk", "resmi"], "mevcut": True},
    {"id": 6, "isim": "Siyah Boğazlı Kazak", "kategori": "ust", "renk": "siyah", "hava": ["soguk"], "ortam": ["gunluk", "resmi"], "mevcut": True},
    {"id": 7, "isim": "Mavi Klasik Gömlek", "kategori": "ust", "renk": "mavi", "hava": ["ilik", "sicak"], "ortam": ["resmi", "gunluk"], "mevcut": True},
    {"id": 8, "isim": "Ekru Şifon Bluz", "kategori": "ust", "renk": "bej", "hava": ["ilik", "sicak"], "ortam": ["resmi", "gunluk"], "mevcut": True},
    {"id": 9, "isim": "Gri Kapüşonlu Sweatshirt", "kategori": "ust", "renk": "gri", "hava": ["soguk", "ilik"], "ortam": ["gunluk", "rahat"], "mevcut": True},
    {"id": 10, "isim": "Kırmızı Oversize Sweatshirt", "kategori": "ust", "renk": "kirmizi", "hava": ["soguk", "ilik"], "ortam": ["gunluk", "rahat"], "mevcut": True},

    # --- ALT GİYİM (alt) ---
    {"id": 11, "isim": "Siyah Yüksek Bel Tayt", "kategori": "alt", "renk": "siyah", "hava": ["soguk", "ilik", "sicak"], "ortam": ["rahat", "gunluk"], "mevcut": True},
    {"id": 12, "isim": "Gri Spor Tayt", "kategori": "alt", "renk": "gri", "hava": ["ilik", "sicak"], "ortam": ["rahat"], "mevcut": True},
    {"id": 13, "isim": "Siyah Pileli Mini Etek", "kategori": "alt", "renk": "siyah", "hava": ["ilik", "sicak"], "ortam": ["gunluk", "resmi"], "mevcut": True},
    {"id": 14, "isim": "Bej Kalem Etek", "kategori": "alt", "renk": "bej", "hava": ["ilik", "sicak"], "ortam": ["resmi"], "mevcut": True},
    {"id": 15, "isim": "Kot Şort", "kategori": "alt", "renk": "lacivert", "hava": ["sicak"], "ortam": ["gunluk", "rahat"], "mevcut": True},
    {"id": 16, "isim": "Mavi Mom Jean (Kot Pantolon)", "kategori": "alt", "renk": "lacivert", "hava": ["soguk", "ilik", "sicak"], "ortam": ["gunluk"], "mevcut": True},
    {"id": 17, "isim": "Siyah Kumaş Pantolon", "kategori": "alt", "renk": "siyah", "hava": ["soguk", "ilik"], "ortam": ["resmi", "gunluk"], "mevcut": True},
    {"id": 18, "isim": "Gri Eşofman Altı", "kategori": "alt", "renk": "gri", "hava": ["soguk", "ilik"], "ortam": ["rahat"], "mevcut": True},
    {"id": 19, "isim": "Haki Kargo Pantolon", "kategori": "alt", "renk": "yesil", "hava": ["ilik", "soguk"], "ortam": ["gunluk"], "mevcut": True},

    # --- TEK PARÇA / ELBİSE (tek_parca) ---
    {"id": 20, "isim": "Lila Çiçekli Yazlık Elbise", "kategori": "tek_parca", "renk": "lila", "hava": ["sicak"], "ortam": ["gunluk"], "mevcut": True},
    {"id": 21, "isim": "Siyah Triko Kışlık Elbise", "kategori": "tek_parca", "renk": "siyah", "hava": ["soguk", "ilik"], "ortam": ["gunluk", "resmi"], "mevcut": True},
    {"id": 22, "isim": "Kırmızı Kruvaze Şık Elbise", "kategori": "tek_parca", "renk": "kirmizi", "hava": ["ilik", "sicak"], "ortam": ["resmi"], "mevcut": True},
    {"id": 23, "isim": "Siyah Rahat Penye Elbise", "kategori": "tek_parca", "renk": "siyah", "hava": ["sicak", "ilik"], "ortam": ["rahat", "gunluk"], "mevcut": True},

    # --- AYAKKABI (ayakkabi) ---
    {"id": 24, "isim": "Siyah Deri Bot", "kategori": "ayakkabi", "renk": "siyah", "hava": ["soguk"], "ortam": ["gunluk", "resmi"], "mevcut": True},
    {"id": 25, "isim": "Beyaz Sneaker (Spor Ayakkabı)", "kategori": "ayakkabi", "renk": "beyaz", "hava": ["ilik", "sicak"], "ortam": ["gunluk", "rahat"], "mevcut": True},
    {"id": 26, "isim": "Bej Deri Sandalet", "kategori": "ayakkabi", "renk": "bej", "hava": ["sicak"], "ortam": ["gunluk", "rahat"], "mevcut": True},
    {"id": 27, "isim": "Siyah Klasik Stiletto", "kategori": "ayakkabi", "renk": "siyah", "hava": ["ilik", "sicak"], "ortam": ["resmi"], "mevcut": True},

    # --- AKSESUAR / ÇANTA (aksesuar) ---
    {"id": 28, "isim": "Siyah Deri Sırt Çantası", "kategori": "aksesuar", "renk": "siyah", "hava": ["soguk", "ilik", "sicak"], "ortam": ["gunluk", "rahat"], "mevcut": True},
    {"id": 29, "isim": "Kahverengi Büyük Kol Çantası", "kategori": "aksesuar", "renk": "bej", "hava": ["soguk", "ilik"], "ortam": ["gunluk", "resmi"], "mevcut": True},
    {"id": 30, "isim": "Minimal Şık El Çantası", "kategori": "aksesuar", "renk": "siyah", "hava": ["ilik", "sicak"], "ortam": ["resmi"], "mevcut": True}
]

# Hafıza listeleri
aktif_kombin = []
begenilmeyen_kombinler = []



# 2. ALGORİTMA VE FİLTRELEME FONKSİYONLARI

def renk_uyumlu_mu(renk1, renk2):
    notr_renkler = ["siyah", "beyaz", "gri", "bej", "lacivert"]
    if (renk1 in notr_renkler) or (renk2 in notr_renkler) or (renk1 == renk2):
        return True
    return False


def kombin_havuzu_olustur(hava, ortam):
    ustler = [k for k in gardrop if k["mevcut"] and k["kategori"] == "ust" and hava in k["hava"] and ortam in k["ortam"]]
    altlar = [k for k in gardrop if k["mevcut"] and k["kategori"] == "alt" and hava in k["hava"] and ortam in k["ortam"]]
    elbiseler = [k for k in gardrop if k["mevcut"] and k["kategori"] == "tek_parca" and hava in k["hava"] and ortam in k["ortam"]]
    ayakkabilar = [k for k in gardrop if k["mevcut"] and k["kategori"] == "ayakkabi" and hava in k["hava"] and ortam in k["ortam"]]
    aksesuarlar = [k for k in gardrop if k["mevcut"] and k["kategori"] == "aksesuar" and ortam in k["ortam"]]

    olasi_kombinler = []

    # Üst + Alt + Ayakkabı + Çanta kombinasyonları
    for ust in ustler:
        for alt in altlar:
            if renk_uyumlu_mu(ust["renk"], alt["renk"]):
                for ayakkabi in ayakkabilar:
                    for aksesuar in aksesuarlar:
                        olasi_kombinler.append([ust, alt, ayakkabi, aksesuar])

    # Elbise + Ayakkabı + Çanta kombinasyonları
    for elbise in elbiseler:
        for ayakkabi in ayakkabilar:
            for aksesuar in aksesuarlar:
                olasi_kombinler.append([elbise, ayakkabi, aksesuar])

    return olasi_kombinler



# 3. ARAYÜZ BUTON FONKSİYONLARI

def yeni_kombin_oner():
    global aktif_kombin
    
    # Kullanıcının girdiği sıcaklık derecesini okuma ve aralığa çevirme
    try:
        girilen_derece = float(derece_giris_kutusu.get())
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sıcaklık değeri girin (Örn: 15)")
        return

    if girilen_derece < 10:
        secilen_hava = "soguk"
    elif 10 <= girilen_derece <= 22:
        secilen_hava = "ilik"
    else:
        secilen_hava = "sicak"

    secilen_ortam = ortam_degiskeni.get()

    tum_kombinler = kombin_havuzu_olustur(secilen_hava, secilen_ortam)
    gecerli_kombinler = [k for k in tum_kombinler if k not in begenilmeyen_kombinler]

    if len(gecerli_kombinler) == 0:
        sonuc_etiketi.config(text="Seçtiğin kriterlere ve dolabındaki\nmevcut kıyafetlere uygun kombin kalmadı!", fg="#D90429")
        aktif_kombin = []
        return

    aktif_kombin = random.choice(gecerli_kombinler)

    if len(aktif_kombin) == 4:
        metin = (
            f"ÜST      : {aktif_kombin[0]['isim']} ({aktif_kombin[0]['renk'].capitalize()})\n"
            f"ALT      : {aktif_kombin[1]['isim']} ({aktif_kombin[1]['renk'].capitalize()})\n"
            f"AYAKKABI : {aktif_kombin[2]['isim']} ({aktif_kombin[2]['renk'].capitalize()})\n"
            f"ÇANTA    : {aktif_kombin[3]['isim']} ({aktif_kombin[3]['renk'].capitalize()})"
        )
    else:
        metin = (
            f"ELBİSE   : {aktif_kombin[0]['isim']} ({aktif_kombin[0]['renk'].capitalize()})\n"
            f"AYAKKABI : {aktif_kombin[1]['isim']} ({aktif_kombin[1]['renk'].capitalize()})\n"
            f"ÇANTA    : {aktif_kombin[2]['isim']} ({aktif_kombin[2]['renk'].capitalize()})"
        )

    sonuc_etiketi.config(text=metin, fg="#2B2D42")


def kombini_begendim():
    if not aktif_kombin:
        messagebox.showwarning("Uyarı", "Önce bir kombin önermelisin!")
        return
    messagebox.showinfo("Harika!", "Kombin onaylandı! Günün güzel geçsin.")


def kombini_begenmedim():
    if not aktif_kombin:
        messagebox.showwarning("Uyarı", "Önce bir kombin önermelisin!")
        return
    begenilmeyen_kombinler.append(aktif_kombin)
    yeni_kombin_oner()



# 4. GÖRSEL ARAYÜZ (TKINTER) TASARIMI

pencere = tk.Tk()
pencere.title("Akıllı Kombin Asistanı")
pencere.geometry("520x620")
pencere.configure(bg="#F8F9FA")

# Başlık
tk.Label(pencere, text="GÜNLÜK KOMBİN ASİSTANI", font=("Helvetica", 15, "bold"), bg="#F8F9FA", fg="#2B2D42").pack(pady=15)

# Hava Durumu Derece Giriş Alanı
hava_cerceve = tk.LabelFrame(pencere, text=" 1. Bugün Hava Kaç Derece? ", font=("Helvetica", 10, "bold"), bg="#F8F9FA", fg="#2B2D42", padx=10, pady=8)
hava_cerceve.pack(fill="x", padx=25, pady=5)

derece_giris_kutusu = tk.Entry(hava_cerceve, font=("Helvetica", 11), justify="center", width=10)
derece_giris_kutusu.pack(side="left", padx=10)
derece_giris_kutusu.insert(0, "20")

tk.Label(hava_cerceve, text="°C  (Örn: 8, 15, 26)", font=("Helvetica", 9), bg="#F8F9FA", fg="#6C757D").pack(side="left", padx=5)

# Ortam / Etkinlik Seçim Alanı
ortam_cerceve = tk.LabelFrame(pencere, text=" 2. Nereye Gidiyorsun? ", font=("Helvetica", 10, "bold"), bg="#F8F9FA", fg="#2B2D42", padx=10, pady=8)
ortam_cerceve.pack(fill="x", padx=25, pady=5)

ortam_degiskeni = tk.StringVar(value="gunluk")
tk.Radiobutton(ortam_cerceve, text="Okul / Günlük", variable=ortam_degiskeni, value="gunluk", bg="#F8F9FA").pack(side="left", expand=True)
tk.Radiobutton(ortam_cerceve, text="Resmi / Şık", variable=ortam_degiskeni, value="resmi", bg="#F8F9FA").pack(side="left", expand=True)
tk.Radiobutton(ortam_cerceve, text="Ev / Rahat", variable=ortam_degiskeni, value="rahat", bg="#F8F9FA").pack(side="left", expand=True)

# Kombin Öner Butonu
tk.Button(pencere, text="KOMBİN ÖNER", command=yeni_kombin_oner, font=("Helvetica", 11, "bold"), bg="#457B9D", fg="white", pady=8, cursor="hand2").pack(fill="x", padx=25, pady=12)

# Sonuç Gösterme Kutusu (Kart)
sonuc_cerceve = tk.Frame(pencere, bg="white", bd=2, relief="groove")
sonuc_cerceve.pack(fill="both", expand=True, padx=25, pady=5)

sonuc_etiketi = tk.Label(sonuc_cerceve, text="Sıcaklığı girip\n'KOMBİN ÖNER' butonuna tıkla!", font=("Helvetica", 11, "bold"), bg="white", fg="#6C757D", justify="left")
sonuc_etiketi.pack(expand=True, padx=15, pady=15)

# Karar Butonları (Beğendim / Beğenmedim)
karar_cerceve = tk.Frame(pencere, bg="#F8F9FA")
karar_cerceve.pack(fill="x", padx=25, pady=12)

tk.Button(karar_cerceve, text="Beğendim", command=kombini_begendim, bg="#2A9D8F", fg="white", font=("Helvetica", 10, "bold"), width=20, pady=6).pack(side="left", expand=True, padx=3)
tk.Button(karar_cerceve, text="Beğenmedim (Değiştir)", command=kombini_begenmedim, bg="#E76F51", fg="white", font=("Helvetica", 10, "bold"), width=20, pady=6).pack(side="right", expand=True, padx=3)


# 5. PROGRAMI ÇALIŞTIRAN ANA DÖNGÜ

pencere.mainloop()