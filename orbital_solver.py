import math

#SABİTLER
GM = 3.986004418e14  #Dünya'nın yerçekimi parametresi (m^3/s^2)


def saat_donustur(zaman_str):
    """'12:00' formatındaki stringi matematiksel saate dönüştürür."""
    try:
        saat, dakika = map(int, zaman_str.split(":"))
        return saat + (dakika / 60)
    except:
        return None


print("--- Uydu Yörünge Analiz Aracı ---")

try:
    #GİRDİLER
    e = float(input("Eksantriklik (e) (Örn: 0.008): "))
    T_hours = float(input("Periyot (T) saat cinsinden (Örn: 10): "))

    #Perigee Zamanı Girişi
    t0_input = input("Uydunun perigee'yi geçtiği zaman (t0) (Örn: 12:00): ")

    #Kaç dakika sonraki konumu?
    gecen_dakika = float(input(f"{t0_input} zamanından kaç dakika sonraki konumu istiyorsunuz? (Örn: 30): "))

    #HESAPLAMALAR
    #Zaman farkını saniyeye çeviriyoruz
    delta_t_sec = gecen_dakika * 60

    #Periyot saniye
    T_sec = T_hours * 3600

    #Mean Motion (n)
    n = (2 * math.pi) / T_sec

    #Mean Anomaly (M)
    M = n * delta_t_sec

    #Eccentric Anomaly (E) - İterasyon
    E = M
    for _ in range(15):
        E = M + e * math.sin(E)

    #Semi-major Axis (a)
    a = math.pow((GM * (T_sec ** 2)) / (4 * (math.pi ** 2)), 1 / 3)

    #Koordinatlar
    x = a * (math.cos(E) - e)
    y = a * math.sqrt(1 - e ** 2) * math.sin(E)
    r = a * (1 - e * math.cos(E))

    #Hedef Saat Hesaplama
    t0_saat_ondalik = saat_donustur(t0_input)
    hedef_saat_ondalik = t0_saat_ondalik + (gecen_dakika / 60)
    saat_sonuc = int(hedef_saat_ondalik)
    dakika_sonuc = int((hedef_saat_ondalik - saat_sonuc) * 60)

    #SONUÇLAR
    print("\n" + "=" * 45)
    print(f" ANALİZ SONUCU ({t0_input} + {gecen_dakika} dk -> {saat_sonuc:02d}:{dakika_sonuc:02d})")
    print("-" * 45)
    print(f"Yarı Büyük Eksen (a):    {a / 1000:.2f} km")
    print(f"Eksantrik Anomali (E):  {math.degrees(E):.4f} derece")
    print("-" * 45)
    print(f"X_pe Koordinatı:        {x / 1000:.2f} km")
    print(f"Y_pe Koordinatı:        {y / 1000:.2f} km")
    print(f"Vektörel Yarıçap (r):   {r / 1000:.2f} km")
    print("=" * 45)

except ValueError:
    print("Hata: Lütfen sayıları ve zaman formatını (12:00) doğru giriniz.")