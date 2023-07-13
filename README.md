## Dosya Şifreleme

Bu Python kodu, kullanıcının bir dosya seçmesine izin veren bir arayüz sağlar ve seçilen dosyayı AES-256 algoritması kullanarak şifreler.

### Kullanım

1. `select_file()` fonksiyonu, Tkinter kütüphanesini kullanarak bir dosya seçim iletişim kutusu açar ve kullanıcının bir dosya seçmesini bekler.

2. Kullanıcı bir dosya seçtikten sonra, `file_path` değişkenine seçilen dosyanın yolunu kaydeder ve bu dosyanın şifrelemesini yapmak için `encrypt_file()` fonksiyonunu çağırır.

3. `encrypt_file()` fonksiyonu, AES-256 algoritması için 32 byte (256 bit) uzunluğunda bir rastgele anahtar oluşturur.

4. Seçilen dosyayı açar ve içeriğini `file_data` değişkenine kaydeder.

5. AES şifreleme nesnesini `cipher` olarak oluşturur ve belirlenen anahtar ile şifreleme modunu (AES.MODE_EAX) kullanır.

6. `cipher` nesnesini kullanarak dosyanın içeriğini şifreler ve şifrelenmiş veriyi `ciphertext` değişkenine kaydeder.

7. Şifrelenmiş veriyi, orijinal dosyanın üzerine yazar ve dosyayı şifrelenmiş haliyle günceller.

8. Şifre anahtarını bir TXT dosyasına kaydeder ve dosya adının sonuna "_key.txt" ekler.

# AES-256 Şifreleme Algoritması

Bu Readme.md dosyası, AES-256 şifreleme algoritmasının nasıl çalıştığını adım adım açıklamaktadır.

## Algoritma Özeti

AES (Advanced Encryption Standard), blok şifreleme algoritması olarak kullanılan bir simetrik şifreleme algoritmasıdır. AES-256, 256 bit anahtar kullanarak veriyi şifrelemek için kullanılan bir varyantıdır.

## Adım 1: Anahtar Oluşturma

AES-256 şifrelemesi için 256 bit (32 byte) bir anahtar oluşturulur. Bu anahtar rastgele ve güvenli bir şekilde oluşturulmalıdır.

## Adım 2: Veri Bloklarına Bölme

Şifrelenecek veri, 128 bitlik (16 byte) bloklara bölünür. Her blok ayrı ayrı işlenir.

## Adım 3: Şifreleme

Her veri bloğu, anahtar kullanılarak şifrelenir. Şifreleme işlemi, karmaşık matematiksel dönüşümler ve substitüsyonlar kullanır.

## Adım 4: Şifreli Veri Çıktısı

Her veri bloğu, şifreleme işleminden sonra şifreli veri olarak çıktı verir. Şifreli veri blokları bir araya getirilerek tam şifreli veri oluşturulur.

## Adım 5: Şifre Çözme

Şifreli veri, doğru anahtar kullanılarak tersine işlemler uygulanarak şifre çözülür. Bu adım, şifreleme adımlarının tersine çevrilmesiyle gerçekleştirilir.


## AES-256 Şifreleme Algoritması Adımları ve Hücre Karıştırması

AES-256 (Advanced Encryption Standard 256-bit), güçlü bir simetrik şifreleme algoritmasıdır. İşte AES-256 algoritmasının 4 aşaması ve hücre karıştırmasını gösteren bir tablo:

### Aşama 1: Başlangıç Değerleri

|    |    |    |    |
|----|----|----|----|
| a2 | 7q | c7 | F1 |
| 1d | 4a | 5c | 6e |
| e8 | b3 | 9f | 2d |
| 3c | 9b | a7 | f0 |

### Aşama 2: Dönüşümler

|    |    |    |    |
|----|----|----|----|
| 2b | 3x | 9z | d8 |
| u2 | h6 | g0 | x9 |
| 1a | z5 | k7 | c0 |
| r4 | p9 | 5l | 6j |

### Aşama 3: Karıştırma

|    |    |    |    |
|----|----|----|----|
| p5 | 6k | y4 | m9 |
| q8 | n5 | b7 | 2t |
| 3q | i9 | 8m | s2 |
| o0 | x2 | 7s | h5 |

### Aşama 4: Şifrelenmiş Hücreler

|    |    |    |    |
|----|----|----|----|
| c1 | d6 | z8 | 4e |
| 7s | h5 | c1 | d6 |
| z8 | 4e | 7s | h5 |
| d6 | z8 | 4e | 7s |

Bu tabloda, AES-256 şifreleme algoritmasının 4 aşaması ve hücre karıştırmasını adıyla birlikte gösteren bir Markdown tablosu bulunmaktadır. Her aşamanın yanında adı belirtilmiştir.

Bu örnekteki değerler sadece görsel amaçlar için basit bir şekilde temsil edilmektedir. AES-256 algoritmasının gerçek uygulamasında kullanılan dönüşümler ve karıştırma işlemleri daha karmaşıktır.

AES-256 algoritması, güvenli bir şekilde veriyi şifrelemek için yaygın olarak kullanılan bir algoritmadır. Daha fazla ayrıntı için AES-256 algoritmasının resmi belgelendirme kaynaklarına başvurabilirsiniz.



## Lisans

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bu projeyi [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisansladık. Lisansın tam açıklamasını burada bulabilirsiniz.
















[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bu projeyi [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisansladık. Lisansın tam açıklamasını burada bulabilirsiniz.
