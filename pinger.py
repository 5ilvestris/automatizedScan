import argparse
import socket
import os

parser = argparse.ArgumentParser()
parser.add_argument(
  "-p",
  "--ping",
  dest="ping",
  type=str,
  help="Pinglenecek site",
)
parser.add_argument(
  "-o",
  "--output",
  dest="output",
  type=str,
  help="Pinglenecek site",
)
args = parser.parse_args()
adress = args.ping




socket.setdefaulttimeout(2)
host = socket.gethostbyname(args.ping)
print(host)

cwd = os.getcwd()
print(cwd)
# nmap -sV --script=vulscan/vulscan.nse www.example.com

os.system("nmap -sv --script="+cwd+"""/vulscan/vulscan.nse """+host)




