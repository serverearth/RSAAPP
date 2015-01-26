#Boa:Frame:Frame1

import wx


file_id_pusat = 'virtualfile/kantor_pusat.conf'
file_id_cabang= 'virtualfile/kantor_cabang.conf'
def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTN_SIMPAN_ID_KUNCI_CABANG, 
 wxID_FRAME1BTN_SIMPAN_ID_KUNCI_PUSAT, wxID_FRAME1BTN_TAMBAH_ID_CABANG, 
 wxID_FRAME1BTN_TAMBAH_ID_PUSAT, wxID_FRAME1LB_ID_KUNCI_CABANG, 
 wxID_FRAME1LB_ID_KUNCI_PUSAT, wxID_FRAME1PANEL1, wxID_FRAME1STATICBOX1, 
 wxID_FRAME1STATICBOX2, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1TXT_ID_KUNCI_CABANG, 
 wxID_FRAME1TXT_ID_KUNCI_PUSAT, 
] = [wx.NewId() for _init_ctrls in range(15)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(742, 239), size=wx.Size(426, 309),
              style=wx.DEFAULT_FRAME_STYLE, title='Setting Kantor Pusat')
        self.SetClientSize(wx.Size(410, 270))
        self.SetIcon(wx.Icon(u'img/icon.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(410, 270),
              style=wx.TAB_TRAVERSAL)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Kantor Pusat ', name='staticBox1', parent=self.panel1,
              pos=wx.Point(16, 16), size=wx.Size(184, 216), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Identitas Kunci User Pusat :', name='staticText1',
              parent=self.panel1, pos=wx.Point(32, 40), size=wx.Size(134, 13),
              style=0)

        self.txt_id_kunci_pusat = wx.TextCtrl(id=wxID_FRAME1TXT_ID_KUNCI_PUSAT,
              name=u'txt_id_kunci_pusat', parent=self.panel1, pos=wx.Point(32,
              56), size=wx.Size(104, 21), style=0, value=u'')

        self.btn_tambah_id_pusat = wx.Button(id=wxID_FRAME1BTN_TAMBAH_ID_PUSAT,
              label=u'+', name=u'btn_tambah_id_pusat', parent=self.panel1,
              pos=wx.Point(144, 56), size=wx.Size(40, 23), style=0)
        self.btn_tambah_id_pusat.Bind(wx.EVT_BUTTON,
              self.OnBtn_tambah_id_pusatButton,
              id=wxID_FRAME1BTN_TAMBAH_ID_PUSAT)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Kantor Cabang : ', name='staticBox2', parent=self.panel1,
              pos=wx.Point(208, 16), size=wx.Size(184, 216), style=0)

        self.lb_id_kunci_cabang = wx.ListBox(choices=[],
              id=wxID_FRAME1LB_ID_KUNCI_CABANG, name=u'lb_id_kunci_cabang',
              parent=self.panel1, pos=wx.Point(224, 88), size=wx.Size(152, 104),
              style=0)
        self.lb_id_kunci_cabang.Bind(wx.EVT_LEFT_DCLICK,
              self.OnLb_id_kunci_cabangLeftDclick)

        self.txt_id_kunci_cabang = wx.TextCtrl(id=wxID_FRAME1TXT_ID_KUNCI_CABANG,
              name=u'txt_id_kunci_cabang', parent=self.panel1, pos=wx.Point(224,
              56), size=wx.Size(104, 21), style=0, value=u'')

        self.btn_tambah_id_cabang = wx.Button(id=wxID_FRAME1BTN_TAMBAH_ID_CABANG,
              label=u'+', name=u'btn_tambah_id_cabang', parent=self.panel1,
              pos=wx.Point(336, 56), size=wx.Size(40, 23), style=0)
        self.btn_tambah_id_cabang.Bind(wx.EVT_BUTTON,
              self.OnBtn_tambah_id_cabangButton,
              id=wxID_FRAME1BTN_TAMBAH_ID_CABANG)

        self.btn_simpan_id_kunci_cabang = wx.Button(id=wxID_FRAME1BTN_SIMPAN_ID_KUNCI_CABANG,
              label=u'Simpan', name=u'btn_simpan_id_kunci_cabang',
              parent=self.panel1, pos=wx.Point(224, 200), size=wx.Size(155, 23),
              style=0)
        self.btn_simpan_id_kunci_cabang.Bind(wx.EVT_BUTTON,
              self.OnBtn_simpan_id_kunci_cabangButton,
              id=wxID_FRAME1BTN_SIMPAN_ID_KUNCI_CABANG)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Identitas Kunci User Cabang : ', name='staticText4',
              parent=self.panel1, pos=wx.Point(224, 40), size=wx.Size(147, 13),
              style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'untuk menghapus id kunci, klik dua kali pada id item kunci yang ingin di hapus',
              name='staticText5', parent=self.panel1, pos=wx.Point(24, 240),
              size=wx.Size(367, 13), style=0)
        self.staticText5.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

        self.lb_id_kunci_pusat = wx.ListBox(choices=[],
              id=wxID_FRAME1LB_ID_KUNCI_PUSAT, name=u'lb_id_kunci_pusat',
              parent=self.panel1, pos=wx.Point(32, 88), size=wx.Size(152, 104),
              style=0)
        self.lb_id_kunci_pusat.Bind(wx.EVT_LEFT_DCLICK,
              self.OnLb_id_kunci_pusatLeftDclick)

        self.btn_simpan_id_kunci_pusat = wx.Button(id=wxID_FRAME1BTN_SIMPAN_ID_KUNCI_PUSAT,
              label=u'Simpan', name=u'btn_simpan_id_kunci_pusat',
              parent=self.panel1, pos=wx.Point(32, 200), size=wx.Size(155, 23),
              style=0)
        self.btn_simpan_id_kunci_pusat.Bind(wx.EVT_BUTTON,
              self.OnBtn_simpan_id_kunci_pusatButton,
              id=wxID_FRAME1BTN_SIMPAN_ID_KUNCI_PUSAT)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        # baca file id kunci pusat
        with open(file_id_pusat,"r") as r:
            data_id_pusat = r.read()
            
        # baca file id kunci cabang
        with open(file_id_cabang,"r") as c:
            data_id_cabang = c.read()
        
        msg = ""
        if data_id_pusat == "":
            msg += "Id Kunci Pusat Belum ada isinya, Anda perlu mengisinya.\n"
        
        if data_id_cabang == "":
            msg += "Id Kunci Cabang Belum ada isinya, Anda perlu mengisinya."
        
        if msg != "":
            pesan = wx.MessageDialog(self,msg,"Pesan",\
            wx.ICON_INFORMATION)
            pesan.ShowModal()
            #event.Skip()
        
        # lakukan pembacaan
        # dan masukan hasilnya 
        # kedalam listbox
            
        # listbox kantor pusat
        id_kunci_pusat = data_id_pusat.split("\n")
        for i in id_kunci_pusat:
            if len(i) <= 0:
                self.lb_id_kunci_pusat.Clear()
            else:
                self.lb_id_kunci_pusat.Append(i)
        
        # listbox kantor cabang
        id_kunci_cabang = data_id_cabang.split("\n")
        self.lb_id_kunci_cabang.Clear()
        for i in id_kunci_cabang:
            if len(i) <= 0:
                self.lb_id_kunci_cabang.Clear()
            else:
                self.lb_id_kunci_cabang.Append(i)
            

    def OnBtn_tambah_id_pusatButton(self, event):
        # cek isian self.txt_id_kunci_pusat
        if self.txt_id_kunci_pusat.GetValue() == "":
            pesan = wx.MessageDialog(self,"ID Pusat Belum di isi","Pesan",\
            wx.ICON_WARNING)
            pesan.ShowModal()
        else:
            # tambahkan nilai self.txt_id_kunci_pusat
            # ke list box pusat
            id_kunci = "idkp_"+self.txt_id_kunci_pusat.GetValue()
            self.lb_id_kunci_pusat.Append(id_kunci.replace(" ","_"))
            self.__bersih()
    
    def __bersih(self):
        self.txt_id_kunci_pusat.SetValue("")
        self.txt_id_kunci_pusat.SetFocus()
        
    def __bersih2(self):
        self.txt_id_kunci_cabang.SetValue("")
        self.txt_id_kunci_cabang.SetFocus()
        
    
    def OnBtn_simpan_id_kunci_pusatButton(self, event):
        # cek apakah list box id pusat kosong ?
        if len(self.lb_id_kunci_pusat.GetStrings()) == 0:
            pesan = wx.MessageDialog(self,"Anda belum menambahkan \
            id kunci pusat satupun","Pesan",\
            wx.ICON_WARNING)
            pesan.ShowModal()
        else:
            # jika list ada, maka proses penyimpanan berlanjut
            
            # proses pengambilan semua list
            data_list_id_kunci_pusat = self.lb_id_kunci_pusat.GetStrings()
            data_list_id_kunci_pusat = " ".join(data_list_id_kunci_pusat)
            data_list_id_kunci_pusat = data_list_id_kunci_pusat.replace(" ","\n")
            try:
                with open(file_id_pusat,"w") as f:
                    f.write(data_list_id_kunci_pusat)
                
                pesan = wx.MessageDialog(self,"Berhasil Mengupdate Data","Pesan",\
                wx.OK)
                pesan.ShowModal()
                self.__bersih()
            except:
                pesan = wx.MessageDialog(self,"Terjadi kesalahan pada \
                penulisan file id kunci pusat","Pesan",\
                wx.ICON_ERROR)
                pesan.ShowModal()

    def OnLb_id_kunci_pusatLeftDclick(self, event):
        ''' menghapus item
        dengan double clik'''
        index = self.lb_id_kunci_pusat.GetSelection()
        self.lb_id_kunci_pusat.Delete(index)
        self.__bersih()

    def OnBtn_tambah_id_cabangButton(self, event):
        '''tambah id kunci cabang'''
        # cek isi self.txt_id_kunci_cabang
        if self.txt_id_kunci_cabang.GetValue() == "":
            pesan = wx.MessageDialog(self,"ID Cabang Belum di isi","Pesan",\
            wx.ICON_WARNING)
            pesan.ShowModal()
        else:
            # tambahkan nilai self.txt_id_kunci_cabang
            # ke list box cabang
            id_kunci = "idkc_"+self.txt_id_kunci_cabang.GetValue()
            self.lb_id_kunci_cabang.Append(id_kunci.replace(" ","_"))
            self.__bersih2()

    def OnBtn_simpan_id_kunci_cabangButton(self, event):
        # cek apakah list box id cabang kosong ?
        if len(self.lb_id_kunci_cabang.GetStrings()) == 0:
            pesan = wx.MessageDialog(self,"Anda belum menambahkan \
            id kunci cabang satupun","Pesan",\
            wx.ICON_WARNING)
            pesan.ShowModal()
        else:
            # jika list ada, maka proses penyimpanan berlanjut
            
            # proses pengambilan semua list
            data_list_id_kunci_cabang = self.lb_id_kunci_cabang.GetStrings()
            data_list_id_kunci_cabang = " ".join(data_list_id_kunci_cabang)
            data_list_id_kunci_cabang = data_list_id_kunci_cabang.replace(" ","\n")
            try:
                with open(file_id_cabang,"w") as f:
                    f.write(data_list_id_kunci_cabang)
                
                pesan = wx.MessageDialog(self,"Berhasil Mengupdate Data","Pesan",\
                wx.OK)
                pesan.ShowModal()
                self.__bersih2()
            except:
                pesan = wx.MessageDialog(self,"Terjadi kesalahan pada \
                penulisan file id kunci cabang","Pesan",\
                wx.ICON_ERROR)
                pesan.ShowModal()

    def OnLb_id_kunci_cabangLeftDclick(self, event):
        ''' menghapus item
        dengan double clik'''
        index = self.lb_id_kunci_cabang.GetSelection()
        self.lb_id_kunci_cabang.Delete(index)
        self.__bersih2()

            
            
            
