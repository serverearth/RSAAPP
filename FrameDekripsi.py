#Boa:Frame:FrameDekripsi

import wx
import wx.lib.buttons
import codevil
import thread

def create(parent):
    return FrameDekripsi(parent)

[wxID_FRAMEDEKRIPSI, wxID_FRAMEDEKRIPSIBTN_BERSIH, 
 wxID_FRAMEDEKRIPSIBTN_BROWSE_DIR_FILE, 
 wxID_FRAMEDEKRIPSIBTN_BROWSE_FILE_DEKRIPSI, 
 wxID_FRAMEDEKRIPSIBTN_BROWSE_KUNCI_RAHASIA, wxID_FRAMEDEKRIPSIBTN_DEKRIPSI, 
 wxID_FRAMEDEKRIPSIPANEL1, wxID_FRAMEDEKRIPSISTATICTEXT1, 
 wxID_FRAMEDEKRIPSISTATICTEXT2, wxID_FRAMEDEKRIPSISTATICTEXT3, 
 wxID_FRAMEDEKRIPSISTATICTEXT4, wxID_FRAMEDEKRIPSISTATICTEXT5, 
 wxID_FRAMEDEKRIPSISTATICTEXT6, wxID_FRAMEDEKRIPSITXT_D, 
 wxID_FRAMEDEKRIPSITXT_DIR_FILE_DEKRIPSI, wxID_FRAMEDEKRIPSITXT_FILE_DEKRIPSI, 
 wxID_FRAMEDEKRIPSITXT_N, wxID_FRAMEDEKRIPSITXT_WAKTU, 
] = [wx.NewId() for _init_ctrls in range(18)]

