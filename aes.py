import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def select_file():
    root = tk.Tk()
    root.withdraw()  # Ana pencereyi gizle

    file_path = filedialog.askopenfilename()  # Dosya seçme iletişim kutusunu aç

    if file_path:
        print("Seçilen dosya:", file_path)
        # Dosyayı şifreleme fonksiyonunu çağır
        encrypt_file(file_path)

def encrypt_file(file_path):
    key = get_random_bytes(32)  # 512-bitlik rastgele anahtar oluştur

    # Dosyayı okuma ve şifrelemeyi uygulama
    with open(file_path, 'rb') as file:
        file_data = file.read()

        # AES şifreleme nesnesini oluşturma
        cipher = AES.new(key, AES.MODE_EAX)

        # Şifrelenmiş veriyi ve etiketleri oluşturma
        ciphertext, tag = cipher.encrypt_and_digest(file_data)

    # Şifrelenmiş veriyi dosyanın üzerine yazma
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(cipher.nonce + tag + ciphertext)

    print(f"{file_path} başarıyla şifrelendi")

    # Şifre anahtarını bir TXT dosyasına yazma
    key_file_path = file_path + "_key.txt"
    with open(key_file_path, 'wb') as key_file:
        key_file.write(key)

    print(f"Şifre anahtarı dosyaya yazıldı: {key_file_path}")

def main():
    select_file()

if __name__ == "__main__":
    main()
