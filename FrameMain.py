#-----------------------------------------------------------------------------
# Name:        FrameMain.py
# Purpose:     RSA Cryptography Implementation Using Python, FrameMain (Layar Utama)
#
# Author:      Yanwar Solahudin (Zen Su)
#
# Created:     2014/11/07
# RCS-ID:      $Id: FrameMain.py $
# Copyright:   (c) zensu 2014
# Licence:     KKP - 2014/2015 - Universitas Budiluhur
#-----------------------------------------------------------------------------
#Boa:Frame:Frame1

import wx
import wx.lib.buttons
import FrameGenKey
import FrameEnkripsi
import FrameDekripsi
import FrameBantuan
import FrameAktivitas
import FrameKantor
import FrameHelp

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1LOGO_DEPAN, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(582, 186), size=wx.Size(518, 479),
              style=wx.TRANSPARENT_WINDOW | wx.DEFAULT_FRAME_STYLE | wx.CLOSE_BOX,
              title=u'Layar Utama - Kriptografi RSA')
        self.SetClientSize(wx.Size(502, 440))
        self.SetIcon(wx.Icon(u'img/icon.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(502, 440),
              style=wx.THICK_FRAME | wx.MINIMIZE_BOX | wx.CAPTION | wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.logo_depan = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_FRAME1LOGO_DEPAN, name='logo_depan', parent=self.panel1,
              pos=wx.Point(179, 76), size=wx.Size(144, 128), style=0)
        self.logo_depan.Center(wx.HORIZONTAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Dhe Fud', name='staticText1', parent=self.panel1,
              pos=wx.Point(173, 224), size=wx.Size(156, 57), style=0)
        self.staticText1.Center(wx.HORIZONTAL)
        self.staticText1.SetFont(wx.Font(36, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Edwardian Script ITC'))
        self.staticText1.SetForegroundColour(wx.Colour(221, 0, 0))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Dhe Fud Resto & Catering Cengkareng, Jakarta, Indonesia address\nJl. Duri Kosambi No. 53, Cengkareng, Jakarta\n',
              name='staticText2', parent=self.panel1, pos=wx.Point(92, 288),
              size=wx.Size(318, 39), style=wx.ALIGN_CENTRE)
        self.staticText2.Center(wx.HORIZONTAL)
        self.staticText2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))
        self.staticText2.SetForegroundColour(wx.Colour(153, 153, 153))

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        # Panggil menu utama
        self.__menu_utama()
        
        # Tampil gambar logo depan
        file_gambar = 'img/shield.png'
        img = wx.Image(file_gambar, wx.BITMAP_TYPE_ANY)
        self.logo_depan.SetBitmap(wx.BitmapFromImage(img))
   
    def __menu_utama(self):
        """Membuat menu utama"""
        menubar = wx.MenuBar()
        
        menu_rsa = wx.Menu()
        sub_menu_generate = menu_rsa.Append(wx.ID_ANY, 'Generate Kunci')
        sub_menu_enkripsi = menu_rsa.Append(wx.ID_ANY, 'Enkripsi')
        sub_menu_dekripsi = menu_rsa.Append(wx.ID_ANY, 'Dekripsi')
        menubar.Append(menu_rsa, 'RSA')
        
        menu_log_user = wx.Menu()
        sub_menu_log = menu_log_user.Append(wx.ID_ANY,'Log Aktivitas')
        sub_menu_user = menu_log_user.Append(wx.ID_ANY,'User')
        menubar.Append(menu_log_user, 'Log User')
        
        menu_bantuan = wx.Menu()
        sub_menu_bantuan = menu_bantuan.Append(wx.ID_ANY, 'Bantuan')
        sub_menu_tentang = menu_bantuan.Append(wx.ID_ANY, 'About')
        menu_bantuan.AppendSeparator()
        sub_menu_keluar = menu_bantuan.Append(wx.ID_ANY, 'Keluar')
        menubar.Append(menu_bantuan, 'Help')
        
        self.SetMenuBar(menubar)
        
        # Event menu untuk memanggil frame lain
        self.Bind(wx.EVT_MENU, self.__event_panggil_frame_genereate, sub_menu_generate)  # panggil frame generate
        self.Bind(wx.EVT_MENU, self.__event_panggil_frame_enkripsi, sub_menu_enkripsi)  # panggil frame enkripsi
        self.Bind(wx.EVT_MENU, self.__event_panggil_frame_dekripsi, sub_menu_dekripsi)  # panggil frame dekripsi
        self.Bind(wx.EVT_MENU, self.__event_panggil_frame_log, sub_menu_log)  # panggil frame log aktivitas
        self.Bind(wx.EVT_MENU, self.__event_panggil_frame_user, sub_menu_user)  # Panggil frame user 
        self.Bind(wx.EVT_MENU, self.__event_panggil_frame_bantuan, sub_menu_bantuan)  # Panggil frame bantuan
        self.Bind(wx.EVT_MENU, self.__event_panggil_frame_tentang, sub_menu_tentang)  # Panggil frame about
        self.Bind(wx.EVT_MENU, self.__event_keluar, sub_menu_keluar)  # Event keluar
        
    
    def __event_panggil_frame_genereate(self, e):
        """Event memanggil frame generate kunci."""
        call_form = FrameGenKey.create(None)
        call_form.Show()
        
    
    def __event_panggil_frame_enkripsi(self, e):
        """Event memanggil frame enkripsi."""
        call_form = FrameEnkripsi.create(None)
        call_form.Show()
    
    
    def __event_panggil_frame_dekripsi(self, e):
        """Event memanggil frame dekripsi."""
        call_form = FrameDekripsi.create(None)
        call_form.Show()
    
    
    def __event_panggil_frame_log(self, e):
        """Event memanggil frame log aktivitas."""
        call_form = FrameAktivitas.create(None)
        call_form.Show()
    
    
    def __event_panggil_frame_user(self, e):
        """Event memanggil frame user."""
        call_form = FrameKantor.create(None)
        call_form.Show()
    
    
    def __event_panggil_frame_bantuan(self, e):
        """Event memanggil frame bantuan."""
        call_form = FrameHelp.create(None)
        call_form.Show()
    
    
    def __event_panggil_frame_tentang(self, e):
        """Event memanggil frame tentang"""
        call_form = FrameBantuan.create(None)
        call_form.Show()
    
    
    def __event_keluar(self, e):
        """Event keluar dari aplikasi"""
        self.Destroy()
    
    
