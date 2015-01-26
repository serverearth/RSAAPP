#-----------------------------------------------------------------------------
# Name:        FrameGenKey.py
# Purpose:     Generate Keys RSA Crypto (for testing, key length is default 2)
#
# Author:      Yanwar Solahudin (Zen Su)
#
# Created:     2014/11/07
# RCS-ID:      $Id: FrameGenKey.py $
# Copyright:   (c) zensu 2014
# Licence:     KKP - 2014/2015 - Universitas Budiluhur
#-----------------------------------------------------------------------------
#Boa:Frame:FrameGenKey

import wx
import wx.lib.buttons
import codevil
import time
from multiprocessing.pool import ThreadPool
import datetime

file_id_pusat = 'virtualfile/kantor_pusat.conf'
file_datalog = 'virtualfile/data_log.log'
file_id_cabang= 'virtualfile/kantor_cabang.conf'

def create(parent):
    return FrameGenKey(parent)

[wxID_FRAMEGENKEY, wxID_FRAMEGENKEYBTN_BERSIH, wxID_FRAMEGENKEYBTN_BROWSE, 
 wxID_FRAMEGENKEYBTN_GENERATE, wxID_FRAMEGENKEYCMB_KANTOR_CABANG, 
 wxID_FRAMEGENKEYCMB_KANTOR_PUSAT, wxID_FRAMEGENKEYPANEL1, 
 wxID_FRAMEGENKEYSTATICTEXT1, wxID_FRAMEGENKEYSTATICTEXT2, 
 wxID_FRAMEGENKEYSTATICTEXT3, wxID_FRAMEGENKEYSTATICTEXT4, 
 wxID_FRAMEGENKEYSTATICTEXT5, wxID_FRAMEGENKEYSTATICTEXT6, 
 wxID_FRAMEGENKEYSTATICTEXT7, wxID_FRAMEGENKEYSTATICTEXT8, 
 wxID_FRAMEGENKEYSTATICTEXT9, wxID_FRAMEGENKEYTXT_DIR_SAVE_KUNCI, 
 wxID_FRAMEGENKEYTXT_GENKEY_D, wxID_FRAMEGENKEYTXT_GENKEY_E, 
 wxID_FRAMEGENKEYTXT_GENKEY_N, wxID_FRAMEGENKEYTXT_PUBLIK, 
 wxID_FRAMEGENKEYTXT_RAHASIA, wxID_FRAMEGENKEYTXT_WAKTU, 
] = [wx.NewId() for _init_ctrls in range(23)]

