#Boa:Frame:Frame1

import wx
import wx.html
import wx.html as html


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1HTML_HELP, wxID_FRAME1PANEL1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(646, 183), size=wx.Size(370, 492),
              style=wx.DEFAULT_FRAME_STYLE, title='Bantuan Aplikasi')
        self.SetClientSize(wx.Size(354, 453))
        self.SetIcon(wx.Icon(u'img/icon.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(354, 453),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.html_help = wx.html.HtmlWindow(id=wxID_FRAME1HTML_HELP,
              name='html_help', parent=self.panel1, pos=wx.Point(8, 8),
              size=wx.Size(336, 440), style=wx.html.HW_SCROLLBAR_AUTO)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        # Load UserGuide.html
        self.html_help.LoadFile('UserGuide.html')
        

        
       
