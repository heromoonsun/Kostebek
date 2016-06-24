#!/usr/bin/env python
#-*-coding:utf-8-*-

from tkinter import *
import os.path
from threading import Thread
import  portforwarder
import subprocess
import webbrowser
import time

class Uygulama(object):
    def __init__(self):
        self.arabirim()
        self.puttyAyniDizindemi()

    def arabirim(self):

        pencere.title("KÖSTEBEK by HeroMoonSun")
        pencere.resizable(width=FALSE, height=FALSE)
        pencere.geometry("500x500+600+460")


        self.etiket_putty = Label(text="Putty.exe aynı dizinde",font=("Helvetica", 12),justify=LEFT)
        self.etiket_putty.place(relx=0.03, rely=0.1 ,relwidth=0.3)

        self.etiket_putty_evet = Label(text="Evet",fg="green",font=("Helvetica", 12))
        self.etiket_putty_evet.place(relx=0.5, rely=0.1)



        self.etiket_sunucu_adresi = Label(text="Sunucu adresini girin yada IP",font=("Helvetica", 12),justify=LEFT)
        self.etiket_sunucu_adresi.place(relx=0.03,rely=0.2,relwidth=0.4)
        
        self.giris = Entry(font = "Helvetica 14 bold")
        self.giris.insert(END, 'formator.dynu.com')
        self.giris.place(relx=0.5,rely=0.2,relheight=0.05,relwidth=0.4)
        
        
        # YARDIM
        whatever_you_do = """IE ve Chrome Proxy ayarı İçin \nInternet Seçenekleri >Bağlantılar> Yerel ağ ayarları> Ara sunucu >Gelişmiş >Sock kutusuna \nlocalhost port kısmınada 8080 yazın.
        \nFirefox Proxy Ayarı İçin \n Seçenekler > Gelişmiş > Ağ > Ayarlar \n yolunu takip edin"""

        self.msg = Message(pencere, text = whatever_you_do,width=500)
        self.msg.config(bg='white', font=('times', 13))
        self.msg.place(relx=0, rely=0.35,relheight=0.4,relwidth=1)


        self.dugme = Button(text="KÖSTEBEĞİ BIRAK",font=("Helvetica", 16), command = self.baslat)
        self.dugme.place(relx=0.1, rely=0.8,relheight=0.1,relwidth=0.8)


        pencere.update_idletasks()
        w = pencere.winfo_screenwidth()
        h = pencere.winfo_screenheight()
        size = tuple(int(_) for _ in pencere.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        pencere.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def puttyAyniDizindemi(self):
        sonuc = os.path.exists("putty.exe")
        if sonuc:
            self.etiket_putty_evet = Label(text="Evet",fg="green")
        else:
            self.etiket_putty_evet["text"]  ="Hayır !!!!!"
            self.etiket_putty_evet["fg"]    ="red"



    def baslat(self):
        self.runPortForwarder()

    def runPortForwarder(self):
        
        self.test1  = Thread(target = self.proxyicalistir)
        self.test1.start() 
        
        self.test2  = Thread(target = self.putyicalistir)
        self.test2.start()
        
        self.test3  = Thread(target = self.chromeyiicalistir)
        self.test3.start()

    
    def proxyicalistir(self):
        hostname    = self.giris.get()
        subprocess.call("proxy.py localhost:2222 formator.dynu.com:80", shell=True)
    
    def putyicalistir(self):
        # putty yi çalıştıralım 
        response = os.system("putty.exe -ssh -D 8080 -P 2222 -pw 1234 anonim@localhost")

    def chromeyiicalistir(self):        
        time.sleep(5)
        
        try:
            response = os.system('start chrome --proxy-server="socks5://localhost:8080" "www.ipgor.com" "www.youtube.com" ')
        except ValueError:
            print ("Oops!  chrome bulunamadı")
            
       
        
        
      

pencere = Tk()
uyg = Uygulama()
mainloop()