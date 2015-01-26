#Boa:Frame:FrameEnkripsi

import wx
import wx.lib.buttons
from multiprocessing.pool import ThreadPool
import codevil
import thread
import datetime
import time

file_datalog = 'virtualfile/data_log.log'

def create(parent):
    return FrameEnkripsi(parent)

[wxID_FRAMEENKRIPSI, wxID_FRAMEENKRIPSIBTN_BERSIH, 
 wxID_FRAMEENKRIPSIBTN_BROWSE_DIR_SIMPAN_FILE, 
 wxID_FRAMEENKRIPSIBTN_BROWSE_FILE_ENKRIPSI, 
 wxID_FRAMEENKRIPSIBTN_BROWSE_KUNCI_PUBLIK, wxID_FRAMEENKRIPSIBTN_ENKRIPSI, 
 wxID_FRAMEENKRIPSIPANEL1, wxID_FRAMEENKRIPSISTATICTEXT1, 
 wxID_FRAMEENKRIPSISTATICTEXT2, wxID_FRAMEENKRIPSISTATICTEXT3, 
 wxID_FRAMEENKRIPSISTATICTEXT4, wxID_FRAMEENKRIPSISTATICTEXT5, 
 wxID_FRAMEENKRIPSISTATICTEXT6, wxID_FRAMEENKRIPSITXT_DIR_SIMPAN_FILE, 
 wxID_FRAMEENKRIPSITXT_E, wxID_FRAMEENKRIPSITXT_FILE_ENKRIPSI, 
 wxID_FRAMEENKRIPSITXT_N, wxID_FRAMEENKRIPSITXT_WAKTU, 
] = [wx.NewId() for _init_ctrls in range(18)]

