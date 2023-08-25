# author : @Syhrularv_
# -*- coding: utf-8 -*-

import os
import sys
import fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m' #putih
B = '\033[1;34m' #Biru
R = '\033[1;31m'
G = '\033[1;32m' #hijau
Y = '\033[1;33m' #kuning
C = '\033[1;36m' 

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'

banner = """     
         ⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⣠⣶⣿⣿⡿⣿⣿⣿⡿⠋⠉⠀⠀⠉⠙⢿⣿⣿⡿⣿⣿⣷⣦⡀⠀⠀⠀
                            ⠀⢀⣼⣿⣿⠟⠁⢠⣿⣿⠏⠀⠀⢠⣤⣤⡀⠀⠀⢻⣿⣿⡀⠙⢿⣿⣿⣦⠀⠀
                            ⣰⣿⣿⡟⠁⠀⠀⢸⣿⣿⠀⠀⠀⢿⣿⣿⡟⠀⠀⠈⣿⣿⡇⠀⠀⠙⣿⣿⣷⡄
                            ⠈⠻⣿⣿⣦⣄⠀⠸⣿⣿⣆⠀⠀⠀⠉⠉⠀⠀⠀⣸⣿⣿⠃⢀⣤⣾⣿⣿⠟⠁
                            ⠀⠀⠈⠻⣿⣿⣿⣶⣿⣿⣿⣦⣄⠀⠀⠀⢀⣠⣾⣿⣿⣿⣾⣿⣿⡿⠋⠁⠀⠀
                           ⠀  ⠀ ⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀
                          ⠀ ⠀⠀⠀⠀  ⠀⠀⠈⠉⠛⠛⠿⠿⠿⠿⠿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 
                     {}╔═╗ ╔╗╔ ╔═╗     ╔╦╗ ╔╗╔ ╔═╗     ╔═╗ ╔═╗ ╦ ╦ 
                     {}║╣  ║║║ ║        ║║ ║║║ ║   ==  ║   ╠═╝ ╚╦╝ 
                     {}╚═╝ ╝╚╝ ╚═╝     ═╩╝ ╝╚╝ ╚═╝     ╚═╝ ╩    ╩
                            {}⟦ {}WELCOME TO TOOLS UCH-2009 {}⟧
       
{}➣ {}Created By  {}:{} UCH 2009
{}➣ {}Community   {}:{} FROM UCH 2009 
{}➣ {}Version     {}:{} 0.01 {}Version

""".format(W,W,W,Y,W,Y,Y,G,Y,G,Y,G,Y,G,Y,G,Y,G,G)

banner2 = """

{}[ {}𝚂𝙸𝙻𝙰𝙺𝙰𝙽 𝚃𝚄𝙰𝙽 𝙱𝙸𝚂𝙰 𝙿𝙰𝙺𝙴 𝚃𝙾𝙾𝙻𝚂𝙽𝚈𝙰 {}]

{}╔═══════════════════╗
{}║  {}ENC & DNE - CPY  {}║
{}╟━━━┳━━━━━━━━━━━━━━━╢ 
{}║{}[{}1{}]{}┃  {}Decrypt      {}║
{}║{}[{}2{}]{}┃  {}Encript      {}║
{}╚═══╧═══════════════╝
""".format(Y,W,Y,B,B,R,B,B,B,Y,G,Y,B,W,B,B,Y,G,Y,B,W,B,B)

print banner
print banner2

def dekrip():
   try:
       sc = raw_input(ask + W + " Masukan Name Sc yang tuan sudah buat tadi " + G + "➮" + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "Masukan Name Baru Buat Sc yang sudah di buat " + G + "➮ " + W)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.system("mv -f tes.sh " + out)
       print (sukses + "Done.. Gak Bang [ Done ]")

   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Tidak Ada !")

def enkrip():
   try:
       script = raw_input(ask + W + " Masukan Name Sc yang tuan sudah buat tadi " + G + "➮" + W)
       output = raw_input(ask + W + "Masukan Name Baru Buat Sc yang sudah di buat " + G + "➮ " + W)
       os.system("bash-obfuscate " + script + " -o " + output )
       print (sukses + "Done..Gak Bang [ Done ]")
   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Tidak Ada ! ")


takok = raw_input(W + " Masukan Nomer " + G + "➮")

if takok == "1" or takok == "01":
   enkrip()
elif takok == "2" or takok == "02":
   dekrip()
else:
   print (eror + " pilih Yang bener TOD ! ")