class FrameDekripsi(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEDEKRIPSI, name=u'FrameDekripsi',
              parent=prnt, pos=wx.Point(455, 286), size=wx.Size(380, 250),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Dekripsi - RSA')
        self.SetClientSize(wx.Size(364, 211))
        self.SetIcon(wx.Icon(u'img/icon.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAMEDEKRIPSIPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(364, 211),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAMEDEKRIPSISTATICTEXT1,
              label=u'File yang akan di Dekripsi :', name='staticText1',
              parent=self.panel1, pos=wx.Point(8, 8), size=wx.Size(128, 13),
              style=0)

        self.txt_file_dekripsi = wx.TextCtrl(id=wxID_FRAMEDEKRIPSITXT_FILE_DEKRIPSI,
              name=u'txt_file_dekripsi', parent=self.panel1, pos=wx.Point(8,
              24), size=wx.Size(264, 21), style=0, value=u'')

        self.staticText2 = wx.StaticText(id=wxID_FRAMEDEKRIPSISTATICTEXT2,
              label=u'Direktori Penyimpanan File Dekripsi : ',
              name='staticText2', parent=self.panel1, pos=wx.Point(8, 56),
              size=wx.Size(177, 13), style=0)

        self.txt_dir_file_dekripsi = wx.TextCtrl(id=wxID_FRAMEDEKRIPSITXT_DIR_FILE_DEKRIPSI,
              name=u'txt_dir_file_dekripsi', parent=self.panel1, pos=wx.Point(8,
              72), size=wx.Size(264, 21), style=0, value=u'')

        self.staticText3 = wx.StaticText(id=wxID_FRAMEDEKRIPSISTATICTEXT3,
              label=u'File Kunci Rahasia : ', name='staticText3',
              parent=self.panel1, pos=wx.Point(8, 104), size=wx.Size(96, 13),
              style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAMEDEKRIPSISTATICTEXT4,
              label=u'Modulo N : ', name='staticText4', parent=self.panel1,
              pos=wx.Point(8, 128), size=wx.Size(55, 13), style=0)

        self.txt_n = wx.TextCtrl(id=wxID_FRAMEDEKRIPSITXT_N, name=u'txt_n',
              parent=self.panel1, pos=wx.Point(64, 128), size=wx.Size(80, 21),
              style=0, value=u'')

        self.staticText5 = wx.StaticText(id=wxID_FRAMEDEKRIPSISTATICTEXT5,
              label=u'Eksponen D : ', name='staticText5', parent=self.panel1,
              pos=wx.Point(152, 128), size=wx.Size(67, 13), style=0)

        self.txt_d = wx.TextCtrl(id=wxID_FRAMEDEKRIPSITXT_D, name=u'txt_d',
              parent=self.panel1, pos=wx.Point(224, 128), size=wx.Size(64, 21),
              style=0, value=u'')

        self.staticText6 = wx.StaticText(id=wxID_FRAMEDEKRIPSISTATICTEXT6,
              label=u'Waktu Yang Dibutuhkan :', name='staticText6',
              parent=self.panel1, pos=wx.Point(8, 160), size=wx.Size(123, 13),
              style=0)

        self.txt_waktu = wx.TextCtrl(id=wxID_FRAMEDEKRIPSITXT_WAKTU,
              name=u'txt_waktu', parent=self.panel1, pos=wx.Point(8, 176),
              size=wx.Size(160, 21), style=0, value=u'')

        self.btn_browse_file_dekripsi = wx.lib.buttons.GenButton(id=wxID_FRAMEDEKRIPSIBTN_BROWSE_FILE_DEKRIPSI,
              label=u'....', name=u'btn_browse_file_dekripsi',
              parent=self.panel1, pos=wx.Point(288, 24), size=wx.Size(64, 25),
              style=0)
        self.btn_browse_file_dekripsi.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_file_dekripsiButton,
              id=wxID_FRAMEDEKRIPSIBTN_BROWSE_FILE_DEKRIPSI)

        self.btn_browse_dir_file = wx.lib.buttons.GenButton(id=wxID_FRAMEDEKRIPSIBTN_BROWSE_DIR_FILE,
              label=u'....', name=u'btn_browse_dir_file', parent=self.panel1,
              pos=wx.Point(288, 72), size=wx.Size(64, 25), style=0)
        self.btn_browse_dir_file.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_dir_fileButton,
              id=wxID_FRAMEDEKRIPSIBTN_BROWSE_DIR_FILE)

        self.btn_browse_kunci_rahasia = wx.lib.buttons.GenButton(id=wxID_FRAMEDEKRIPSIBTN_BROWSE_KUNCI_RAHASIA,
              label=u'....', name=u'btn_browse_kunci_rahasia',
              parent=self.panel1, pos=wx.Point(312, 128), size=wx.Size(40, 25),
              style=0)
        self.btn_browse_kunci_rahasia.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_kunci_rahasiaButton,
              id=wxID_FRAMEDEKRIPSIBTN_BROWSE_KUNCI_RAHASIA)

        self.btn_dekripsi = wx.Button(id=wxID_FRAMEDEKRIPSIBTN_DEKRIPSI,
              label=u'Dekripsi', name=u'btn_dekripsi', parent=self.panel1,
              pos=wx.Point(280, 176), size=wx.Size(75, 23), style=0)
        self.btn_dekripsi.Bind(wx.EVT_BUTTON, self.OnBtn_dekripsiButton,
              id=wxID_FRAMEDEKRIPSIBTN_DEKRIPSI)

        self.btn_bersih = wx.Button(id=wxID_FRAMEDEKRIPSIBTN_BERSIH,
              label=u'Bersih', name=u'btn_bersih', parent=self.panel1,
              pos=wx.Point(192, 176), size=wx.Size(75, 23), style=0)
        self.btn_bersih.Bind(wx.EVT_BUTTON, self.OnBtn_bersihButton,
              id=wxID_FRAMEDEKRIPSIBTN_BERSIH)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def __bersih(self):
        self.txt_d.SetValue("")
        self.txt_dir_file_dekripsi.SetValue("")
        self.txt_n.SetValue("")
        self.txt_waktu.SetValue("")
        self.txt_file_dekripsi.SetValue("")

    def __del_obj(self,obj):
        del obj


    def OnBtn_browse_file_dekripsiButton(self, event):
        """Event mengambil file yang akan didekripsi"""
        # estimasi program : 13/Nov/2014
        # mencari file yang akan di dekripsi
        # dengan fungsi ambil_file()
        # pada package codevil, lalu menyimpannya
        # ke dalam variabel file_dekrip
        # setelah itu menampilkannya ke self.txt_file_dekripsi
        file_dekrip = codevil.ambil_file(['doc','xls']) ## penyaringan ['doc','xls']
        self.txt_file_dekripsi.SetValue(file_dekrip)

    def OnBtn_browse_dir_fileButton(self, event):
        """Event untuk mengambil direktori tampat dimana file enkripsi"""
        # estimasi program : 13/Nov/2014
        # mencari direktori tempat penyimpanan
        # file hasil dekripsi. 
        # menggunakan method ambil_dir()
        # yang ada pada package codevil.
        # nilainya di tampilkan di self.txt_dir_file_dekripsi
        # dir_dekrip = codevil.ambil_dir()
        # self.txt_dir_file_dekripsi.SetValue(dir_dekrip)
        dialog = wx.DirDialog(None, 'Choose a directory',
            style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            direktori = dialog.GetPath()
            if len(direktori) <= 3:
                self.txt_dir_file_dekripsi.SetValue(str(direktori))
            else:
                self.txt_dir_file_dekripsi.SetValue(str(direktori)+'\\')
        dialog.Destroy()

    def OnBtn_browse_kunci_rahasiaButton(self, event):
        '''tombol untuk mengambil
        file kunci rahasia'''
        # estimasi program : 13/Nov/2014
        # membaca kunci rahasia RSA.
        # dengan fungsi baca_kunci_rsa
        # dimana nilainya akan di simpan ke dalam
        # variabel file_kunci.
        # sebagai catatan, fungsi ini
        # sudah di set penyaringan hanya file
        # berekstensi .key saja yang bisa di buka.
        # nilai n akan di tampilkan di txt_n
        # nilai d akan di tampilkan di txt_d
        file_kunci = codevil.baca_kunci_rsa()
        keys = file_kunci
        if file_kunci != False:
            try:
                self.user_enk = file_kunci[0].split("@")[0]
                self.kunci = keys[0] + ".key"
                self.txt_n.SetValue(keys[1])
                self.txt_d.SetValue(keys[2])
            except:
                # estimasi program : 13/Nov/2014
                # menampilkan notifikasi pesan kunci tak valid
                pesan = "Kunci Rahasia Tidak Valid"
                notif = wx.MessageDialog(self, pesan, "Peringatan", wx.ICON_ERROR)
                notif.ShowModal()
                self.txt_n.SetValue("")
                self.txt_d.SetValue("")
        else:
            # estimasi program : 13/Nov/2014
            # menampilkan notifikasi pesan kunci tak valid
            pesan = "Kunci Rahasia Tidak Valid"
            notif = wx.MessageDialog(self, pesan, "Peringatan", wx.ICON_ERROR)
            notif.ShowModal()
            self.txt_n.SetValue("")
            self.txt_d.SetValue("")



    def OnBtn_dekripsiButton(self, event):
        '''tombol untuk melakukan dekripsi'''
        # estimasi program : 13/Nov/2014
        # pengecekan elemen yang kosong
        # sebelum proses dekripsi dimulai
        if self.txt_file_dekripsi.GetValue() != "" and \
        self.txt_dir_file_dekripsi.GetValue() != "" and \
        self.txt_d.GetValue() != "" and \
        self.txt_n.GetValue() != "":
            # estimasi program : 13/Nov/2014
            # menggunakan Threading
            # untuk program agar tidak terjadi 
            # error (not respon) saat melakukan
            # proses dekripsi, karena 
            # proses dekripsi pada RSA memakan
            # banyak memori.
            # proses pertama secara manual
            # adalah menyimpan nilai 
            # url file yang akan di dekripsi ke 
            # variabel file_dek.
            # menyimpan nilai path direktori
            # tempat penyimpanan file hasil dekripsi
            # ke variabel dir_dek
            # menyimpan nilai modulo n dan eksponen d
            # ke variabel n dan d
            ## url file
            file_dek = self.txt_file_dekripsi.GetValue()
            ## path dir simpan
            dir_dek = self.txt_dir_file_dekripsi.GetValue()
            ## modulo n
            n = self.txt_n.GetValue()
            ## eksponen d
            d = self.txt_d.GetValue()
            
            # catatan : perlu menambahkan objek
            # self.txt_waktu ke parameter, untuk
            # melakukan proses mendapatkan waktu hasil
            # dari pendekripsian dokumen, karena Thread tidak 
            # menangkap nilai kembali dari suatu fungsi atau method.
            ## set obj
            obj = self.txt_waktu
            
            kunci = self.kunci
            user = self.user_enk
            file = self.txt_file_dekripsi.GetValue()
            thread.start_new_thread(codevil.dekripsi, (dir_dek,file_dek,n,d,obj,kunci, user,file,))
            '''
            dekrips = ThreadPool(processes=1)
            asy = dekrips.apply_async(codevil.dekripsi,(dir_dek,file_dek,n,d,))
            ## return data
            ## index 0 : waktu akhir enkripsi
            ## index 1 : tempat penyimpanan hasil enkripsi
            return_val = asy.get()
            self.txt_waktu.SetValue(str(return_val[0])[:4] + " Second")
            codevil.alert_box("Dekripsi Berhasil, Check : " +return_val[1],"Notif")
            # estimasi program : 13/Nov/2014
            del dekrips
            '''
        else:
            notif1 = ""
            if self.txt_file_dekripsi.GetValue() == "":
                notif1 += "\nPilih file yang akan di dekrip"
            if self.txt_dir_file_dekripsi.GetValue() == "":
                notif1 += "\nPilih direktori tempat untuk menyimpan file yang akan di dekripsi"
            if self.txt_d.GetValue() == "":
                notif1 += "\nPilih kunci rahasia untuk mendapatkan nilai Eksponen D"
            if self.txt_n.GetValue() == "":
                notif1 += "\nPilih kunci rahasia untuk mendapatkan nilai Modulo N"
                # estimasi program : 13/Nov/2014
            codevil.alert_box(notif1,"Notifikasi")


    def OnBtn_bersihButton(self, event):
        '''tombol untuk membersihkan form txt'''

        ## membersihkan form
        self.__bersih()
        try:
            self.__del_obj(self.dekrip)
        except:
            print ""

