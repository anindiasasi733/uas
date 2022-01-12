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



