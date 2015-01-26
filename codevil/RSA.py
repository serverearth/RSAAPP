#-------------------------------------------------------------------------------
# Name:        module RSA
# Purpose:
#
# Author:      yanwar
#
# Created:     09/11/2014
# Copyright:   (c) yanwar 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import gmpy2, random, time, os, Pendukung_Kripto, wx
import EasyDialogs
import time
import DataLog
import datetime
def generate_kunci(id, direktori):
    '''untuk : menggenerate kunci RSA
    param : String id, String direktori
    return : List nilai kunci dan list Float waktu generate kunci RSA'''

    id = str(id)
    direktori = str(direktori)

    ## set time awal
    waktu_awal = time.clock()

    ## set level kunci
    level = 3

    ## set minimal dan maksimal untuk generate kunci
    minimal = int("1" + str("0" * (level -1 )))
    maksimal = int("9" * level)

    ## set bilangan prima p dan q
    p = gmpy2.next_prime(random.randrange(minimal,maksimal))
    q = gmpy2.next_prime(random.randrange(minimal,maksimal))

    ## set nilai modulo N
    n = gmpy2.mul(p, q)     # p * q

    ## set nilai phi
    tp = gmpy2.sub(p, gmpy2.mpz(1))    # (p - 1)
    tq = gmpy2.sub(q, gmpy2.mpz(1))    # (q - 1)
    phi = gmpy2.mul(tp,tq)                  # (p - 1) * (q - 1)

    ## set nilai e
    ## mencari nilai random sebanyak phi / 2
    ## untuk pembatasan iterasi dalam pencarian nilai gcd
    ## dengan syarat e dan phi coprime atau gcd e dan phi == 1
    batas = random.randrange(gmpy2.mpz(phi)/2)
    e = 0
    while True:
        batas = batas + 1
        ## greatest common divisor e & phi == 1 (coprime)
        es = gmpy2.gcd(batas,gmpy2.mpz(phi))
        if es == 1:
            e = batas
            break

    ## set nilai d
    d = gmpy2.invert(e,phi)

    ## time akhir
    waktu_akhir = time.clock()  -  waktu_awal

    ## set nama kunci
    kunci_publik = direktori + id +"-publick.key"
    kunci_rahasia = direktori + id+"-private.key"
    kunci_uji = direktori + id + "-pengujian.html"

    ## menyimpan kunci di dalam direktori
    ## index 0 : id kunci
    ## index 1 : Modulo N
    ## index 2 : Eksponen E
    with open(kunci_publik, "wb") as wpub:
        wpub.write(id + "\n")
        wpub.write(str(int(n)) + "\n")
        wpub.write(str(int(e)))

    ## index 0 : id kunci
    ## index 1 : Modulo N
    ## index 2 : Eksponen D
    with open(kunci_rahasia,"wb") as wpriv:
        wpriv.write(id + "\n")
        wpriv.write(str(int(n)) + "\n")
        wpriv.write(str(int(d)))

    ## simpan semua nilai kunci
    ## untuk melakukan pengujian
    with open(kunci_uji,"w") as wuji:
        wuji.write("<h3>RSA - Dhe Fud Resto</h3>")
        wuji.write("<pre>"+str(time.asctime( time.localtime(time.time())))+"</pre>")
        wuji.write("<table>")
        wuji.write("<tr>")
        wuji.write("<th colpsan=2>Identitas Kunci : "+id+"</th>")
        wuji.write("</tr>")
        ## prima p
        wuji.write("<tr>")
        wuji.write("<td>Prima P </td>")
        wuji.write("<td> : </td>")
        wuji.write("<td>"+str(int(p))+"</td>")
        wuji.write("</tr>")
        ## prima q
        wuji.write("<tr>")
        wuji.write("<td>Prima Q </td>")
        wuji.write("<td> : </td>")
        wuji.write("<td>"+str(int(q))+"</td>")
        wuji.write("</tr>")
        ## modulo N
        wuji.write("<tr>")
        wuji.write("<td>Modulo N </td>")
        wuji.write("<td> : </td>")
        wuji.write("<td>"+str(int(n))+"</td>")
        wuji.write("</tr>")
        ## totient PHI
        wuji.write("<tr>")
        wuji.write("<td>Totient PHI </td>")
        wuji.write("<td> : </td>")
        wuji.write("<td>"+str(int(phi))+"</td>")
        wuji.write("</tr>")
        ## eksponen E
        wuji.write("<tr>")
        wuji.write("<td>Eksponen E </td>")
        wuji.write("<td> : </td>")
        wuji.write("<td>"+str(int(e))+"</td>")
        wuji.write("</tr>")
        ## eksponen D
        wuji.write("<tr>")
        wuji.write("<td>Eksponen D </td>")
        wuji.write("<td> : </td>")
        wuji.write("<td>"+str(int(d))+"</td>")
        wuji.write("</tr>")
        wuji.write("</table>")

    ## kembalikan nilai kunci dan waktu pembuatan kunci
    ## dalam bentuk list
    ## index 0 : id
    ## index 1 : bilangan prima P
    ## index 2 : bilangan prima Q
    ## index 3 : bilangan modulo N
    ## index 4 : bilangan totient PHI
    ## index 5 : bilangan eksponen E
    ## index 6 : bilangan eksponen D
    ## index 7 : waktu pembuatan kunci
    ## index 8 : path dan file kunci publik
    ## index 9 : path dan file kunci rahasia
    return [id, int(p), int(q), int(n), int(phi), int(e), int(d), waktu_akhir, \
    kunci_publik, kunci_rahasia]
