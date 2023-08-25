# athor : UCH-2009
# Tools Version : 0.1
# Admin website: www.uch-2009.com
clear

b='\033[1m'
u='\033[4m'
bl='\E[30m'
r='\E[31m'
g='\E[32m'
bu='\E[34m'
m='\E[35m'
c='\E[36m'
w='\E[37m'
endc='\E[0m'
enda='\033[0m'
blue='\e[1;34m'
cyan='\e[1;36m'
red='\e[1;31m'

RED="$(printf '\033[31m')"  GREEN="$(printf '\033[32m')"  ORANGE="$(printf '\033[33m')"  BLUE="$(printf '\033[34m')"
MAGENTA="$(printf '\033[35m')"  CYAN="$(printf '\033[36m')"  WHITE="$(printf '\033[37m')" BLACK="$(printf '\033[30m')"
REDBG="$(printf '\033[41m')"  GREENBG="$(printf '\033[42m')"  ORANGEBG="$(printf '\033[43m')"  BLUEBG="$(printf '\033[44m')"
MAGENTABG="$(printf '\033[45m')"  CYANBG="$(printf '\033[46m')"  WHITEBG="$(printf '\033[47m')" BLACKBG="$(printf '\033[40m')"
DEFAULT_FG="$(printf '\033[39m')"  DEFAULT_BG="$(printf '\033[49m')"

echo " "
echo "${GREEN} ╦ ╔╗╔ ╔═╗ ╔╦╗ ╔═╗ ╦┈┈ ╦┈┈ ┈ ╔═╗ ╔═╗ ╦═╗ ╦ ╔═╗ ╔╦╗  "
echo "${GREEN} ║ ║║║ ╚═╗ ┈║┈ ╠═╣ ║┈┈ ║┈┈ ┈ ╚═╗ ║┈┈ ╠╦╝ ║ ╠═╝ ┈║┈  "
echo "${GREEN} ╩ ╝╚╝ ╚═╝ ┈╩┈ ╩┈╩ ╩═╝ ╩═╝ ┈ ╚═╝ ╚═╝ ╩╚═ ╩ ╩┈┈ ┈╩┈  "
sleep 1s
echo "${WHITE} Script By : UCH 2009 FROM"
sleep 1s
echo  " "
echo "${BLUE}[${RED}!${BLUE}] ${GREEN}Tuan Mengunakan Software installasi Termux tunggu sampai instalasinya selesai"
sleep 1s
echo "${BLUE}[${RED}✓${BLUE}] ${GREEN}Loading Installing In Termux..."
    echo " "
      sleep 2s
   echo "~{${ORANGE} Bersiap Untuk Menginstal Tuan ${GREEN}}~"
      sleep 3s
    echo " "
pkg upgrade && pkg update
pkg install git
pkg install python2
pkg install python
pip2 install termcolor
pkg install nodejs
pkg install neofetch -y
npm install -g bash-obfuscate
bash ENC-TTp.sh

# copyright © UCH-2009
