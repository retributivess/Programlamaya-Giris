#ilk once değikenlerimizi tanımlayacagız ve while dongüsü yaratacagız
# dikkat! print("sonuc"int(a)+int(b)) = hatalı print("sonuc",int(a)+int(b)) = dogru (((virgül(,) koymayı unutma!))) 


while(True):
    a = input("bir sayi gir:")
    b = input("bir sayi daha gir")

    T = "t"
    C = "c"
    B = "b"
    I = "ı"


    print("hangi islemi istiyorsunuz: (T,C,B,I)")
    print("T = toplama C = carpma B = bölme I = cıkarma")
    cevap = input()

    if cevap == T :
        print("sonucunuz:",int(a)+int(b))

    elif cevap == C :
        print("sonucunuz:",int(a)*int(b))

    elif cevap == B :
        print("sonucunuz:",int(a)//int(b))

    elif cevap == I :
        print("sonucunuz:",int(a)-int(b))

    else:
        print("islem bulunamadı")

    E = "e"
    H = "h"
    
    print("cıkmak istermisiniz: (E,H)")
    
    sonuc = input()
    
    if sonuc == E :
        print("islem bittt")
        break