'''
## contoh penggunaan generate kunci
print generate_kunci("myidkey","D:/mydirectory")
'''

def enkripsi(direktori, filename, n, e, obj, kunci, user,file):
    '''
    untuk	: enkripsi file dengan kriptografi RSA
    param	: String direktori, String filename, int n, int e
    return	: Float waktu enkripsi, String fileenkripsi

    estimasi code : 13/Nov/2014
    ---------------------------
    menambahkan objek txt waktu
    untuk ditampilan nilai waktu akhir
    setelah proses enkripsi selesai.
    karena Thread tidak bisa menangkap return data dari suatu
    fungsi atau method.
    '''
    # estimasi code : 13/Nov/2014
    # menambahkan sedikit pengalihan kesalahan
    # jika suatu saat program terjadi error
    # karena sesuatu.
    # penambahan try dimaksudkan untuk
    # memberi tau user kesalahan yang terjadi
    # karena pada dasarnya Thread yang saya gunakan
    # berupa thread tanpa kita tahu letak kesalahannya dimana.
    try:
        # estimasi code : 13/Nov/2014
        # memulai waktu enkripsi
        # nilai waktu tersebut akan di simpan
        # ke variabel waktu_awal
        waktu_awal = time.clock()

        # estimasi code : 13/Nov/2014
        # mengeset tempat penyimpanan hasil file
        # yang selesai di enkripsi
        direktori = str(direktori)

        # estimasi code : 13/Nov/2014
        # menyimpan filename ke dalam
        # variabel filename yang sebelumnya
        # dilakukan pemformatan ke string
        # terlebih dahulu.
        filename = str(filename)

        # estimasi code : 13/Nov/2014
        # mengambil ekstensi file
        # dari filename. nilainya
        # yang di dapat adalah nama extensi file
        # tersebut. kita menggunakan fungsi ambil_nama_file
        # yang ada pada package Pendukung_Kripto.
        fileAekstensi = Pendukung_Kripto.ambil_nama_file(filename)

        # estimasi code : 13/Nov/2014
        # mengeset nama default name file
        # yang di jadikan nama file setelah proses
        # enkripsi selesai.
        nama_enkripsi = "enkripRSA-"


        # estimasi code : 13/Nov/2014
        # membuat tempat sekaligus nama file
        # yang digunakan untuk write binary file.
        # nilainya di simpan ke variabel namafile_enkripsi
        # sebagai contoh: [D:/enkripRSA-excel-perusahaan-dagang.xls]
        namafile_enkripsi = direktori + nama_enkripsi + fileAekstensi
        
        n = int(n)
        e = int(e)

        with open(filename, "rb") as rf:
            data_awal = rf.read()

        ## di ubah ke list
        data_awal = list(data_awal)

        ## ascii
        data_awal = [ord(i) for i in data_awal]

        ## padding add 5
        data_awal = [int(i + 1) for i in data_awal]

        # estimasi code : 13/Nov/2014
        # progress bar
        meter = EasyDialogs.ProgressBar('Enkripsi : ' + filename,
                                        maxval=len(data_awal),
                                        label='Starting',
                                        )

        ## proses enkripsi
        chiper = []
        for num,i in enumerate(data_awal):
            ch = int(gmpy2.digits(gmpy2.powmod(gmpy2.mpz(i),\
            gmpy2.mpz(e), gmpy2.mpz(n))))
            chiper.append(ch)
            msg = 'Data Chiper : %d' % ch
            meter.label(msg)
            meter.set(num)
            #time.sleep(0.1)
        '''
        chiper = [(int(gmpy2.digits(gmpy2.powmod(gmpy2.mpz(i),
        gmpy2.mpz(e), gmpy2.mpz(n))))) for i in data_awal]
        '''

        ## time akhir
        waktu_akhir = time.clock()  -  waktu_awal

        ## diubah ke string
        chiper = [str(i) for i in chiper]

        ## di join dengan pemisah spasi
        chiper = " ".join(chiper)

        ## simpan chiper
        with open(namafile_enkripsi,"wb") as enk:
            enk.write(chiper)

        ## return data
        ## index 0 : waktu akhir enkripsi
        ## index 1 : tempat penyimpanan hasil enkripsi
        obj.SetValue(str(waktu_akhir)[:6])
        notifikasi = "Berhasil Melakukan Enkripsi, silahkan cek : " + namafile_enkripsi
        notif = wx.MessageDialog(None, notifikasi, "Sukses", wx.OK)
        notif.ShowModal()
        
        # set Log aktivitas
        aktivitas = "ENKRIPSI"
        waktu = datetime.datetime.now().strftime("%y/%m/%d %H:%M")
        proses = str(waktu_akhir)[:5] + " Detik"
        list_datalog = [ aktivitas, user.replace("\n",""), waktu, 
                         proses, kunci.replace("\n",""), file.replace("\n","") ]
        file_datalog = 'virtualfile/data_log.log'
        hasil_datalog = DataLog.DataLog(file_datalog,list_datalog)
            
        if not hasil_datalog:
            pesan = "Pencatatan Log Gagal"
            notif = wx.MessageDialog(self,pesan, "Info",wx.ICON_WARNING)
            notif.ShowModal()
        # estimasi code : 13/Nov/2014
        # tidak mengembalikan nilai
        ##return [waktu_akhir, namafile_enkripsi]
    except:
        # estimasi code : 13/Nov/2014
        # menampilkan pesan kesalahan (pelemparan kesalahan)
        # jika terdapat kesalahan
        notifikasi = "Terjadi kesalahan saat melakukan enkripsi"
        notif = wx.MessageDialog(None, notifikasi, "Error", wx.ICON_ERROR)
        notif.ShowModal()


