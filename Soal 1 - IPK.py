from texttable import Texttable

table = Texttable()
no = 0
nim = []
nama = []
alamat = []
asalSekolah = []
kodeProdi = []
ipkAwal = []
uts = []
uas = []
tm = []

while True:    
    Nim = input('NIM : ')
    nim.append(Nim)
    Nama = input('Nama : ')
    nama.append(Nama)
    Alamat = input('Alamat : ')
    alamat.append(Alamat)
    Sekolah = input('Asal Sekolah : ')
    asalSekolah.append(Sekolah)
    Prodi = input('Kode Prodi : ')
    kodeProdi.append(Prodi)
    Ipk = input('Nilai IPK Awal : ')
    ipkAwal.append(Ipk)
    Uts = input('Nilai UTS : ')
    uts.append(Uts)
    Uas = input('Nilai UAS : ')
    uas.append(Uas)
    Tm = input('Nilai TM : ')
    tm.append(Tm)

    jawab = ' '
    while jawab != 'y' and jawab != 't':
        jawab = input('Tambah Data (y/t)?' )
    no+=1
    if jawab == 't':
        break

print('UNIVERSITAS ABC')
for a in range (no):
    b = float(uts[a])*30/100
    c = float(uas[a])*40/100
    d = float(tm[a])*30/100
    ips = b+c+d
    ipk = (float(ipkAwal[a]) + ips) / 2
    table.add_rows([['No', 'NIM', 'Nama', 'Alamat', 'Asal Sekolah', 'Kode Prodi', 'Nilai IPK Awal', 'Nilai UTS', 'Nilai UAS', 'Nilai TM', 'Nilai IPS', 'IPK'],[a+1,nim[a],nama[a],alamat[a],asalSekolah[a],kodeProdi[a],ipkAwal[a],uts[a],uas[a],tm[a],ips,ipk]])
    print(table.draw())

'''if kodeProdi == 'TI' and kodeProdi == 'SI':
    elif ipk > 75 and ipk <= 85:
        print('Beasiswa 20%')
    elif ipk > 85 and ipk <= 100:
        print('Beasiswa 30%')
    else:
        print('Tidak Dapat Beasiswa')

if kodeProdi == 'DKV' and kodeProdi == 'Teknik Industri':
    elif ipk > 75 and ipk <= 85:
        print('Beasiswa 25%')
    elif ipk > 85 and ipk <= 100:
        print('Beasiswa 35%')
    else:
        print('Tidak Dapat Beasiswa')'''
