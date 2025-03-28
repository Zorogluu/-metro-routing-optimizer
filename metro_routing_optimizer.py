from collections import defaultdict, deque  # defaultdict ve deque sınıflarını collections modülünden içe aktarır
import heapq  # heapq modülünü içe aktarır, öncelik kuyruğu işlemleri için kullanılır
from typing import Dict, List, Set, Tuple, Optional  # Tip ipuçları için gerekli veri tiplerini typing modülünden içe aktarır

class Istasyon:  # Istasyon sınıfını tanımlar; metro istasyonlarını temsil eder
    def __init__(self, idx: str, ad: str, hat: str):  # Yapıcı metod; idx, ad, hat parametrelerini alarak Istasyon örneği oluşturur
        self.idx = idx  # İstasyonun benzersiz ID'sini (str) saklar
        self.ad = ad  # İstasyonun adını (str) saklar
        self.hat = hat  # İstasyonun ait olduğu hattı (str) saklar
        self.komsular: List[Tuple['Istasyon', int]] = []  # Komşuları ve geçiş sürelerini saklamak için boş bir liste oluşturur

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):  # komsu_ekle metodu; verilen istasyonu ve geçiş süresini ekler
        self.komsular.append((istasyon, sure))  # Komşular listesine (istasyon, sure) tuple'ını ekler

class MetroAgi:  # MetroAgi sınıfını tanımlar; metro ağını yönetir
    def __init__(self):  # Yapıcı metod; MetroAgi örneği oluşturulurken çağrılır
        self.istasyonlar: Dict[str, Istasyon] = {}  # İstasyonları ID'ye göre saklamak için boş bir sözlük oluşturur (anahtar: str, değer: Istasyon)
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)  # Hatları saklamak için defaultdict(list) kullanır (anahtar: hat adı, değer: Istasyon listesi)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:  # istasyon_ekle metodu; yeni bir istasyon eklemek için parametreleri alır
        if idx not in self.istasyonlar:  # Eğer idx anahtarı daha önce eklenmemişse
            istasyon = Istasyon(idx, ad, hat)  # Yeni bir Istasyon nesnesi oluşturur
            self.istasyonlar[idx] = istasyon  # Oluşturulan istasyonu istasyonlar sözlüğüne ekler
            self.hatlar[hat].append(istasyon)  # İlgili hatın listesine istasyonu ekler

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:  # baglanti_ekle metodu; iki istasyon arasında çift yönlü bağlantı kurar
        istasyon1 = self.istasyonlar[istasyon1_id]  # istasyon1_id kullanarak ilk istasyon nesnesini alır
        istasyon2 = self.istasyonlar[istasyon2_id]  # istasyon2_id kullanarak ikinci istasyon nesnesini alır
        istasyon1.komsu_ekle(istasyon2, sure)  # İlk istasyona, ikinci istasyonu ve geçiş süresini ekler
        istasyon2.komsu_ekle(istasyon1, sure)  # İkinci istasyona, ilk istasyonu ve geçiş süresini ekler


    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:  # en_az_aktarma_bul fonksiyonu; baslangic_id ve hedef_id parametreleri alarak, en az aktarmalı rota (Istasyon listesi) veya None değeri döndürür

      if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:  # Başlangıç veya hedef istasyon metro ağında yoksa
        return None  # None değerini döndür

      baslangic = self.istasyonlar[baslangic_id]  # baslangic_id ile metro ağından başlangıç istasyonunu al
      hedef = self.istasyonlar[hedef_id]  # hedef_id ile metro ağından hedef istasyonunu al

      kuyruk = deque([(baslangic, [baslangic])])  # deque oluştur; başlangıç istasyonu ve rota listesini ekle
      ziyaret_edildi = {baslangic}  # ziyaret_edilen isminde başlangıç istasyonunu içeren set oluştur

      while kuyruk:  # kuyruk boşalana kadar döngüye gir
          mevcut, rota = kuyruk.popleft()  # kuyruktan sol taraftan mevcut istasyon ve rota listesini al
          if mevcut == hedef:  # eğer mevcut istasyon hedef istasyon ise
              return rota  # bulunan rotayı döndür

          for komsu, _ in mevcut.komsular:  # mevcut istasyonun komşularını teker teker incele
              if komsu not in ziyaret_edildi:  # eğer komsu daha önce ziyaret edilmediyse
                  ziyaret_edildi.add(komsu)  # komsuyu ziyaret_edilen setine ekle
                  kuyruk.append((komsu, rota + [komsu]))  # kuyruk değişkenine komsu ve güncellenmiş rota listesini ekle
      return None  # hedefe ulaşılamadıysa None değerini döndür
      """BFS algoritması kullanarak en az aktarmalı rotayı bulur

        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın

        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
      """


    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:  # en_hizli_rota_bul fonksiyonu; baslangic_id ve hedef_id parametreleri alarak, en hızlı rotayı (Istasyon listesi ve toplam süre) veya None döndürür
      if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:  # Eğer baslangic_id veya hedef_id metro ağında bulunmuyorsa
          return None  # None değerini döndür

      baslangic = self.istasyonlar[baslangic_id]  # baslangic_id kullanılarak metro ağından başlangıç istasyonunu al
      hedef = self.istasyonlar[hedef_id]  # hedef_id kullanılarak metro ağından hedef istasyonunu al
      pq = [(0, id(baslangic), baslangic, [baslangic])]  # Öncelik kuyruğu oluştur; başlangıç için (toplam süre=0, tie-breaker, istasyon, rota) tuple'ı ekle
      en_dusuk_sure = {baslangic: 0}  # Her istasyon için en düşük süre bilgisini saklamak üzere, başlangıç istasyonuna 0 atayarak bir sözlük oluştur

      while pq:  # pq (öncelik kuyruğu) boşalana kadar döngüye gir
          toplam_sure, _, mevcut, rota = heapq.heappop(pq)  # Öncelik kuyruğundan en düşük toplam süreye sahip öğeyi çıkar; mevcut istasyon ve rota listesini al

          if mevcut == hedef:  # Eğer mevcut istasyon, hedef istasyona eşitse
              return rota, toplam_sure  # Bulunan rotayı ve toplam süreyi döndür

          for komsu, sure in mevcut.komsular:  # Mevcut istasyonun komşuları üzerinde döngü başlat; her komsu ve aradaki süreyi al
              yeni_sure = toplam_sure + sure  # Komşuya ulaşmak için yeni toplam süreyi hesapla

              if komsu not in en_dusuk_sure or yeni_sure < en_dusuk_sure[komsu]:  # Eğer komsu daha önce ziyaret edilmemişse ya da yeni süre mevcut o noktaya ulaşan süreden daha düşükse
                  en_dusuk_sure[komsu] = yeni_sure  # Komsunun en düşük süresini güncelle
                  tahmini_sure = 0  # Heuristic fonksiyonu için tahmini süre; burada sıfır kabul edilerek A* algoritması Dijkstra gibi çalışır
                  toplam_maliyet = yeni_sure + tahmini_sure  # Toplam maliyeti hesapla (geçen süre + tahmini süre)
                  heapq.heappush(pq, (toplam_maliyet, id(komsu), komsu, rota + [komsu]))  # Öncelik kuyruğuna yeni öğeyi (toplam maliyet, tie-breaker, komsu, güncellenmiş rota) ekle
      return None  # Eğer hedefe ulaşılamadıysa None değerini döndür

      """A* algoritması kullanarak en hızlı rotayı bulur

        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. A* algoritmasını kullanarak en hızlı rotayı bulun
        3. Rota bulunamazsa None, bulunursa (istasyon_listesi, toplam_sure) tuple'ı döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın

        İpuçları:
        - heapq modülünü kullanarak bir öncelik kuyruğu oluşturun, HINT: pq = [(0, id(baslangic), baslangic, [baslangic])]
        - Ziyaret edilen istasyonları takip edin
        - Her adımda toplam süreyi hesaplayın
        - En düşük süreye sahip rotayı seçin
      """

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB

    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar

    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören

    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma

    # Test senaryoları