'''
## contoh enkripsi
enkripsi("D:/","D:/format-laporan-keuangan-bulanan.xls","3233","17")
'''


def dekripsi(direktori, filename, n, d, obj, kunci, user,file):
    '''
    untuk	: dekripsi file dengan kriptografi RSA
    param	: String direktorim String filename, int n, int d
    return	: Float waktu dekripsi, String file dekripsi
    '''
    ## set time awal
    waktu_awal = time.clock()

    direktori = str(direktori)  ## tempat penyimpana hasil enkripsi
    ##  D:/excel-perusahaan-dagang.xls
    filename = str(filename)
    fileAekstensi = Pendukung_Kripto.ambil_nama_file(filename)
    nama_dekripsi = "dekripsiRSA-"

    ##  D:/dekripRSA-excel-perusahaan-dagang.xls
    namafile_dekripsi = direktori + nama_dekripsi + fileAekstensi



    with open(filename, "rb") as rf:
        data_awal = rf.read()

    ## pemisahan split spasi
    data_awal = data_awal.split(" ")

    ## mengubah ke integer
    data_awal = [int(i) for i in data_awal]

    # estimasi code : 13/Nov/2014
    # progress bar

    meter = EasyDialogs.ProgressBar('Dekripsi : ' + filename,
                                        maxval=len(data_awal),
                                        label='Starting',
                                        )

    ## dekripsi data
    data_dek = []
    num = 0
    for i in data_awal:
        dt = int(gmpy2.digits(gmpy2.powmod(gmpy2.mpz(i), \
        gmpy2.mpz(d), gmpy2.mpz(n))))
        data_dek.append(int(gmpy2.digits(gmpy2.powmod(gmpy2.mpz(i), \
        gmpy2.mpz(d), gmpy2.mpz(n)))))
        msg = 'Data Dekripsi : %d' % dt
        meter.label(msg)
        num += 1
        meter.set(num)
    '''data_dek = [(int(gmpy2.digits(gmpy2.powmod(gmpy2.mpz(i), \
    gmpy2.mpz(d), gmpy2.mpz(n))))) for i in data_awal]'''


    ## time akhir
    waktu_akhir = time.clock()  -  waktu_awal

    ## padd -1 ke data_dek
    data_dek = [int(i - 1) for i in data_dek]

    ## to char
    data_dek = [chr(i) for i in data_dek]

    ## join
    data_dek = "".join(data_dek)

    ## simpan data
    with open(namafile_dekripsi,"wb") as w:
        w.write(data_dek)

    ## return data
    notifikasi = "Berhasil Melakukan Dekripsi, silahkan cek : " + namafile_dekripsi
    notif = wx.MessageDialog(None, notifikasi, "Sukses", wx.OK)
    notif.ShowModal()
    obj.SetValue(str(waktu_akhir)[:6])
    ##return [str(waktu_akhir), namafile_dekripsi]
    
    # set Log aktivitas
    aktivitas = "DEKRIPSI"
    waktu = datetime.datetime.now().strftime("%y/%m/%d %H:%M")
    proses = str(waktu_akhir)[:5] + " Detik"
    list_datalog = [ aktivitas, user.replace("\n",""), waktu, 
                     proses, kunci.replace("\n",""), file.replace("\n","") ]
    file_datalog = 'virtualfile/data_log.log'
    hasil_datalog = DataLog.DataLog(file_datalog,list_datalog)
        
    if not hasil_datalog:
        pesan = "Pencatatan Log Gagal"
        notif = wx.MessageDialog(self,pesan, "Info",wx.ICON_WARNING)
        notif.ShowModal()

'''
## contoh dekrip
dekripsi('D:/','D:/enkripRSA-format-laporan-keuangan-bulanan.xls',"3233","2753")
'''





