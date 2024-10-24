umur  = 0
uang = 0
orang = 0

while (umur != ''):
    umur = str(input("Masukan Umur Anda : "))
    orang += 1
    if (umur == str('')):
        break
    else:
        
        if (int(umur) <= 2):
            print('GRATIS')
            uang += 0
            print("total bayar  = ", uang)
        elif (3 <= int(umur) <= 12):
            print("Harga $14.00")
            uang += 14.00
            print("total bayar  = ", uang)
        elif (150 >= int(umur) >= 65):
            print('Harga  $18.00')
            uang += 18.00
            print("total bayar = ", uang)
        elif (13 <= int(umur) <= 64):
            print('Harga $23.00')
            uang += 23.00
            print("total bayar= ", uang)
        else:
            orang -= 1
            print('INVALID')
            
if(orang == 1):
    print(" ")
else:
    bayar = float(input("Bayar = "))
    kembalian = bayar - uang
    print('Kembalian = ', kembalian)