class FrameEnkripsi(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEENKRIPSI, name=u'FrameEnkripsi',
              parent=prnt, pos=wx.Point(392, 74), size=wx.Size(381, 253),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Enkripsi - RSA')
        self.SetClientSize(wx.Size(365, 215))

        self.panel1 = wx.Panel(id=wxID_FRAMEENKRIPSIPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(365, 215),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAMEENKRIPSISTATICTEXT1,
              label=u'File yang akan di Enkripsi :', name='staticText1',
              parent=self.panel1, pos=wx.Point(8, 8), size=wx.Size(127, 13),
              style=0)

        self.txt_file_enkripsi = wx.TextCtrl(id=wxID_FRAMEENKRIPSITXT_FILE_ENKRIPSI,
              name=u'txt_file_enkripsi', parent=self.panel1, pos=wx.Point(8,
              24), size=wx.Size(264, 21), style=0, value=u'')
        self.txt_file_enkripsi.SetEditable(False)

        self.btn_browse_file_enkripsi = wx.lib.buttons.GenButton(id=wxID_FRAMEENKRIPSIBTN_BROWSE_FILE_ENKRIPSI,
              label=u'....', name=u'btn_browse_file_enkripsi',
              parent=self.panel1, pos=wx.Point(288, 24), size=wx.Size(64, 25),
              style=0)
        self.btn_browse_file_enkripsi.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_file_enkripsiButton,
              id=wxID_FRAMEENKRIPSIBTN_BROWSE_FILE_ENKRIPSI)

        self.staticText2 = wx.StaticText(id=wxID_FRAMEENKRIPSISTATICTEXT2,
              label=u'Direktori Penyimpanan File Enkripsi :',
              name='staticText2', parent=self.panel1, pos=wx.Point(8, 56),
              size=wx.Size(173, 13), style=0)

        self.txt_dir_simpan_file = wx.TextCtrl(id=wxID_FRAMEENKRIPSITXT_DIR_SIMPAN_FILE,
              name=u'txt_dir_simpan_file', parent=self.panel1, pos=wx.Point(8,
              72), size=wx.Size(264, 21), style=0, value=u'')
        self.txt_dir_simpan_file.SetEditable(False)

        self.btn_browse_dir_simpan_file = wx.lib.buttons.GenButton(id=wxID_FRAMEENKRIPSIBTN_BROWSE_DIR_SIMPAN_FILE,
              label=u'....', name=u'btn_browse_dir_simpan_file',
              parent=self.panel1, pos=wx.Point(288, 72), size=wx.Size(64, 25),
              style=0)
        self.btn_browse_dir_simpan_file.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_dir_simpan_fileButton,
              id=wxID_FRAMEENKRIPSIBTN_BROWSE_DIR_SIMPAN_FILE)

        self.staticText3 = wx.StaticText(id=wxID_FRAMEENKRIPSISTATICTEXT3,
              label=u'File Kunci Publik :', name='staticText3',
              parent=self.panel1, pos=wx.Point(8, 104), size=wx.Size(82, 13),
              style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAMEENKRIPSISTATICTEXT4,
              label=u'Modulo N :', name='staticText4', parent=self.panel1,
              pos=wx.Point(8, 128), size=wx.Size(52, 13), style=0)

        self.txt_n = wx.TextCtrl(id=wxID_FRAMEENKRIPSITXT_N, name=u'txt_n',
              parent=self.panel1, pos=wx.Point(64, 128), size=wx.Size(80, 21),
              style=0, value=u'')
        self.txt_n.SetEditable(False)

        self.staticText5 = wx.StaticText(id=wxID_FRAMEENKRIPSISTATICTEXT5,
              label=u'Eksponen E :', name='staticText5', parent=self.panel1,
              pos=wx.Point(152, 128), size=wx.Size(63, 13), style=0)

        self.txt_e = wx.TextCtrl(id=wxID_FRAMEENKRIPSITXT_E, name=u'txt_e',
              parent=self.panel1, pos=wx.Point(224, 128), size=wx.Size(64, 21),
              style=0, value=u'')
        self.txt_e.SetEditable(False)

        self.btn_browse_kunci_publik = wx.lib.buttons.GenButton(id=wxID_FRAMEENKRIPSIBTN_BROWSE_KUNCI_PUBLIK,
              label=u'....', name=u'btn_browse_kunci_publik',
              parent=self.panel1, pos=wx.Point(312, 128), size=wx.Size(40, 25),
              style=0)
        self.btn_browse_kunci_publik.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_kunci_publikButton,
              id=wxID_FRAMEENKRIPSIBTN_BROWSE_KUNCI_PUBLIK)

        self.staticText6 = wx.StaticText(id=wxID_FRAMEENKRIPSISTATICTEXT6,
              label=u'Waktu Yang Dibutuhkan : ', name='staticText6',
              parent=self.panel1, pos=wx.Point(8, 160), size=wx.Size(126, 13),
              style=0)

        self.txt_waktu = wx.TextCtrl(id=wxID_FRAMEENKRIPSITXT_WAKTU,
              name=u'txt_waktu', parent=self.panel1, pos=wx.Point(8, 176),
              size=wx.Size(160, 21), style=0, value=u'')
        self.txt_waktu.SetEditable(False)

        self.btn_enkripsi = wx.Button(id=wxID_FRAMEENKRIPSIBTN_ENKRIPSI,
              label=u'Enkripsi', name=u'btn_enkripsi', parent=self.panel1,
              pos=wx.Point(280, 176), size=wx.Size(75, 23), style=0)
        self.btn_enkripsi.Bind(wx.EVT_BUTTON, self.OnBtn_enkripsiButton,
              id=wxID_FRAMEENKRIPSIBTN_ENKRIPSI)

        self.btn_bersih = wx.Button(id=wxID_FRAMEENKRIPSIBTN_BERSIH,
              label=u'Bersih', name=u'btn_bersih', parent=self.panel1,
              pos=wx.Point(192, 176), size=wx.Size(75, 23), style=0)
        self.btn_bersih.Bind(wx.EVT_BUTTON, self.OnBtn_bersihButton,
              id=wxID_FRAMEENKRIPSIBTN_BERSIH)

    def __init__(self, parent):
        self._init_ctrls(parent)


    def __bersih(self):
        self.txt_dir_simpan_file.SetValue("")
        self.txt_e.SetValue("")
        self.txt_file_enkripsi.SetValue("")
        self.txt_n.SetValue("")
        self.txt_waktu.SetValue("")

    def del_objek_enkripsi(self,obj_enkrip):
        del obj_enkrip

    def OnBtn_browse_file_enkripsiButton(self, event):
        """Event mengambil file yang akan dienkripsi"""
        # estimasi program : 13/Nov/2014
        # mencari file yang akan di enkripsi
        # memfilter dengan list_allow_file
        # yang artinya hanya boleh file bertipe tertentu
        # yang bisa di enkripsi. setelah itu
        # menampilkan filenamenya di self.txt_file_enkripsi
        list_allow_file = ['xls','doc']
        file_enkripsi = codevil.ambil_file(list_allow_file)
        self.txt_file_enkripsi.SetValue(file_enkripsi)
        
        # estimasi program : 13/Nov/2014
        # mendapatkan ukuran file dengan fungsi get_file_size()
        # dari package codevil. nilainya di set ke variabel ukuran_file
        ukuran_file = codevil.get_file_size(self.txt_file_enkripsi.GetValue())
        if ukuran_file > 3:
            # estimasi program : 13/Nov/2014
            # menampilkan notifikasi jika ukuran file
            # melebihi kapasitas yang telah ditentukan (3mb)
            pesan = "Ukuran file sebesar " + str(ukuran_file) + " Mb Tidak di izinkan"
            notif = wx.MessageDialog(self, pesan, "Peringatan", wx.ICON_ERROR)
            notif.ShowModal()
            ## bersihkan
            self.__bersih()


    def OnBtn_browse_dir_simpan_fileButton(self, event):
        """Event untuk mengambil direktori tampat dimana file enkripsi"""
        dialog = wx.DirDialog(
            None, 'Choose a directory',
            style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            # ambil path
            direktori = dialog.GetPath()
            # untuk direktori D:\ C:\ (single direktori)
            if len(direktori) <= 3:
                self.txt_dir_simpan_file.SetValue(str(direktori))
            else:
                direktori = direktori + "\\"
                self.txt_dir_simpan_file.SetValue(str(direktori))
        dialog.Destroy()

    def OnBtn_browse_kunci_publikButton(self, event):
        """Event untuk mendapatkan file kunci"""
        self.kunci = codevil.baca_kunci_rsa()
        keys = self.kunci
        # cek validasi kunci
        if self.kunci:
            try:
                self.user_enk = self.kunci[0].split("@")[1]
                self.kunci = self.kunci[0] + ".key"
                self.txt_n.SetValue(keys[1])
                self.txt_e.SetValue(keys[2])
            except:
                # estimasi program : 13/Nov/2014
                # menampilkan notifikasi ketidak valid-an kunci
                # publik RSA.
                pesan = "Kunci Publik Tidak Valid"
                notif = wx.MessageDialog(self, pesan, "Peringatan", wx.ICON_ERROR)
                notif.ShowModal()
                self.txt_e.SetValue("")
                self.txt_n.SetValue("")
        else:
            pesan = "Kunci Publik Tidak Valid"
            notif = wx.MessageDialog(self, pesan, "Peringatan", wx.ICON_ERROR)
            notif.ShowModal()

    def OnBtn_enkripsiButton(self, event):
        """Event untuk melakukan enkripsi"""
        # Cek 
        if self.txt_n.GetValue() != "" and \
        self.txt_e.GetValue() != "" and \
        self.txt_dir_simpan_file.GetValue() != "" and \
        self.txt_file_enkripsi.GetValue() != "":
            n = self.txt_n.GetValue().replace(" ","")
            e = self.txt_e.GetValue().replace(" ","")
            ##<codevil.enkripsi(self.txt_dir_simpan_file.GetValue(),\>##
            ##<self.txt_file_enkripsi.GetValue(), n, e)>##
            
            # estimasi program : 13/Nov/2014
            # menggunakan Threading saat enkripsi
            # untuk menghindari terjadinya not responding
            # karena melakukan proses pembacaan dan proses lainnya
            # yang memakan banyak memori komputer
            # nilai direktori penyimpanan hasil enkripsi akan
            # di simpan ke dalam variabel dir_enk,
            # nilai file yang akan di enkripsi akan di simpan
            # kedalam variabel file_enk, nilai modulo n 
            # akan di simpan ke dalam variabel n dan 
            # nilai eksponen e akan di simpan ke dalam e
            # nilai objek self.txt_waktu akan di kirim
            # sebagai objek reference untuk di proses 
            # di dalam method enkripsi pada package codevil
            # karena thread tidak bisa menangkap nilai kembali
            # dari sebuah method atau fungsi.
            dir_enk = self.txt_dir_simpan_file.GetValue()
            file_enk = self.txt_file_enkripsi.GetValue()
            obj_txt_waktu = self.txt_waktu
            kunci = self.kunci
            user = self.user_enk
            file = self.txt_file_enkripsi.GetValue()
            thread.start_new_thread(codevil.enkripsi, (dir_enk, file_enk, n, e,obj_txt_waktu, kunci, user, file,))
            
            
            ##<enkrip = ThreadPool(processes=1)>##
            ##<async = enkrip.apply_async(codevil.enkripsi,>## 
            ##<(self.txt_dir_simpan_file.GetValue(),\>##
            ##<self.txt_file_enkripsi.GetValue(), n, e))>##
            ##<return_data = async.get()>##
            
        else:
            notif1 = ""
            if self.txt_n.GetValue() == "":
                notif1 += "\nPilih Kunci Publik untuk mendapatkan nilai modulo N"
            if self.txt_e.GetValue() == "":
                notif1 += "\nPilih Kunci Publik untuk mendapatkan nilan Eksponen E"
            if self.txt_dir_simpan_file.GetValue() == "":
                notif1 += "\nPilih direktori untuk menyimpan file hasil enkripsi"
            if self.txt_file_enkripsi.GetValue() == "":
                notif1 += "\nPilih File yang akan di enkripsi"
            # estimasi program : 13/Nov/2014
            # program akan menampilkan notifikasi
            # saat beberapa elemen tidak di isi
            notif = wx.MessageDialog(self, notif1, "Peringatan", wx.ICON_ERROR)
            notif.ShowModal()



    def OnBtn_bersihButton(self, event):
        ## bersih form
        ## hapus objek enkripsi
        self.__bersih()












