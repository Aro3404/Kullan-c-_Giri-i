print('''
*******************
Kullanıcı Girişi
*******************
''')
a = "deneme"
b = "1234"
hak=5
while True:
    c = input("Kullanıcı Adı:")
    d = input("Şifre:")
    if (c == "yeni" and d == "şifre"):
        new_şifre=input("Yeni Şifreniz:")
        b = new_şifre
        print("Şifreniz başarıyla değiştirildi.")
        continue
    if (c == a and d != b):
        print("Şifre Hatalı.")
        print("Eğer şifrenizi unuttuysanız 'Kullanıcı Adı' ve 'Şifreye' sırsıyla ; yeni ve şifre yazın.")
        hak-=1
        print("Kalan Hak:", hak)
    elif (c != a and d == b):
        print("Kullanıcı Adı Hatalı.")
        hak-=1
        print("Kalan Hak:",hak)
    elif (c != a and d != b):
        print("Kullanıcı Adı ve Şifre Hatalı.")
        hak-=1
        print("Kalan Hak:", hak)

    else:
        print("Sisteme Başarıyla Girildi.Hoşgeldiniz☺.")
        break


    if (hak==0):
        print("Çok fazla yanlış burayı terk et.")
        break

