import os, sys

print ("\033[1;32mTUAN HARUS MASUKAN USERNAME DAN PASSWORD BIAR BISA LOGIN")

print ("\033[1;32mWEBSITE = www.uch-2009.ueuo.com")

username = 'TOOLS2'      

password = 'TOOLS2'


def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("masukan username : ")

	if uname == username:

		pwd = raw_input("masukan password : ")



		if pwd == password:

			print "\033[1;32mPASS BENAR SILAKAN MENIKMATI BRO !", 

			sys.exit()



		else:

			print "\033[1;32mSorry Passwordmu salah TOD yang Bener !!!\033[00m"

			print "Masukan Ulang password dengan benar !\n"

			restart()



	else:

		print "\033[1;32mSorry..anda noob kalo gak tau tanya sama UCH-2009 !!!\033[00m"

		print "Masukan username dengan benar !\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()