print("\n=== Test Senaryoları ===")  # Ekrana test senaryolarının başlığını yazdır

# Senaryo 1: AŞTİ'den OSB'ye
print("\n1. AŞTİ'den OSB'ye:")  # Ekrana senaryo 1'in başlığını yazdır
rota = metro.en_az_aktarma_bul("M1", "K4")  # "M1" ve "K4" istasyonları arasında en az aktarmalı rotayı bul
if rota:  # Eğer rota bulunduysa
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))  # Rotadaki istasyon adlarını, " -> " ile ayrılmış şekilde ekrana yazdır

sonuc = metro.en_hizli_rota_bul("M1", "K4")  # "M1" ve "K4" istasyonları arasında en hızlı rotayı bul
if sonuc:  # Eğer sonuç bulunduysa
    rota, sure = sonuc  # Sonuçtaki rota ve süre bilgilerini ayır
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))  # Rotadaki istasyon adlarını ve toplam süreyi ekrana yazdır

# Senaryo 2: Batıkent'ten Keçiören'e
print("\n2. Batıkent'ten Keçiören'e:")  # Ekrana senaryo 2'nin başlığını yazdır
rota = metro.en_az_aktarma_bul("T1", "T4")  # "T1" ve "T4" istasyonları arasında en az aktarmalı rotayı bul
if rota:  # Eğer rota bulunduysa
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))  # Rotadaki istasyon adlarını, " -> " ile ayrılmış şekilde ekrana yazdır

sonuc = metro.en_hizli_rota_bul("T1", "T4")  # "T1" ve "T4" istasyonları arasında en hızlı rotayı bul
if sonuc:  # Eğer sonuç bulunduysa
    rota, sure = sonuc  # Sonuçtaki rota ve süre bilgilerini ayır
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))  # Rotadaki istasyon adlarını ve toplam süreyi ekrana yazdır

# Senaryo 3: Keçiören'den AŞTİ'ye
print("\n3. Keçiören'den AŞTİ'ye:")  # Ekrana senaryo 3'ün başlığını yazdır
rota = metro.en_az_aktarma_bul("T4", "M1")  # "T4" ve "M1" istasyonları arasında en az aktarmalı rotayı bul
if rota:  # Eğer rota bulunduysa
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))  # Rotadaki istasyon adlarını, " -> " ile ayrılmış şekilde ekrana yazdır

sonuc = metro.en_hizli_rota_bul("T4", "M1")  # "T4" ve "M1" istasyonları arasında en hızlı rotayı bul
if sonuc:  # Eğer sonuç bulunduysa
    rota, sure = sonuc  # Sonuçtaki rota ve süre bilgilerini ayır
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))  # Rotadaki istasyon adlarını ve toplam süreyi ekrana yazdır
