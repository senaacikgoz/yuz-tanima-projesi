<<<<<<< HEAD
# yuz-tanima-projesi
=======
📚 Yüz İfadelerine Göre Çalışma Öneri Sistemi

Bu proje, yapay zeka ve duygu analizini birleştirerek yüz ifadesi üzerinden öğrencinin ruh halini algılar ve buna uygun çalışma önerileri sunar. Amaç, öğrencinin duygusal durumuna göre daha verimli ve kişiselleştirilmiş bir öğrenme deneyimi sağlamaktır.

🚀 Proje Amacı

Yeni nesil eğitim çözümleri geliştirmek için tasarlanan bu sistem, gerçek zamanlı duygu tanıma teknolojisini kullanarak öğrencinin ruh halini analiz eder ve uygun bir çalışma stratejisi önerir. Özellikle çevrimiçi eğitim ortamlarında öğrencilerin motivasyonunu artırmaya yönelik yenilikçi bir adımdır.

🎯 Nasıl Çalışır?

1. **Kamera Açılır** – Kullanıcının yüzü canlı olarak analiz edilir.
2. **Duygu Tespiti** – `fer` ve `deepface` kütüphaneleri ile duygular analiz edilir.
3. **Öneri** – Tespit edilen duyguya göre kullanıcıya özel çalışma önerisi gösterilir.

🧠 Kullanılan Teknolojiler

- `Python`
- `OpenCV` – Görüntü işleme ve kamera erişimi
- `FER` – Yüz ifadelerinden duygu analizi
- `DeepFace` – Alternatif duygu tespiti
- `NumPy` – Veri işlemleri

📂 Dosya Yapısı

yuz-tanima-projesi/
│
├── venv/                    # Sanal ortam
├── main.py                  # Kamera ve yüz tanıma uygulaması
├── emotion_utils.py         # DeepFace ile duygu analizi
├── suggestion_utils.py      # Duyguya göre öneriler
├── requirements.txt         # Gereken kütüphaneler
└── README.md                # Proje açıklaması


💡 Duyguya Göre Çalışma Önerileri

Sistem, yüz ifadenizi analiz ederek aşağıdaki yedi temel duygudan birini tespit eder ve buna göre çalışma önerisinde bulunur:

Duygu               Açıklama

Happy (Mutlu)       :Enerjin yüksek! Bu verimlilikle daha önce zorlandığın konulara odaklanmak için mükemmel bir zaman.
Sad (Üzgün)         :Biraz keyfin kaçmış gibi. Daha hafif ve ilgini çeken konularla başlamak motivasyonunu artırabilir. Belki kısa bir mola da iyi gelebilir.
Angry (Sinirli)     :Öfkelisin. Hemen çalışmaya başlamadan önce kısa bir yürüyüş yapabilir, nefes egzersizleriyle rahatlayabilirsin. Ardından sade konularla devam etmek en iyisi.
Surprise (Şaşırmış) :Beklenmedik bir ruh halindesin. Bu şaşkınlık duygusunu yeni bir şey öğrenmek için kullanabilirsin. Yeni bir konu keşfetmenin tam zamanı!
Fear (Korku/Endişe) :Endişelisin. Kolay ve temel konularla başla, kendine güvenin arttıkça daha zor konulara geçebilirsin.
Neutral (Nötr)      :Duygusal olarak dengedesin. Mevcut çalışma programınla devam etmen için uygun bir zaman.
Disgust (İğrenme)   :Kendini motive etmekte zorlanıyor olabilirsin. Kısa ve ilgi çekici bir video izleyip ardından düşük tempolu bir çalışmayla başlamak sana iyi gelir.

🛠️ Kurulum

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

```bash
# Sanal ortam oluşturun
python -m venv venv
source venv/bin/activate  
# Windows için: venv\Scripts\activate

# Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

🚀 Kullanım
Terminal üzerinden main.py dosyasını çalıştırarak gerçek zamanlı duygu analizi başlatabilirsiniz:

python main.py

❌ Mevcut Durum ve Sorunlar

DeepFace ile duygu analizi çalışıyor fakat bazı sistemlerde model indirme sürecinde gecikme olabiliyor.

Arayüz ve öneri entegrasyonu zaman darlığından ötürü tamamlanamadı.

Sistem gerçek zamanlı çalışıyor ancak duyguya bağlı öneri gösterimi şu anda sadece fonksiyon olarak tanımlı.

📌 Geliştirilebilir Yönler

Web arayüzü veya mobil uygulama entegrasyonu.

Öğrenci profiline göre önerilerin kişiselleştirilmesi.

Duygu analizi sonrası otomatik içerik öneri sistemi (video, konu, ders).

>>>>>>> a69992c (İlk proje yüklemesi: duyguya göre çalışma öneri sistemi)
