data = "0"
nilai = 0
hasil = 0

while (data != ""):
    data = str(input ("Masukan Nilainya : ")).upper()
    nilai += 1 
    if (data == ""):
        break 

    elif data in ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "E"]:
        if data ==  "A":
            hasil += 4.00
            print("nilai = 4")
        elif data == "A-" :
            hasil += 3.75 
            print("nilai = 3.75")
        elif data == "B+":
            hasil += 3.50
            print("nilai = 3.50")
        elif data == "B":
            hasil += 3.00
            print("nilai = 3.00")
        elif data == "B-":
            hasil += 2.75
            print("nilai = 2.75")
        elif data == "C+":
            hasil += 2.50
            print("nilai = 2.50")
        elif data == "C":
            hasil += 2.00
            print(" nilai = 2.00")
        elif data == "C-":
            hasil += 1.75
            print("nilai = 1.75")
        elif data == "D":
            hasil += 1.50
            print("nilai = 1.50")
        elif data == "E":
            hasil += 1.25
            print("nilai = 1.25")
    else:
        if data != ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "E"]:
            nilai = nilai - 1
            print ("Data tidak valid : ")

rata_rata = hasil / (nilai -1)
print("nilai rata-rata ", rata_rata)


        
                