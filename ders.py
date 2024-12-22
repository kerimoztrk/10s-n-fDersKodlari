
# Bu haftanın konusu 
# değişken ve sabit
#  tanımlama


"""
uc tane çift tırnak arasına yorum satırı
çoklu satır olarak yazılır

"""

'''
üç tane tek tırnak arasına yorum satırı
coklu satır olarak yazılır.
'''

# print(4+5+52+234/8)


# sayi = 5  #bu bir tamsayı (integer) değişlen tanımlamasıdır.

# sayi1 =5.0 #bu bir float (ondalıklı sayı) değşken tanmlamasıdır.

# print(type(sayi))

# print(type(sayi1))
#12metin="metin" şeklinde bir değişken tanımlama hatalıdır.
#degiskenlerin başına herhangi bir sayı gelemez
#değişkenler büyük küçük harf duyarlıdır.
#programlama dilinde kullanılan özel karakterler kullanılamaz
#değişlenin basına ve ortasına boşluk ifadesi konuklmaz
# ogrenci adı =" ali" şeklinde bir ifade hatalıdır. 
# metin="bu bir metindir."  
# Metin="Bu farklı bir metindir"

# print(type(metin))
# print("Metin")
# print(Metin)


# _degisken=1
# degisken=1              doğru değişkeb isimlebdirmeleri
# degisken12=1
# degisken-türü="str"


# for = 4324
# if=5
# None =5      #bunlar özel karakter old için bu isimle değişken tanımlanamaz.



# yas = 25 # int
# sicaklik = 35.4 #float
# metin = " bu bir metindir " #string
# PI= 3.13159 #sabit


# print(type(yas))
# print(type(sicaklik))
# print(type(metin))
# print(type(PI))

# yas2=input("Yaşınızı giriniz:")
# yas2_int=int(yas2)
# print("5 sene sonraki yaşı =",yas2_int+5)

# a=5

# print(a)
# a +=5 

# print(a)

# a -=5

# print(a)

# a *=5

# print(a)

# a /=5

# print(a)


# aritmatiksel operatörler için uygulama örnekleri (-,+,/,*)

# sayi1=10
# sayi2=5


# toplam = sayi1+sayi2

# cikarma= sayi1-sayi2

# carpim = sayi1 * sayi2

# bolme = sayi1 / sayi2

# mod= sayi1 % sayi2

# print( toplam)
# print(cikarma)
# print( carpim)
# print(bolme)

# matematik=(int(input("mat notunu gir")))
# fizik=(int(input("fzk notunu gir")))
# yazilim=(int(input("yazlm notunu gir")))

# ortalama= (matematik+fizik+yazilim)/3

# print(ortalama)


# taban=10
# us=2

# sonuc= taban ** us

# print(sonuc)


#Temel Bilgiler  Karşılaştırma operatörleri

# ==  : İki değer eşit mi ?
# !=  : İki değe eşit değilmi ?
# >   : Soldaki değer sağdaki değerden büyükmü==?
# <   : soldaki değer ssağdaki değerde küçük mü ?
# >=  : Soldaki değer sağdaki değerden büyük mü veya eşitmi
# <=  : Soldaki değer sağdaki değerden küçük mü  veya eşit mi?
#
#


# not1= 70

# print(not1>=50)
# print(not1 ==100)
# print(not1<40)


# fiyat=200
# indirim=150

# print(fiyat>indirim)
# print(fiyat<=150)
# print( fiyat !=indirim)

# yas2=16

# print(yas2 >=18)
# print(yas2<18)
# print(yas2!=16)


# Mantıksal Operatörler

# Birden fazla koşulun birlikte kontrol edilmesine yarar.

#Temel açıklam

#and : Her iki koşul doğruysa TRUE
#or  : En az bir koşul dığruysa True
#not : Koşulun tersini döner

#bir öğrencinin sınavdan geçebilmesi için notu en az 50 olmalı ve katılım göstermeli

# not1=55
# katilim=True

# print (not1>=50 and katilim) #True (her iki koşulda doğru)
# print (not1<50 and katilim)#False (Not' 50 den küçük olduğu için)
# print (not katilim) #False 

# #bir alışverişte ücretsiz kargo ve %10 indirim koşulları kontol

# ucretsizKargo=True
# indirimYuzde10=False

# print(ucretsizKargo and indirimYuzde10) #False (indirim yok)
# print(ucretsizKargo or indirimYuzde10) #True en az bir koşul doğru)
# print(not ucretsizKargo) #False 

#etkinlik yaş orneği
#etkinliğe katılım için yaş kontrol

# yas=20

# print(yas>18 and yas<65) #True (18den büyük ve 65 den küçük old için)
# print(yas<18 or yas>65) #False (her iki koşulda yanlış)
# print(not(yas>18))

#kimlik operatörleri

#Amaç= iki nesnein aynı olup olmadığını sorgular

# temel bilgiler
# is: iki nesne aynı mı =
# is not : iki nesne farklı mı =

liste1=[1,2,3]
liste2=[1,2,3]
liste3=liste1

print(liste1 is liste2)
print(liste1 is liste3)
print(liste2 is not liste3)