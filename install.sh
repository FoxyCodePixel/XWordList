#!/bin/bash

echo " "
echo "*** Installing Requirements ***"
echo " "

echo $(pip3 install colorama)
sleep 1
echo " "
echo "*** Creating directories ***"
$(mkdir result)
$(mkdir result/fasttrack)
$(mkdir result/john)
$(mkdir result/nmap)
$(mkdir result/rockyou)
$(mkdir result/sqlmap)
$(mkdir result/wifite)

echo " "
echo "*** Done! "
sleep 2

echo " "
echo "*** Downloading rockyou wordlist *** "
echo $(wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt && mv rockyou.txt WordList/)

echo " "
echo "*** Installation done! *** "
sleep 1

echo $(chmod +x xwl.py)
echo "*** Now run the tool by typing './xwl.py' OR 'python3 xwl.py' *** "
echo " "
