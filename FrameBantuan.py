#Boa:Frame:FrameBantuan

import wx
import wx.richtext

import FrameHelp

def create(parent):
    return FrameBantuan(parent)

[wxID_FRAMEBANTUAN, wxID_FRAMEBANTUANBTN_BANTUAN, wxID_FRAMEBANTUANLOGO, 
 wxID_FRAMEBANTUANPANEL1, wxID_FRAMEBANTUANSTATICTEXT1, 
 wxID_FRAMEBANTUANSTATICTEXT2, wxID_FRAMEBANTUANSTATICTEXT3, 
 wxID_FRAMEBANTUANSTATICTEXT4, 
] = [wx.NewId() for _init_ctrls in range(8)]

class FrameBantuan(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEBANTUAN, name=u'FrameBantuan',
              parent=prnt, pos=wx.Point(593, 242), size=wx.Size(311, 215),
              style=wx.DEFAULT_FRAME_STYLE, title='Tentang Aplikasi')
        self.SetClientSize(wx.Size(295, 176))
        self.SetIcon(wx.Icon(u'img/icon.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAMEBANTUANPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(295, 176),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.logo = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_FRAMEBANTUANLOGO, name='logo', parent=self.panel1,
              pos=wx.Point(40, 24), size=wx.Size(48, 48), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAMEBANTUANSTATICTEXT1,
              label='Aplikasi RSA', name='staticText1', parent=self.panel1,
              pos=wx.Point(96, 24), size=wx.Size(120, 23), style=0)
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))
        self.staticText1.SetForegroundColour(wx.Colour(44, 157, 177))

        self.staticText2 = wx.StaticText(id=wxID_FRAMEBANTUANSTATICTEXT2,
              label='Kuliah Kerja Praktik', name='staticText2',
              parent=self.panel1, pos=wx.Point(96, 48), size=wx.Size(128, 13),
              style=0)
        self.staticText2.SetForegroundColour(wx.Colour(117, 117, 117))

        self.staticText3 = wx.StaticText(id=wxID_FRAMEBANTUANSTATICTEXT3,
              label='Copyright @ 2014, 2015 Nahar, Yanwar, Ridwan',
              name='staticText3', parent=self.panel1, pos=wx.Point(29, 88),
              size=wx.Size(236, 13), style=0)
        self.staticText3.Center(wx.HORIZONTAL)

        self.staticText4 = wx.StaticText(id=wxID_FRAMEBANTUANSTATICTEXT4,
              label='Universitas Budiluhur - Fakultas Teknologi Informasi',
              name='staticText4', parent=self.panel1, pos=wx.Point(24, 104),
              size=wx.Size(247, 13), style=0)
        self.staticText4.SetForegroundColour(wx.Colour(40, 160, 200))
        self.staticText4.Center(wx.HORIZONTAL)

        self.btn_bantuan = wx.Button(id=wxID_FRAMEBANTUANBTN_BANTUAN,
              label='Bantuan', name='btn_bantuan', parent=self.panel1,
              pos=wx.Point(112, 136), size=wx.Size(75, 23), style=0)
        self.btn_bantuan.Bind(wx.EVT_BUTTON, self.OnBtn_bantuanButton,
              id=wxID_FRAMEBANTUANBTN_BANTUAN)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        # Tampil gambar logo belakang
        file_gambar = 'img/shield_about.png'
        img = wx.Image(file_gambar, wx.BITMAP_TYPE_ANY)
        self.logo.SetBitmap(wx.BitmapFromImage(img))

    def OnBtn_bantuanButton(self, event):
        """Menampilkan Frame bantuan"""
        call_form = FrameHelp.create(None)
        call_form.Show()
