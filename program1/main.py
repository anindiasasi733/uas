
print("===DAFTAR NILAI===")
###tambah data
print("==============tambah data==============")
nama1 = ['jeno', 'hiyyih', 'jun', 'soobin']
nilai2 = [90, 100, 99, 80]

print (nama1[0],nilai2[0])
print (nama1[1],nilai2[1])
print (nama1[2],nilai2[2])
print (nama1[3],nilai2[3])

###ubah data
print ("==============ubah data==============")
nama1 = ['jeno', 'hiyyih', 'jun', 'soobin']
nilai2 = [90, 100, 99, 80]
print(nama1)
print(nilai2)

nama1.append("akbar")
nilai2.append("88")
print (" setelah data ditambahkan :", nama1, nilai2)

###hapus data
print("==============hapus data==============")
nama1 = ['jeno', 'hiyyih', 'jun', 'soobin', 'akbar']
nilai2 = [90, 100, 99, 80, 88]
print(nama1)
print(nilai2)

del (nama1[2])
del (nilai2[2])
print ("Setelah dihapus nilai pada index 2 : ", nama1, nilai2)

###cari data
print("==============cari data==============")
a = ['jeno', 'hiyyih', 'jun', 'soobin', 'akbar']
nilai = [90, 100, 99, 80, 88]

cari = input("Masukkan nama yang dicari: ")
ketemu = False
for i in range(0, len(a)):
  if cari == a[i]:
    ketemu = True
    break

if ketemu:
  print ("Nilai: ", cari, "berhasil ditemukan")
else:
  print ("Nilai: ", cari, "tidak ditemukan")


##view nilai

print("===VIEW NILAI===")
jeno = 99
hiyyih = 100
soobin = 70
jun = 85

print("nilai jeno = "+str(jeno)+ " dan nilai hiyyih = " +str(hiyyih)+ \
    " dan nilai soobin = " +str(soobin)+ " dan nilai jun = "+str(jun))


##input nilai

print("===INPUT NILAI===")
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