print("Metode Fuzzy Tsukamoto")
"""
Keterangan:
VARIABEL PERMINTAAN
pmtb=permintaan banyak 
pmts=permintaan sedikit

VARIABEL PERSEDIAAN
psdb=persediaan banyak
psds=persediaan sedikit

VARIABEL PRODUKSI BARANG
prod_brgmax=produksi barang max
prod_brgmin=produksi barang min
"""
pmtb=5000
pmts=1000
psdb=600
psds=100
prod_brgmax=7000
prod_brgmin=2000
pmt=int(input("Masukan jumlah permintaan: "))
psd=int(input("Masukan jumlah persediaan: "))

#Variabel Permintaan
if pmt<=pmts:
    pmt_turun=1
    print("Derajat Keanggotaan pmt_turun: ",pmt_turun)
elif pmt>=pmts and pmt<=pmtb:
    pmt_turun=(pmtb-pmt)/(pmtb-pmts)
    print("Derajat keanggotaan pmt_turun= ",pmt_turun)
elif pmt>=pmtb:
    pmt_turun = 0
    print("Derajat keanggotaan pmt_turun=", pmt_turun)

if pmt<=pmts:
    pmt_naik=0
    print("Derajat Keanggotaan pmt_naik: ",pmt_naik)
elif pmt>=pmts and pmt<=pmtb:
    pmt_naik=(pmt-pmts)/(pmtb-pmts)
    print("Derajat keanggotaan pmt_naik= ",pmt_naik)
elif pmt>=pmtb:
    pmt_naik = 1
    print("Derajat keanggotaan pmt_naik=", pmt_naik)

#Variabel Persediaan
if psd<=psds:
    psd_sedikit=1
    print("Derajat Keanggotaan psd_sedikit: ",psd_sedikit)
elif psd>=psds and psd<=psdb:
    psd_sedikit=(psdb-psd)/(psdb-psds)
    print("Derajat keanggotaan psd_sedikit= ",psd_sedikit)
elif psd>=psdb:
    psd_sedikit=0
    print("Derajat Keanggotaan psd_sedikit: ",psd_sedikit)

if psd<=psds:
    psd_banyak=0
    print("Derajat Keanggotaan psd_banyak: ",psd_banyak)
elif psd>=psds and psd<=psdb:
    psd_banyak=(psd-psds)/(psdb-psds)
    print("Derajat keanggotaan psd_banyak= ",psd_banyak)
elif psd>=psdb:
    psd_banyak=1
    print("Derajat Keanggotaan psd_banyak: ",psd_banyak)

#Rule 1 : IF Permintaan BANYAK And Persediaan BANYAK THEN Produksi Barang BERTAMBAH")
def Rule1():
    prod_brg_bertambah1=min(pmt_naik,psd_banyak)
    return prod_brg_bertambah1
#Rule 2 : IF Permintaan SEDIKIT And Persediaan SEDIKIT THEN Produksi Barang BERKURANG")
def Rule2():
    prod_brg_berkurang1=min(pmt_turun,psd_sedikit)
    return prod_brg_berkurang1
#Rule 3 : IF Permintaan SEDIKIT And Persediaan BANYAK THEN Produksi Barang BERKURANG")
def Rule3():
    prod_brg_berkurang2=min(pmt_turun,psd_banyak)
    return prod_brg_berkurang2
#Rule 4 : IF Permintaan BANYAK And Persediaan SEDIKIT THEN Produksi Barang BERTAMBAH")
def Rule4():
    prod_brg_bertambah2=min(pmt_naik,psd_sedikit)
    return prod_brg_bertambah2

#Berkurang
z2 = prod_brgmax-(Rule2()*(prod_brgmax-prod_brgmin))
z3 = prod_brgmax-(Rule3()*(prod_brgmax-prod_brgmin))
#Bertambah
z1 = (Rule1()*(prod_brgmax-prod_brgmin))+prod_brgmin
z4 = (Rule4()*(prod_brgmax-prod_brgmin))+prod_brgmin

print("Menghitung z akhir dengan merata-rata semua z berbobot")
z=round(((Rule1()*z1)+(Rule2()*z2)+(Rule3()*z3)+(Rule4()*z4))/(Rule1()+Rule2()+Rule3()+Rule4()))
print("z=","(",Rule1(),"*",z1,")+(",Rule2(),"*",z2,")+(",Rule3(),"*",z3,")+(",Rule4(),"*",z4,"))/(",Rule1(),"+",Rule2(),"+",Rule3(),"+",Rule4(),"))")
print("Jadi jumlah makanan yang harus diproduksi sebanyak",z,"kemasan")