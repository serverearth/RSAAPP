#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import FrameMain

modules ={u'FrameAktivitas': [0, '', u'FrameAktivitas.py'],
 u'FrameBantuan': [0, '', u'FrameBantuan.py'],
 u'FrameDekripsi': [0, '', u'FrameDekripsi.py'],
 u'FrameEnkripsi': [0, '', u'FrameEnkripsi.py'],
 u'FrameGenKey': [0, '', u'FrameGenKey.py'],
 u'FrameHelp': [0, '', u'FrameHelp.py'],
 u'FrameKantor': [0, '', u'FrameKantor.py'],
 u'FrameMain': [1, 'Main frame of Application', u'FrameMain.py']}

class BoaApp(wx.App):
    
        
    def OnInit(self):
        self.main = FrameMain.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
