'''

PROBLEMLER

Problem 1. (30 puan) Tam bölenlerinin sayısına kalansız bölünebilen sayılara Tau sayısı denir. Örneğin, 12 sayısının tam bölenleri 1,2,3,4,6 ve 12 olup toplam 6 tanedir ve 12 sayısı 6’ya tam bölündüğü için bir Tau sayısıdır. Buna göre klavyeden girilen bir sayının Tau sayısı olup olmadığını bulan algoritmayı yazınız ve akış diyagramını Flowgorithm kullanarak çizip ekran görüntüsünü buraya ekleyiniz.
Çözüm 1.
1.Başla
2. Bir “bölünen_sayi” adi altında bir değişken tanımlayıp bu değişkene 0 değerini atıyoruz.
3.Kullanıcıdan Bir Sayı İstiyoruz.
4. For Döngüsü İle birlikte Bir “g” Değişkeni oluşturuyoruz ve bu değişkene ‘girdiğimiz sayı ,0 ve -1’ limitleri koyuyoruz.
5. Eğer girdiğimiz sayı g değişkenine böldüğümüzde kalan 0 ise “bölünen_sayi” değişkenine her aşamada 1 ekliyoruz.
6.”bölünen_sayı” değişkenimiz eğer girdiğimiz sayıyı böldüğümüzde kalan 0 ise bilgisayar “Bu bir Tau Sayısıdır” Çıktısı Oluşturulur.
7.Kalan 0 Değil ise Bilgisayar “Bu bir Tau sayısı değildir.” Çıktısı Oluşturur.
8.Çıkış


Problem 2. (20 puan) While döngüsü ve “//” operatörü ile kullanıcı tarafından girilen bir sayıyı 2lik tabana çeviren ve ekrana yazdıran Python kodunu yazınız.
Not: // operatörü bir bölme işleminde bölüm kısmını tamsayı olarak verir. Örneğin: 7//3 işlem sonucu 2 olarak değerlendirir.
Çözüm 2.
'''
from math import pow #import pow fonksiyon x sayisinin üstünü  almıya yarar. pow(2,3)= 2*2*2 =8 demektir.
ikilik=0
kalan=0 #Burada İhtiyacımız olan 3 tane Değişken Tanımlıyoruz.
basamak_sayisi=0
sayi=int(input("Lütfen İkilik Sisteme Çevirilecek Sayiyi Giriniz: ")) #Kullanıcıdan Girmek istediği sayinin girdisini alıyor.
while(sayi>0): #Burada Ondalık Sistemdeki Sayiyi İkilik Sisteme Çevirme İşlemini Yapıyoruz.
    basamak_sayisi=int((sayi%2)*pow(10,kalan))
    kalan+=1
    sayi=sayi//2
    ikilik=ikilik+basamak_sayisi
print("Sayinın Değeri: ",ikilik) #İkilik Sisteme Çevrilmiş Sayımızı Print Kullanarak Yazdırıyoruz
'''
Problem 3. (20 puan) Bileşik sayı, en az iki asal sayının çarpımı olarak yazılabilen pozitif tam sayıdır.
Tanım olarak, 1'den büyük her tam sayı ya asal ya da bileşik sayıdır. 
Buna göre kullanıcının girdiği bir sayıya kadar olan bütün bileşik tam sayıları yazdıran Python programını yazınız.
Çözüm 3.
'''
sayi=int(input("Lütfen Sayı Giriniz: ")) #Kullanıcıdan Bir Girdi Alınır.
list=0      #İki Değişken alıyoruz ve bunların değerini 0 yapıyoruz. (Döngüde kullanmak için 0 yazdık)
list1=0
for i in range(2,(sayi+1)):  #Girilen Sayının Asal Sayı olup olmadığını bulmak için döngü kuruyoruz.
    list=0
    for e in range(2,i):
        if(i%e==0):
            list+=1
            break
    if(list==1):
        print(i)
        list1+=1

'''
Problem 4. (30 puan) Bir sayısal loto çekilişi için rastgele 8 kupon hazırlayan bir program yazacaksınız. Bu çekilişte çekilen sayılar 1-49 arasındadır. Programın çıktısı aşağıdaki gibi olabilir. Programınızda random kütüphanesinden randint() fonksiyonunu ve while ya da for döngüsünü kullanacaksınız.
Not: Sayıları küçükten büyüğe sıralı olmasına gerek yoktur.
Çözüm 4.
'''
from random import randint  #Kolonlara Rastgele Bir Sayı Atamak İçin Bu fonksiyonu Kullandım.
a=0
sayilar = [0,0,0,0,0,0,0,0] #Sayılar Adı altında 8 sayılık bir liste oluşturuyoruz.
for loto in sayilar:
    while a< len(sayilar):
        sayi=randint(1,49)  #Burada Her Kolonun İçine 8 tane 1'den 49a Kadar,
        if sayi not in sayilar: #Rastgele Gelecek Sayılar İçin Bir Döngü Oluşturuyoruz.
            sayilar[a]=sayi
            a+=1
    print("Kolon",sayilar)      #Oluşturulan Fonksiyonu  Print Fonksiyonu İle Yazdırıyoruz.
    a=0
