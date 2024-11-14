# cyphpass
# Cypher & Password Utility

Bu proje, çeşitli şifreleme ve şifre çözme işlemleri yapmak için tasarlanmış bir Python modülü içermektedir. Ayrıca, güvenli şifreler oluşturmak için bir şifre oluşturma aracı da sağlar.

## Özellikler

### 1. Cypher Sınıfı
`Cypher` sınıfı, çeşitli şifreleme teknikleri uygulamak ve şifreleri çözmek için kullanılabilir:

- **ROTn Şifreleme**: Belirtilen bir alfabe ve `n` değeri kullanarak bir mesajı döndürür. 
  - `ROTn`: Standart bir ROT şifreleme algoritmasıdır.
  - `rev_ROTn`: ROT şifreleme çözme işlemi.
  - `custom_ROT`: Kullanıcı tanımlı bir matematiksel denklem kullanarak özel bir ROT şifreleme sağlar.
  - `ceaser`: Basit bir Sezar şifrelemesi uygular.

- **Vigenere Şifreleme**: 
  - `encrypt_vigenere`: Vigenere algoritmasını kullanarak bir mesajı şifreler.
  - `decrypt_vigenere`: Vigenere algoritmasını kullanarak şifreli bir mesajı çözer.

- **Morse Kodu Dönüşümleri**:
  - `BitToMorse` ve `MorseToBit`: Morse kodunu bitlere ve tersi yönde dönüştürme işlevleri.
  - `stringToMorse` ve `morseToString`: Normal metni Morse koduna ve tersine çevirme işlevleri.

- **Dosya İşlemleri**:
  - `file_cypher`: Bir dosyayı verilen anahtar ile şifreler.
  - `file_decypher`: Bir dosyayı verilen anahtar ile çözer.

- **Anahtar Üretici**:
  - `key_maker`: Verilen alfabe koduna göre rastgele bir anahtar üretir.

### 2. Password Sınıfı
`Password` sınıfı, rastgele ve güvenli şifreler oluşturmak için kullanılabilir:

- **PIN**: Belirtilen uzunlukta sadece sayılardan oluşan bir PIN üretir.
- **Metin Tabanlı Şifreler**: 
  - `Textbased`: Kullanıcı tarafından belirlenen moda göre metin tabanlı bir şifre oluşturur.
    - **Mod 1**: Sadece küçük harfler.
    - **Mod 2**: Küçük ve büyük harfler.
    - **Mod 3**: Harfler ve rakamlar.
    - **Mod 4**: Harfler, rakamlar ve özel karakterler.

## Kurulum

Bu projeyi kullanmak için, Python'un yüklü olduğundan emin olun. Ardından dosyayı indirip çalıştırabilirsiniz.

## Kullanım

Cypher ve Password sınıflarını kullanmak için, öncelikle modülü içe aktarın:

```python
from cyphpass import Cypher, Password

# Cypher örneği
message = "Hello World!"
cypher = Cypher(message)
encrypted = cypher.ROTn("EN", 5)
decrypted = cypher.rev_ROTn("EN", 5)
print(f"Şifrelenmiş Mesaj: {encrypted}")
print(f"Çözülmüş Mesaj: {decrypted}")

# Password örneği
password_generator = Password(length=12, alp_code="EN")
password = password_generator.Textbased(mode=4)
print(f"Oluşturulan Şifre: {password}")
