#Boa:Frame:Frame1
import sys
import wx
import codevil
import EasyDialogs
import os
import datetime

file_datalog = 'virtualfile/data_log.log'

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1LC_AKTIVITAS, wxID_FRAME1PANEL1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class Frame1(wx.Frame):
    def _init_coll_lc_aktivitas_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading=u'Aktivitas', width=100)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading=u'User',
              width=120)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading=u'Waktu',
              width=130)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading=u'Proses', width=100)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading=u'Kunci',
              width=140)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT, heading=u'File',
              width=140)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(265, 132), size=wx.Size(913, 487),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Log Aktivitas')
        self.SetClientSize(wx.Size(897, 448))
        self.SetIcon(wx.Icon(u'D:/Laporan Dhe Fud Resto/Backup2/img/icon.ico',
              wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(897, 448),
              style=wx.TAB_TRAVERSAL)

        self.lc_aktivitas = wx.ListCtrl(id=wxID_FRAME1LC_AKTIVITAS,
              name=u'lc_aktivitas', parent=self.panel1, pos=wx.Point(40, 48),
              size=wx.Size(816, 328), style=wx.LC_REPORT)
        self._init_coll_lc_aktivitas_Columns(self.lc_aktivitas)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'Ekspor',
              name='button1', parent=self.panel1, pos=wx.Point(752, 400),
              size=wx.Size(107, 32), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.__loadLog()
    
    def __loadLog(self):
        """load data log aktivitas"""
        data_log = codevil.readDataLog(file_datalog)
        k = self.lc_aktivitas.GetItemCount()
        
        for idx,i in enumerate(data_log):
            self.lc_aktivitas.InsertStringItem(k,i[0])
            self.lc_aktivitas.SetStringItem(k,1,i[1])
            self.lc_aktivitas.SetStringItem(k,2,i[2])
            self.lc_aktivitas.SetStringItem(k,3,i[3])
            self.lc_aktivitas.SetStringItem(k,4,i[4])
            self.lc_aktivitas.SetStringItem(k,5,i[5])

    def OnButton1Button(self, event):
        """Event untuk mengekspor data-data log aktvitas"""
        jumbar = self.lc_aktivitas.GetItemCount()
        j = 0
        html = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        table {
            border-collapse: collapse;
            font-family : Consolas;
            font-size: 10pt;
        }

        .genkey{
        background: #005C99;
        color: white;
        }

        .enkripsi{
        background: #FF6600;
        color: white;
        }

        .dekripsi {
        background: #008A00;
        color: white;
        }
        .head{
        background: #521400;
        color: white;
        }
        table, td, th {
            border: 1px solid black;
            padding: 3px;
        }
        </style>
        </head>
        <body>
        """
        ##filename = codevil.ambil_dir()
        filename = ''
        # set direktori untuk menyimpan file eksport log
        dialog = wx.DirDialog(None, 'Choose a directory:',
            style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            # untuk single direktori seperti D:/ C:/ dan lain
            filename = dialog.GetPath()
            if len(filename) <= 3:
                pass
            else:
                filename = dialog.GetPath() + '\\'
            dialog.Destroy()
            html += "<table>"
            html += "<tr class='head'>"
            html += "<th>Aktivitas</th>"
            html += "<th>User</th>"
            html += "<th>Waktu</th>"
            html += "<th>Proses</th>"
            html += "<th>Kunci</th>"
            html += "<th>File</th>"
            html += "</tr>"
            print 'Selected:', filename
            while j <= jumbar - 1:
                aktivitas = self.lc_aktivitas.GetItem(j,0).GetText()
                user = self.lc_aktivitas.GetItem(j,1).GetText()
                waktu = self.lc_aktivitas.GetItem(j,2).GetText()
                proses = self.lc_aktivitas.GetItem(j,3).GetText()
                kunci = self.lc_aktivitas.GetItem(j,4).GetText()
                files = self.lc_aktivitas.GetItem(j,5).GetText()
                
                if aktivitas == "GENERATE_KEY":
                    html += "<tr class='genkey'>"
                elif aktivitas == "ENKRIPSI":
                    html += "<tr class='enkripsi'>"
                else:
                    html += "<tr class='dekripsi'>"
                html += "<td>" + aktivitas + "</td>"
                html += "<td>" +user+ "</td>"
                html += "<td>" +waktu+ "</td>"
                html += "<td>" +proses+ "</td>"
                html += "<td>" +kunci+ "</td>"
                html += "<td>" +files+ "</td>"
                html += "</tr>"
                j += 1
            html += "</table></body></html>"
            try:
            
                filename = filename +"AKTIVITAS." + str(datetime.datetime.now().strftime("%y-%m-%d-%H-%M")) + ".html"
                with open(filename,"w") as rep:
                    rep.write(html)
                wx.MessageDialog(self,"Aktivitas Berhasil di ekspor, cek di : " + filename, \
                "Notif", wx.OK).ShowModal()
                file_datalog = 'virtualfile/data_log.log'
                with open(file_datalog,"w") as f:
                    f.write("")
                
                self.__loadLog()
            except:
                wx.MessageDialog(self,"Aktivitas Gagal di ekspor !",\
                "Notif", wx.ICON_ERROR).ShowModal()
        else:
            dialog.Destroy()
            
        
        
            
    
        
        
        
        
