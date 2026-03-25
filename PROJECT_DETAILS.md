# Proje Detayları ve Yapı Kılavuzu

Bu dosya, bu İngilizce A1 kursu projesinin nasıl yapılandırıldığını, hangi dosyanın ne işe yaradığını ve JetBrains Academy Plugin ile nasıl çalıştığını adım adım açıklar.

## 1. Ana Dizin (Root) Dosyaları

*   **`course-info.yaml`**: Kursun "kimlik kartıdır". Kursun adını, özetini, hangi dilde olduğunu ve hangi derslerden (lesson) oluştuğunu burada tanımlarız.
*   **`README.md`**: Projeye genel bakış sağlar. Ders yapısını ve kurulum talimatlarını içerir.
*   **`.gitignore`**: Git sisteminin takip etmemesi gereken dosyaları (örneğin IDE ayarları veya geçici dosyalar) belirtir.

## 2. Ders Yapısı (`lesson1-basics`)

Proje, "Derslerden" (Lessons) oluşur. Şu anki dersimiz `lesson1-basics` klasörüdür.

*   **`lesson-info.yaml`**: Bu dersin içindeki görevlerin (tasks) hangi sırayla görüneceğini belirleyen dosyadır.

## 3. Görev (Task) Yapısı

Her ders, küçük "görevlerden" oluşur. Bir görev klasörünün içinde genellikle şunlar bulunur:

*   **`task.md`**: Öğrencinin IDE içinde sağ panelde gördüğü **ana metindir**. Teori anlatımı, talimatlar ve ipuçları buraya yazılır.
*   **`task-info.yaml`**: Görevin teknik ayarlarını içerir.
    *   Görevin tipi (Teori, Çoktan Seçmeli Quiz veya Kodlama).
    *   Quiz ise doğru cevap hangisi?
    *   Hangi dosyalar öğrenciye görünür olmalı? gibi bilgileri tutar.
*   **`main.py`** (Sadece Kodlama Görevlerinde): Öğrencinin kod yazacağı Python dosyasıdır. Genellikle içinde `TODO` veya `???` gibi doldurulması gereken alanlar bulunur.
*   **`tests/`** (Sadece Kodlama Görevlerinde): Öğrencinin yazdığı kodun doğruluğunu kontrol eden otomatik test scriptlerini içerir.

## 4. Görev Türleri

Bu kursta üç tip görev kullanıyoruz:

1.  **Theory (Teori):** Sadece bilgi verme amaçlıdır. Öğrenci metni okur ve "Next" butonuna basar.
2.  **Choice (Quiz):** Öğrenciye bir soru sorulur ve seçenekler sunulur. Doğru cevabı seçmesi istenir.
3.  **Code (Kodlama):** Öğrencinin Python kodu yazarak bir sorunu çözmesi veya bir kuralı uygulaması istenir.

---

Bu yapı sayesinde, hem İngilizce öğrenen biri için interaktif bir ortam sunulur hem de arka planda gerçek bir yazılım projesi gibi düzenli bir mimari korunur.
