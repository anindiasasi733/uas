
list_nim=[]
list_nama=[]
list_tugas=[]
list_uts=[]
list_uas=[]
list_total=[]

ulang=2

for i in range(ulang):
    print ("data ke - " + str(i+1))
    list_nim.append(input("Masukan nim anda : "))
    list_nama.append(input("Masukan nama anda : "))
    list_tugas.append(int(input("Masukan nilai Tugas : ")))
    list_uts.append(int(input("Masukan nilai UTS : ")))
    list_uas.append(int(input("Masukan nilai UAS : ")))

for i in range(ulang):
    list_total.append((list_tugas[i] + list_uts[i] + list_uas[i] /3 ))


print("===========================================================")
print("Nim    Nama    Tugas    UTS    UAS")
print("===========================================================")

for i in range(ulang):
    print ("%s \t\t %s \t %i \t\t %i \t\t\t %i" % (list_nim[i], list_nama[i], list_tugas[i], list_uts[i], list_uas[i]))
print("===========================================================")