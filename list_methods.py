isimler = ["Ada", "Yiğit", "Hasan", "Beril"]
yaslar = [1998, 2000, 1998, 1987]

# cenk ismini listenin sonuna ekleyin
isimler.append("cenk")

# sena ismini listenin başına ekleyiniz
isimler.insert(0, "sena")

#yiğit isminin indexini bulma
sonuc = isimler.index("Yiğit")
print(sonuc)

# yiğit ismini listeden silin
isimler.remove("Yiğit")
print(isimler)

#beril listenin bir elemanı mıdır?
sonuc = "Beril" in isimler
print(sonuc)

#listenin elemanlarını tersine çevririn
isimler.reverse()
yaslar.reverse()

#liste elemanlarını sıralayın
isimler.sort()
yaslar.sort()

# str = "Iphone X, Iphone XR" karakter dizisini listeye çevirin.
s = "Iphone X, Iphone XR"
sonuc = s.split(",")
print(sonuc)

# yaslar dizisinin en büyük ve en küçük elemanı nedir?
sonuc = max(yaslar)
print(sonuc)
sonuc = min(yaslar)
print(sonuc)

# yaslar listesinde kaç tane 1998 değeri vardır?
print(yaslar.count(1998))

# yaslar dizisinin tüm elemanlarını siliniz
yaslar.clear()

# kullanıcıdan alınan 3 tane markayı bir listede gösterin
liste = []

marka = input("marka giriniz : ")
liste.append(marka)

marka = input("marka giriniz : ")
liste.append(marka)

marka = input("marka giriniz : ")
liste.append(marka)



