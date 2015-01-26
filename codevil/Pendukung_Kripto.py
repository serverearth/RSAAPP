#-------------------------------------------------------------------------------
# Name:        module Pendukung_Kripto
# Purpose:
#
# Author:      yanwar
#
# Created:     09/11/2014
# Copyright:   (c) yanwar 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import EasyDialogs
import wx


def ambil_ext_file(filename):
    """Mengambil ekstensi file, nilai kembalinya berupa string ekstensi file"""
    '''mengambil ekstensi file, return String ekstensi file'''
    ext = os.path.splitext(filename)
    return ext[1]

def ambil_nama_file(filename):
    """Mengambil nama file"""
    '''mengambil nama file, return String nama file'''
    namafile = os.path.basename(filename)
    return namafile

def ambil_file(list_allow_file):
    """Mengambil file"""
    '''get file berdasarkan saringan tertentu,
    thanks to : http://www.java2s.com/Tutorial/Python/0380__wxPython/ChooseafilefromFileDialog.htm'''
    #app = wx.PySimpleApp()
    wildcard = ""
    limit_wildcard = len(list_allow_file)
    for index,i in enumerate(list_allow_file):
        if index < limit_wildcard:
            wildcard += i + " Source (*." + i + ")|*." + i + "|"
        else:
            break
    '''wildcard = "Python source (*.py)|*.py| Compiled Python (*.pyc)|*.pyc|" \
            "All files (*.*)|*.*"'''
    dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        return dialog.GetPath().replace("\\","/")
    dialog.Destroy()

def ambil_dir():
    """Mengambil direktori"""
    filename = EasyDialogs.AskFolder(
    message='Name the destination',
    defaultLocation=os.getcwd(),
    wanted=unicode,
    )

    path = filename
    if len(path) == 3:
        return path.replace('\\','/')
    else:
        return path.replace('\\','/') + '/'

def get_file_size(filename):
    statinfo = os.stat(filename)
    return statinfo.st_size / 1024 / 1024

def baca_kunci_rsa():
    """Baca kunci RSA dalam direktori.

    Nilai kembalinya berupa list kunci dimana nilai indeksnya :
        indeks 0 = identitas kunci
        indeks 1 = modulo N
        indeks 2 = eksponen D / E
    """
    filename = ambil_file(['key'])
    if filename.endswith('.key'):
        with open(filename,"rb") as f:
            kunci = f.readlines()
        return kunci
    else:
        return False

def check_extension_file(filename):
    """Mengecek ekstensi file yang akan di enkrip dan dekrip"""
    if filename.endswith('.doc') or filename.endswith('.xls') or filename.endswith('.key'):
        return True
    else:
        return False

def input_dialog(message):
    response = EasyDialogs.AskString(message, default='yourid')
    return response

if __name__ == '__main__':
    print ambil_dir()
    print ambil_nama_file('D:/haha.xls')
