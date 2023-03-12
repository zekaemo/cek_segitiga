# QUIZ

print("Cek Jenis Segitiga")

panjang_a= float(input("Masukkan sisi A: "))
panjang_b= float(input("Masukkan sisi B: "))
panjang_c= float(input("Masukkan sisi c: "))

if panjang_a ==  panjang_b == panjang_c:
    print("Segitiga adalah segitiga sama sisi")

elif panjang_a  == panjang_b or panjang_b == panjang_c or panjang_a == panjang_c:
    print("Segitiga adalah segitiga sama kaki")

else:
    print ("Segitiga adalah segitiga sembarang")