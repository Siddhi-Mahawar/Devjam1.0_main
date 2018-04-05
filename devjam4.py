import os
a='a'
b='b'
def geary():
    
    a = raw_input("Install Geary?   y/n:")
    if a is 'y':
        os.system("sudo add-apt-repository ppa:geary-team/releases")
        os.system("sudo apt update")
        os.system("sudo apt install geary")

def git():
	print("y/n:")
	b= raw_input("Install Git?   y/n:")
	if b=="y":
		os.system("sudo apt-get update")
geary()
git()