class FrameGenKey(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGENKEY, name=u'FrameGenKey',
              parent=prnt, pos=wx.Point(564, 236), size=wx.Size(386, 351),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Generate Kunci - RSA')
        self.SetClientSize(wx.Size(370, 312))
        self.SetIcon(wx.Icon(u'img/icon.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAMEGENKEYPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(370, 312),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAMEGENKEYSTATICTEXT1,
              label=u'Modulo N :', name='staticText1', parent=self.panel1,
              pos=wx.Point(16, 16), size=wx.Size(52, 13), style=0)

        self.txt_genkey_n = wx.TextCtrl(id=wxID_FRAMEGENKEYTXT_GENKEY_N,
              name=u'txt_genkey_n', parent=self.panel1, pos=wx.Point(16, 32),
              size=wx.Size(144, 21), style=0, value=u'')
        self.txt_genkey_n.SetEditable(False)

        self.staticText2 = wx.StaticText(id=wxID_FRAMEGENKEYSTATICTEXT2,
              label=u'Eksponen E :', name='staticText2', parent=self.panel1,
              pos=wx.Point(16, 64), size=wx.Size(63, 13), style=0)

        self.txt_genkey_e = wx.TextCtrl(id=wxID_FRAMEGENKEYTXT_GENKEY_E,
              name=u'txt_genkey_e', parent=self.panel1, pos=wx.Point(16, 80),
              size=wx.Size(144, 21), style=0, value=u'')
        self.txt_genkey_e.SetEditable(False)

        self.staticText3 = wx.StaticText(id=wxID_FRAMEGENKEYSTATICTEXT3,
              label=u'Eksponen D :', name='staticText3', parent=self.panel1,
              pos=wx.Point(16, 112), size=wx.Size(64, 13), style=0)

        self.txt_genkey_d = wx.TextCtrl(id=wxID_FRAMEGENKEYTXT_GENKEY_D,
              name=u'txt_genkey_d', parent=self.panel1, pos=wx.Point(16, 128),
              size=wx.Size(144, 21), style=0, value=u'')
        self.txt_genkey_d.SetEditable(False)

        self.staticText4 = wx.StaticText(id=wxID_FRAMEGENKEYSTATICTEXT4,
              label=u'Kunci Publik :', name='staticText4', parent=self.panel1,
              pos=wx.Point(208, 16), size=wx.Size(63, 13), style=0)

        self.txt_publik = wx.TextCtrl(id=wxID_FRAMEGENKEYTXT_PUBLIK,
              name=u'txt_publik', parent=self.panel1, pos=wx.Point(208, 32),
              size=wx.Size(144, 21), style=0, value=u'')
        self.txt_publik.SetEditable(False)

        self.staticText5 = wx.StaticText(id=wxID_FRAMEGENKEYSTATICTEXT5,
              label=u'Kunci Rahasia :', name='staticText5', parent=self.panel1,
              pos=wx.Point(208, 64), size=wx.Size(74, 13), style=0)

        self.txt_rahasia = wx.TextCtrl(id=wxID_FRAMEGENKEYTXT_RAHASIA,
              name=u'txt_rahasia', parent=self.panel1, pos=wx.Point(208, 80),
              size=wx.Size(144, 21), style=0, value=u'')
        self.txt_rahasia.SetEditable(False)

        self.staticText6 = wx.StaticText(id=wxID_FRAMEGENKEYSTATICTEXT6,
              label=u'Waktu Generate :', name='staticText6', parent=self.panel1,
              pos=wx.Point(208, 112), size=wx.Size(87, 13), style=0)

        self.txt_waktu = wx.TextCtrl(id=wxID_FRAMEGENKEYTXT_WAKTU,
              name=u'txt_waktu', parent=self.panel1, pos=wx.Point(208, 128),
              size=wx.Size(144, 21), style=0, value=u'')
        self.txt_waktu.SetEditable(False)

        self.staticText7 = wx.StaticText(id=wxID_FRAMEGENKEYSTATICTEXT7,
              label=u'Set direktori penyimpanan kunci :', name='staticText7',
              parent=self.panel1, pos=wx.Point(16, 160), size=wx.Size(160, 13),
              style=0)

        self.txt_dir_save_kunci = wx.TextCtrl(id=wxID_FRAMEGENKEYTXT_DIR_SAVE_KUNCI,
              name=u'txt_dir_save_kunci', parent=self.panel1, pos=wx.Point(16,
              176), size=wx.Size(256, 21), style=0, value=u'')
        self.txt_dir_save_kunci.SetEditable(False)

        self.btn_browse = wx.lib.buttons.GenButton(id=wxID_FRAMEGENKEYBTN_BROWSE,
              label=u'....', name=u'btn_browse', parent=self.panel1,
              pos=wx.Point(288, 176), size=wx.Size(64, 24), style=0)
        self.btn_browse.Bind(wx.EVT_BUTTON, self.OnBtn_browseButton,
              id=wxID_FRAMEGENKEYBTN_BROWSE)

        self.btn_generate = wx.Button(id=wxID_FRAMEGENKEYBTN_GENERATE,
              label=u'Generate', name=u'btn_generate', parent=self.panel1,
              pos=wx.Point(280, 272), size=wx.Size(75, 24), style=0)
        self.btn_generate.Bind(wx.EVT_BUTTON, self.OnBtn_generateButton,
              id=wxID_FRAMEGENKEYBTN_GENERATE)

        self.btn_bersih = wx.Button(id=wxID_FRAMEGENKEYBTN_BERSIH,
              label=u'Bersih', name=u'btn_bersih', parent=self.panel1,
              pos=wx.Point(192, 272), size=wx.Size(75, 24), style=0)
        self.btn_bersih.Bind(wx.EVT_BUTTON, self.OnBtn_bersihButton,
              id=wxID_FRAMEGENKEYBTN_BERSIH)

        self.staticText8 = wx.StaticText(id=wxID_FRAMEGENKEYSTATICTEXT8,
              label=u'Kantor Cabang :', name='staticText8', parent=self.panel1,
              pos=wx.Point(16, 216), size=wx.Size(80, 13), style=0)

        self.cmb_kantor_cabang = wx.ComboBox(choices=[],
              id=wxID_FRAMEGENKEYCMB_KANTOR_CABANG, name=u'cmb_kantor_cabang',
              parent=self.panel1, pos=wx.Point(16, 232), size=wx.Size(160, 21),
              style=0, value=u'')
        self.cmb_kantor_cabang.SetLabel(u'')

        self.staticText9 = wx.StaticText(id=wxID_FRAMEGENKEYSTATICTEXT9,
              label=u'Kantor Pusat', name='staticText9', parent=self.panel1,
              pos=wx.Point(192, 216), size=wx.Size(63, 13), style=0)

        self.cmb_kantor_pusat = wx.ComboBox(choices=[],
              id=wxID_FRAMEGENKEYCMB_KANTOR_PUSAT, name=u'cmb_kantor_pusat',
              parent=self.panel1, pos=wx.Point(192, 232), size=wx.Size(160, 21),
              style=0, value=u'')
        self.cmb_kantor_pusat.SetLabel(u'')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.id_pusat = self.__readIdKey(file_id_pusat)
        self.id_cabang = self.__readIdKey(file_id_cabang)
        msg = ""
        if len(str(self.id_cabang)) <= 4:
            msg += "Anda Perlu mengisi sebuah Id Kunci untuk cabang\n"
        if len(str(self.id_pusat)) <= 4:
            msg += "Anda Perlu mengisi sebuah Id Kunci untuk pusat"
        
        if msg == "":
            self.cmb_kantor_pusat.SetValue(self.id_pusat[0])
            self.cmb_kantor_cabang.SetValue(self.id_cabang[0])
            for i in self.id_pusat:
                self.cmb_kantor_pusat.Append(i)
            
            for i in self.id_cabang:
                self.cmb_kantor_cabang.Append(i)
        else:
            pesan = wx.MessageDialog(self,msg,"PERINGATAN", wx.ICON_WARNING)
            pesan.ShowModal()
            self.Close()

    def __bersih(self):
        self.txt_dir_save_kunci.SetValue("")
        self.txt_genkey_d.SetValue("")
        self.txt_genkey_e.SetValue("")
        self.txt_genkey_n.SetValue("")
        self.txt_publik.SetValue("")
        self.txt_rahasia.SetValue("")
        self.txt_waktu.SetValue("")
        
    def OnBtn_browseButton(self, event):
        '''tombol untuk set direktori
        penyimpanan kunci publik dan rahasia'''
        #self.direktori_simpan_kunci = codevil.ambil_dir()
        #self.txt_dir_save_kunci.SetValue(self.direktori_simpan_kunci)
        dialog = wx.DirDialog(
            None, 'Choose a directory', 
            style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        direktori = ''
        if dialog.ShowModal() == wx.ID_OK:
            direktori = dialog.GetPath()
            if len(direktori) <= 3:
                pass
            else:
                direktori = direktori + '\\'
            self.direktori_simpan_kunci = str(direktori)
            self.txt_dir_save_kunci.SetValue(str(direktori))

    def OnBtn_generateButton(self, event):
        '''tombol generate untuk aksi
        generate kunci'''
        
        self.n = ""
        self.e = ""
        self.d = ""
        
        if self.txt_dir_save_kunci.GetValue() != "":
            #id = codevil.input_dialog("Input ID Kunci : ")
            id_kunci_pusat = self.cmb_kantor_pusat.GetValue()
            id_kunci_cabang = self.cmb_kantor_cabang.GetValue()
            id = id_kunci_pusat+"@"+id_kunci_cabang
            data = codevil.generate_kunci(id,self.direktori_simpan_kunci)
            self.n = str(data[3])
            self.e = str(data[5])
            self.d = str(data[6])
            self.txt_genkey_n.SetValue(self.n)
            self.txt_genkey_e.SetValue(self.e)
            self.txt_genkey_d.SetValue(self.d)
            self.txt_publik.SetValue(self.e)
            self.txt_rahasia.SetValue(self.d)
            self.txt_waktu.SetValue(str(data[7])[:2] + " Detik")
            
            # set data log
            aktivitas = "GENERATE_KEY"
            user = id_kunci_pusat
            waktu = datetime.datetime.now().strftime("%y/%m/%d %H:%M")
            proses = self.txt_waktu.GetValue()
            kunci = self.direktori_simpan_kunci + id_kunci_pusat+"@"+id_kunci_cabang+ "-private.key " + \
            id_kunci_pusat+"@"+id_kunci_cabang+ "-public.key"
            file = "None" 
            list_datalog = [ aktivitas, user, waktu, 
                             proses, kunci, file ]
            hasil_datalog = codevil.DataLog(file_datalog,list_datalog)
            
            if not hasil_datalog:
                pesan = "Pencatatan Log Gagal"
                notif = wx.MessageDialog(self,pesan, "Info",wx.ICON_WARNING)
                notif.ShowModal()
            
            # estimasi program : 13/nov/2014
            # menampilkan notifikasi
            # jika telah berhasil membuat dan 
            # menggenerate kunci RSA
            pesan = "Berhasil Membuat kunci, silahkan cek : " + self.direktori_simpan_kunci
            notif = wx.MessageDialog(self,pesan, "Info",wx.OK)
            notif.ShowModal()
            ##<## notif sukses>##
            ##<notif = """pembuatan kunci berhasil""">##
            ##<codevil.alert_box(notif,"Berhasil")>##
        else:
            # estimasi program : 13/nov/2014
            # menampilkan notifikasi
            # jika belum memilih kunci
            pesan = "Anda Belum Memilih Direktori untuk menyimpan kunci hasil generate"
            notif = wx.MessageDialog(self,pesan, "Peringatan",wx.ICON_ERROR)
            notif.ShowModal()
            ##<codevil.alert_box("Anda Belum Memilih Direktori","Kesalahan")>##
            
            
    def OnBtn_bersihButton(self, event):
        ## bersihkan form
        self.__bersih()
    
    def __readIdKey(self, filename):
        with open(filename, "r") as f:
            data = f.read()
            
        data = data.split("\n")
        return data
