
def lingkaran() :
     phi = 3.14
     r = float(input("Masukkan panjang jari-jari lingkaran: "))
     luas = phi*r*r
     print("Luas lingkaran adalah : "+ str(luas))
def persegi_panjang ():
     p = float(input("Masukkan panjang persegi panjang: "))
     l =  float(input("masukkan lebar persegi panhjang: "))
     luas = p*l
     print("Luas persegi panjang adalah" + str(luas))
def tabung():
     phi = 3.14
     r = float(input("Masukkan jari jari tabung: "))
     t = float(input("masukkan tinggi tabung: "))
     luas = luas=int(2*phi*r*(t+r))
     print("Luas permukaan tabung adalah: " +str(luas))

lingkaran() 
print()
persegi_panjang()
print()
tabung()
