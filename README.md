# Metro Ağı Rota Hesaplama Projesi

Bu proje, bir metro ağını temsil eden ve iki farklı rota bulma algoritmasını (BFS ve A* algoritmaları) uygulayan bir Python uygulamasıdır. Projede, metro istasyonlarını, hatlarını ve aralarındaki bağlantıları modelleyerek, kullanıcıların iki istasyon arasındaki en az aktarmalı veya en hızlı rotayı bulmasını sağlıyoruz.

---

## Proje Hakkında

Proje, gerçek yaşam senaryolarında metro hatları ve aktarma noktaları üzerinden rota hesaplama problemini çözmek amacıyla geliştirilmiştir. Metro ağındaki her istasyon, benzersiz ID, ad ve hattı gibi özelliklere sahip olup, diğer istasyonlarla arasında geçiş süresi bilgileri de tutulmaktadır. Bu yapıyı kullanarak, iki algoritma ile rota hesaplama işlemleri yapılmaktadır:

- **BFS (Genişlik Öncelikli Arama):** En az aktarmalı rotayı bulmak için kullanılır.
- **A* Algoritması (veya Dijkstra Yaklaşımı):** En hızlı, yani en kısa sürede ulaşılabilecek rotayı bulmak için uygulanır.

---

## Teknik Detaylar

### Kullanılan Teknolojiler ve Modüller

- **Python 3.x:** Projenin temel programlama dili.
- **collections (defaultdict, deque):** Veri yapıları oluşturmak ve hızlı kuyruk işlemleri gerçekleştirmek için kullanılmıştır.
- **heapq:** A* algoritması için öncelik kuyruğu (priority queue) işlemlerini sağlamak amacıyla kullanılmıştır.
- **typing:** Kodun okunabilirliğini ve anlaşılabilirliğini artırmak için tip ipuçları eklenmiştir.

### Sınıf ve Fonksiyon Yapısı

- **Istasyon Sınıfı:**  
  - Metro istasyonlarını temsil eder.
  - Her istasyonun benzersiz ID, adı ve ait olduğu hat bilgisi bulunur.
  - Ayrıca, diğer istasyonlarla olan bağlantılar (komşular) ve bu bağlantıların süre bilgileri tutulur.
  
- **MetroAgi Sınıfı:**  
  - Metro ağını yönetir; tüm istasyonlar ve hatlar bu sınıfta saklanır.
  - **istasyon_ekle:** Yeni istasyonların eklenmesi işlemini gerçekleştirir.
  - **baglanti_ekle:** İki istasyon arasındaki çift yönlü bağlantıyı kurar.
  - **en_az_aktarma_bul:** BFS algoritması ile, başlangıç ve hedef istasyon arasında en az aktarmalı rotayı bulur.
  - **en_hizli_rota_bul:** A* algoritması (Dijkstra yaklaşımı) kullanarak, başlangıç ve hedef istasyon arasında en kısa sürede ulaşılabilecek rotayı belirler.

### Algoritmaların Uygulanması

- **BFS Algoritması:**  
  Projede en az aktarmalı rota bulmak için uygulanmıştır.  
  1. Başlangıç ve hedef istasyonların varlığı kontrol edilir.  
  2. `deque` yapısı kullanılarak, başlangıç istasyonu ve rota bilgisi kuyrukta tutulur.  
  3. Her adımda, kuyruktan çıkarılan istasyonun komşuları kontrol edilerek, henüz ziyaret edilmemiş istasyonlar kuyrukta işlenir.
  4. Hedefe ulaşılırsa rota döndürülür, aksi halde rota bulunamazsa `None` değeri döner.

- **A* Algoritması:**  
  En hızlı rotayı bulmak için uygulanmıştır.  
  1. Başlangıç ve hedef istasyonlar kontrol edilir.
  2. `heapq` modülü kullanılarak öncelik kuyruğu oluşturulur; başlangıç istasyonu, toplam süre (başlangıçta 0) ve rota bilgileri kuyrukta tutulur.
  3. Her adımda, en düşük toplam süreye sahip istasyon işlenir, komşuların üzerinden geçilerek yeni süreler hesaplanır.
  4. Eğer daha kısa bir yol bulunursa, ilgili istasyon ve rota bilgileri güncellenir.
  5. Hedefe ulaşıldığında rota ve toplam süre döndürülür; rota bulunamazsa `None` döner.

### Geliştirme Süreci ve Deneyimler

Bu projeyi geliştirirken, metro ağlarının nasıl modellenebileceği ve iki farklı rota hesaplama algoritmasının (BFS ve A*) nasıl uygulanabileceği üzerinde yoğun araştırma yaptım. Hem veri yapılarını doğru seçmenin önemi hem de algoritmaların çalışma mantığını derinlemesine kavramak için zaman harcadım. Projede kod okunabilirliğini artırmak amacıyla tip ipuçları ve kapsamlı yorum satırları ekleyerek PEP 8 standartlarına uygun, temiz ve sürdürülebilir bir yapı oluşturmaya özen gösterdim. Projeyi geliştirirken kazandığım deneyimler, algoritma uygulamaları ve veri yapılarını kullanma konusundaki bilgi ve becerilerimi önemli ölçüde artırdı.

---

## Kurulum ve Çalıştırma

1. **Gereksinimler:**  
   - Python 3.x kurulumu  
   - Gerekli kütüphaneler: `heapq`, `collections` ve `typing` (Python’un standart kütüphaneleri içinde bulunmaktadır)

2. **Çalıştırma Adımları:**  
   - Proje dosyalarını (örneğin `metro_agi.py`) bir klasöre kopyalayın.
   - Terminal veya komut satırı aracılığıyla proje klasörüne gidin.
   - `python metro_agi.py` komutunu çalıştırarak projeyi başlatın.

---

## Sonuç

Bu proje, metro ağlarını ve rota hesaplamayı modelleyen basit ama etkili bir uygulamadır. Hem BFS hem de A* algoritmalarının uygulanması, gerçek dünya problemlerinde farklı çözüm stratejilerinin nasıl kullanılabileceğini göstermektedir. Projede yer alan kodlar ve yapı sayesinde, algoritmaların mantığı ve veri yapılarının kullanımı hakkında kapsamlı bir anlayış elde edilebilir.

---

> Projede yer alan tüm kodlar, verilen ipuçları doğrultusunda, kendi araştırmalarım ve elde ettiğim deneyimler ışığında geliştirilmiştir. Projenin her aşaması, sistematik bir yaklaşım ve titiz kodlama prensipleri gözetilerek hazırlanmıştır.
