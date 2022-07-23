#!/usr/bin/env python3

# Foxy Code Pixel
# Github   : https://github.com/FoxyCodePixel
# Telegram : https://telegram.me/IvanLipovsky

# libraries
from colorama import Fore as c #color
import threading
import itertools
import time
import sys
import os

# The followingline is optianal, uncomment if you want to clear terminal each time you run this tool
# os.system("clear")

# global variables
option = ""
first_menu = ""
done = False

############
def Ascii():
  
  global first_menu
  
  #ascii
  icon = (f'''
 __________________________________________________
|==================================================|
| __  ___________  ___________            * * * == |
|[_j  L_I_I_I_I_j  L_I_I_I_I_j            ~~~~~ == |
|________________________________ _______ ______==_|
|[__I_I_I_I_I_I_I_I_I_I_I_I_I_I_] [__I__] [_I_I_I_]|
|[___I_I_I_I_I_I_I_I_I_I_I_I_]  |    _    [_I_I_I_]|
|[__I_I_I_I_I_I_I_I_I_I_I_I_L___|  _[_]_  [_I_I_I_]|
|[_____I_I_I_I_I_I_I_I_I_I_I____] [_I_I_] [_I_I_T ||
|[__I__I___________________I__L_] _______ [___I_I_j|
|                                                  |
| X Word List                     By FoxyCodePixel |
l__________________________________________________|

{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}Find by Length{c.RESET} 
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}Find by Name{c.RESET}{c.RED}
''')
  print(icon)
  first_menu = int(input(f"{c.RESET}>>> "))

###########
def menu():

  global option
  
  menu = (f'''

{c.RESET}Please choose your Password list below :

{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}rockyou.txt{c.RESET}     {c.WHITE}[{c.RED}4{c.WHITE}] {c.CYAN}nmap.lst{c.RESET}
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}john.lst{c.RESET}        {c.WHITE}[{c.RED}5{c.WHITE}] {c.CYAN}sqlmap.txt{c.RESET}
{c.WHITE}[{c.RED}3{c.WHITE}] {c.CYAN}fasttrack.txt{c.RESET}   {c.WHITE}[{c.RED}6{c.WHITE}] {c.CYAN}wifite.txt{c.RESET}
''')
  print(menu)
  option = int(input(">>> "))

##############
def rockyou():
  
  menu = (f"""
{c.WHITE}[{c.RED}rockyou{c.WHITE}] 
  
{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}Find passwords from range X to range Y{c.RESET}   
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}Find passwords in range X{c.RESET}
""")
  print(menu)
  choose = int(input(">>> "))    
  
  if choose == 1:
    print(" ")
    X = input("From range  : ")
    Y = input("To range    : ")  
    O = input("Output file : ")
    
    st = time.time()
    os.system("grep -x '.\{" + X + "," + Y + "\}'" + " WordList/rockyou.txt > result/rockyou/" + O + '.txt')
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/rockyou/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
    
  elif choose == 2:
    print(" ")
    X = input("In range    : ")
    O = input("Output file : ") 
    
    st = time.time()   
    os.system("grep -x '.\{" + X + "\}'" + " WordList/rockyou.txt > result/rockyou/" + O + '.txt')
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/rockyou/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
      
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ") 
    check = input(">>> ")
    if check == "y":
      rockyou()
    else:
      sys.exit()
      
##########      
def john():

  menu = (f"""
{c.WHITE}[{c.RED}john{c.WHITE}] 
  
{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}Find passwords from range X to range Y{c.RESET}   
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}Find passwords in range X{c.RESET}
""")
  print(menu)
  choose = int(input(">>> "))    
  
  if choose == 1:
    print(" ")
    X = input("From range  : ")
    Y = input("To range    : ")  
    O = input("Output file : ")
    
    st = time.time()
    os.system("grep -x '.\{" + X + "," + Y + "\}'" + " WordList/john.lst > result/john/" + O + '.txt')
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/john/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
    
  elif choose == 2:
    print(" ")
    X = input("In range    : ")
    O = input("Output file : ") 
    
    st = time.time()   
    os.system("grep -x '.\{" + X + "\}'" + " WordList/john.lst > result/john/" + O + '.txt')
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/john/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
      
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ") 
    check = input(">>> ")
    if check == "y":
      john()
    else:
      sys.exit()
  
################
def fasttrack():   

  menu = (f"""
{c.WHITE}[{c.RED}fasttrack{c.WHITE}] 
  
{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}Find passwords from range X to range Y{c.RESET}   
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}Find passwords in range X{c.RESET}
""")
  print(menu)
  choose = int(input(">>> "))    
  
  if choose == 1:
    print(" ")
    X = input("From range  : ")
    Y = input("To range    : ")  
    O = input("Output file : ")
    
    st = time.time()
    os.system("grep -x '.\{" + X + "," + Y + "\}'" + " WordList/fasttrack.txt > result/fasttrack/" + O + '.txt')
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/fasttrack/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
    
  elif choose == 2:
    print(" ")
    X = input("In range    : ")
    O = input("Output file : ") 
    
    st = time.time()   
    os.system("grep -x '.\{" + X + "\}'" + " WordList/fasttrack.txt > result/fasttrack/" + O + '.txt')
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/fasttrack/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
      
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ") 
    check = input(">>> ")
    if check == "y":
      fasttrack()
    else:
      sys.exit()      
      
###########
def nmap():    

  menu = (f"""
{c.WHITE}[{c.RED}nmap{c.WHITE}] 
  
{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}Find passwords from range X to range Y{c.RESET}   
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}Find passwords in range X{c.RESET}
""")
  print(menu)
  choose = int(input(">>> "))    
  
  if choose == 1:
    print(" ")
    X = input("From range  : ")
    Y = input("To range    : ")  
    O = input("Output file : ")
    
    st = time.time()
    os.system("grep -x '.\{" + X + "," + Y + "\}'" + " WordList/nmap.lst > result/nmap/" + O + '.txt')
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/nmap/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
    
  elif choose == 2:
    print(" ")
    X = input("In range    : ")
    O = input("Output file : ") 
    
    st = time.time()   
    os.system("grep -x '.\{" + X + "\}'" + " WordList/nmap.lst > result/nmap/" + O + '.txt')
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/nmap/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
      
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ") 
    check = input(">>> ")
    if check == "y":
      nmap()
    else:
      sys.exit()      
      
#############
def sqlmap():        

  menu = (f"""
{c.WHITE}[{c.RED}sqlmap{c.WHITE}] 
  
{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}Find passwords from range X to range Y{c.RESET}   
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}Find passwords in range X{c.RESET}
""")
  print(menu)
  choose = int(input(">>> "))    
  
  if choose == 1:
    print(" ")
    X = input("From range  : ")
    Y = input("To range    : ")  
    O = input("Output file : ")
    
    st = time.time()
    os.system("grep -x '.\{" + X + "," + Y + "\}'" + " WordList/sqlmap.txt > result/sqlmap/" + O + '.txt')
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/sqlmap/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
    
  elif choose == 2:
    print(" ")
    X = input("In range    : ")
    O = input("Output file : ") 
    
    st = time.time()   
    os.system("grep -x '.\{" + X + "\}'" + " WordList/sqlmap.txt > result/sqlmap/" + O + '.txt')
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/sqlmap/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
      
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ") 
    check = input(">>> ")
    if check == "y":
      sqlmap()
    else:
      sys.exit()      

#############      
def wifite():      

  menu = (f"""
{c.WHITE}[{c.RED}wifite{c.WHITE}] 
  
{c.RED}Note! range starts with 8{c.RESET}
{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}Find passwords from range X to range Y{c.RESET}   
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}Find passwords in range X{c.RESET}
""")
  print(menu)
  choose = int(input(">>> "))    
  
  if choose == 1:
    print(" ")
    X = input("From range  : ")
    Y = input("To range    : ")  
    O = input("Output file : ")
    
    st = time.time()
    os.system("grep -x '.\{" + X + "," + Y + "\}'" + " WordList/wifite.txt > result/wifite/" + O + '.txt')
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/wifite/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
    
  elif choose == 2:
    print(" ")
    X = input("In range    : ")
    O = input("Output file : ") 
    
    st = time.time()   
    os.system("grep -x '.\{" + X + "\}'" + " WordList/wifite.txt > result/wifite/" + O + '.txt')
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/wifite/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
      
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ") 
    check = input(">>> ")
    if check == "y":
      wifite()
    else:
      sys.exit()      

###################
def rockyou_name():
  
  menu = (f"""
{c.WHITE}[{c.RED}rockyou{c.WHITE}] 
  
{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}Look for special pattern {c.RED}(like '#$!!^^&&#$%'){c.RESET}   
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}Look for any pattern include your name {c.RED}(like 'alex' in 'eralexfs435'){c.RESET}
""")
  print(menu)
  choose = int(input(">>> "))    
  
  if choose == 1:
    print(" ")
    X = input("What you are searching for  : ")
    Y = input("Match only whole lines? y/n : ")  
    O = input("Output file name            : ")
    
    if Y == "y":
      st = time.time()
      os.system(f"grep -x {X} WordList/rockyou.txt > result/rockyou/{O}.txt")
      et = time.time()
      print(f"\nFile saved into {c.GREEN}result/rockyou/{O}.txt{c.RESET}")
      print(f"Search time : {c.GREEN}{et - st}{c.RESET}")

    if Y == "n":
      st = time.time()
      os.system(f"grep -F {X} WordList/rockyou.txt > result/rockyou/{O}.txt")
      et = time.time()
      print(f"\nFile saved into {c.GREEN}result/rockyou/{O}.txt{c.RESET}")
      print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
          
  elif choose == 2:
    print(" ")
    X = input("What you are searching for  : ")  
    O = input("Output file name            : ") 
    
    st = time.time()
    os.system(f"grep {X} WordList/rockyou.txt > result/rockyou/{O}.txt")
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/rockyou/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
      
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ") 
    check = input(">>> ")
    if check == "y":
      rockyou_name()
    else:
      sys.exit()
 
################
def john_name():
  
  menu = (f"""
{c.WHITE}[{c.RED}john{c.WHITE}] 
  
{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}Look for special pattern {c.RED}(like '#$!!^^&&#$%'){c.RESET}   
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}Look for any pattern include your name {c.RED}(like 'alex' in 'eralexfs435'){c.RESET}
""")
  print(menu)
  choose = int(input(">>> "))    
  
  if choose == 1:
    print(" ")
    X = input("What you are searching for  : ")
    Y = input("Match only whole lines? y/n : ")  
    O = input("Output file name            : ")
    
    if Y == "y":
      st = time.time()
      os.system(f"grep -x {X} WordList/john.lst > result/john/{O}.txt")
      et = time.time()
      print(f"\nFile saved into {c.GREEN}result/john/{O}.txt{c.RESET}")
      print(f"Search time : {c.GREEN}{et - st}{c.RESET}")

    if Y == "n":
      st = time.time()
      os.system(f"grep -F {X} WordList/john.lst > result/john/{O}.txt")
      et = time.time()
      print(f"\nFile saved into {c.GREEN}result/john/{O}.txt{c.RESET}")
      print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
          
  elif choose == 2:
    print(" ")
    X = input("What you are searching for  : ")  
    O = input("Output file name            : ") 
    
    st = time.time()
    os.system(f"grep {X} WordList/john.lst > result/john/{O}.txt")
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/john/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
      
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ") 
    check = input(">>> ")
    if check == "y":
      john_name()
    else:
      sys.exit()

#####################
def fasttrack_name():
  
  menu = (f"""
{c.WHITE}[{c.RED}fasttrack{c.WHITE}] 
  
{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}Look for special pattern {c.RED}(like '#$!!^^&&#$%'){c.RESET}   
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}Look for any pattern include your name {c.RED}(like 'alex' in 'eralexfs435'){c.RESET}
""")
  print(menu)
  choose = int(input(">>> "))    
  
  if choose == 1:
    print(" ")
    X = input("What you are searching for  : ")
    Y = input("Match only whole lines? y/n : ")  
    O = input("Output file name            : ")
    
    if Y == "y":
      st = time.time()
      os.system(f"grep -x {X} WordList/fasttrack.txt > result/fasttrack/{O}.txt")
      et = time.time()
      print(f"\nFile saved into {c.GREEN}result/fasttrack/{O}.txt{c.RESET}")
      print(f"Search time : {c.GREEN}{et - st}{c.RESET}")

    if Y == "n":
      st = time.time()
      os.system(f"grep -F {X} WordList/fasttrack.txt > result/fasttrack/{O}.txt")
      et = time.time()
      print(f"\nFile saved into {c.GREEN}result/fasttrack/{O}.txt{c.RESET}")
      print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
          
  elif choose == 2:
    print(" ")
    X = input("What you are searching for  : ")  
    O = input("Output file name            : ") 
    
    st = time.time()
    os.system(f"grep {X} WordList/fasttrack.txt > result/fasttrack/{O}.txt")
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/fasttrack/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
      
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ") 
    check = input(">>> ")
    if check == "y":
      fasttrack_name()
    else:
      sys.exit()               
               
################
def nmap_name():
  
  menu = (f"""
{c.WHITE}[{c.RED}nmap{c.WHITE}] 
  
{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}Look for special pattern {c.RED}(like '#$!!^^&&#$%'){c.RESET}   
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}Look for any pattern include your name {c.RED}(like 'alex' in 'eralexfs435'){c.RESET}
""")
  print(menu)
  choose = int(input(">>> "))    
  
  if choose == 1:
    print(" ")
    X = input("What you are searching for  : ")
    Y = input("Match only whole lines? y/n : ")  
    O = input("Output file name            : ")
    
    if Y == "y":
      st = time.time()
      os.system(f"grep -x {X} WordList/nmap.lst > result/nmap/{O}.txt")
      et = time.time()
      print(f"\nFile saved into {c.GREEN}result/nmap/{O}.txt{c.RESET}")
      print(f"Search time : {c.GREEN}{et - st}{c.RESET}")

    if Y == "n":
      st = time.time()
      os.system(f"grep -F {X} WordList/nmap.lst > result/nmap/{O}.txt")
      et = time.time()
      print(f"\nFile saved into {c.GREEN}result/nmap/{O}.txt{c.RESET}")
      print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
          
  elif choose == 2:
    print(" ")
    X = input("What you are searching for  : ")  
    O = input("Output file name            : ") 
    
    st = time.time()
    os.system(f"grep {X} WordList/nmap.lst > result/nmap/{O}.txt")
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/nmap/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
      
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ") 
    check = input(">>> ")
    if check == "y":
      nmap_name()
    else:
      sys.exit()               
               
##################
def sqlmap_name():
  
  menu = (f"""
{c.WHITE}[{c.RED}sqlmap{c.WHITE}] 
  
{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}Look for special pattern {c.RED}(like '#$!!^^&&#$%'){c.RESET}   
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}Look for any pattern include your name {c.RED}(like 'alex' in 'eralexfs435'){c.RESET}
""")
  print(menu)
  choose = int(input(">>> "))    
  
  if choose == 1:
    print(" ")
    X = input("What you are searching for  : ")
    Y = input("Match only whole lines? y/n : ")  
    O = input("Output file name            : ")
    
    if Y == "y":
      st = time.time()
      os.system(f"grep -x {X} WordList/sqlmap.txt > result/sqlmap/{O}.txt")
      et = time.time()
      print(f"\nFile saved into {c.GREEN}result/sqlmap/{O}.txt{c.RESET}")
      print(f"Search time : {c.GREEN}{et - st}{c.RESET}")

    if Y == "n":
      st = time.time()
      os.system(f"grep -F {X} WordList/sqlmap.txt > result/sqlmap/{O}.txt")
      et = time.time()
      print(f"\nFile saved into {c.GREEN}result/sqlmap/{O}.txt{c.RESET}")
      print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
          
  elif choose == 2:
    print(" ")
    X = input("What you are searching for  : ")  
    O = input("Output file name            : ") 
    
    st = time.time()
    os.system(f"grep {X} WordList/sqlmap.txt > result/sqlmap/{O}.txt")
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/sqlmap/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
      
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ") 
    check = input(">>> ")
    if check == "y":
      sqlmap_name()
    else:
      sys.exit()                
               
##################
def wifite_name():
  
  menu = (f"""
{c.WHITE}[{c.RED}wifite{c.WHITE}] 
  
{c.WHITE}[{c.RED}1{c.WHITE}] {c.CYAN}Look for special pattern {c.RED}(like '#$!!^^&&#$%'){c.RESET}   
{c.WHITE}[{c.RED}2{c.WHITE}] {c.CYAN}Look for any pattern include your name {c.RED}(like 'alex' in 'eralexfs435'){c.RESET}
""")
  print(menu)
  choose = int(input(">>> "))    
  
  if choose == 1:
    print(" ")
    X = input("What you are searching for  : ")
    Y = input("Match only whole lines? y/n : ")  
    O = input("Output file name            : ")
    
    if Y == "y":
      st = time.time()
      os.system(f"grep -x {X} WordList/wifite.txt > result/wifite/{O}.txt")
      et = time.time()
      print(f"\nFile saved into {c.GREEN}result/wifite/{O}.txt{c.RESET}")
      print(f"Search time : {c.GREEN}{et - st}{c.RESET}")

    if Y == "n":
      st = time.time()
      os.system(f"grep -F {X} WordList/wifite.txt > result/wifite/{O}.txt")
      et = time.time()
      print(f"\nFile saved into {c.GREEN}result/wifite/{O}.txt{c.RESET}")
      print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
          
  elif choose == 2:
    print(" ")
    X = input("What you are searching for  : ")  
    O = input("Output file name            : ") 
    
    st = time.time()
    os.system(f"grep {X} WordList/wifite.txt > result/wifite/{O}.txt")
    et = time.time()
    print(f"\nFile saved into {c.GREEN}result/wifite/{O}.txt{c.RESET}")
    print(f"Search time : {c.GREEN}{et - st}{c.RESET}")
      
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ") 
    check = input(">>> ")
    if check == "y":
      wifite_name()
    else:
      sys.exit()               
                              
####################           
def loading_first():
  
  global done
  
  for c in itertools.cycle(['*', '**', '***']):
    if done:
      break
    sys.stdout.write('\rRunning first option for you ' + c)
    sys.stdout.flush()
    time.sleep(0.5)     
            
#####################           
def loading_second():
  
  global done
  
  for c in itertools.cycle(['*', '**', '***']):
    if done:
      break
    sys.stdout.write('\rRunning second option for you ' + c)
    sys.stdout.flush()
    time.sleep(0.5)  
                
###################
def mainmenu_len():
  menu()
  
  if option == 1:
    rockyou()
  
  elif option == 2:
    john()
     
  elif option == 3:
    fasttrack()  
    
  elif option == 4:
    nmap()  
    
  elif option == 5:
    sqlmap()  
  
  elif option == 6:
    wifite()  
    
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ")
    check = input(">>> ")
    if check == "y":
      mainmenu()
    else:
      sys.exit()      
      
####################
def mainmenu_name():
  menu()
  
  if option == 1:
    rockyou_name()
  
  elif option == 2:
    john_name()
     
  elif option == 3:
    fasttrack_name()  
    
  elif option == 4:
    nmap_name()  
    
  elif option == 5:
    sqlmap_name()  
  
  elif option == 6:
    wifite_name()  
    
  else:
    print(f"{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ") 
    check = input(">>> ")
    if check == "y":
      mainmenu_name()
    else:
      sys.exit()  
            
###########  
def main():
  
  global option, done, first_menu

  Ascii()
  
  if first_menu == 1:
    ft = threading.Thread(target=loading_first)
    ft.start()
    time.sleep(1.5)
    done = True
    mainmenu_len()
    
  elif first_menu == 2:
    st = threading.Thread(target=loading_second)
    st.start() 
    time.sleep(1.5)
    done = True
    mainmenu_name()
  
  else:
    print(f"\n{c.RED}Oops! wrong option! do you want to go back to menu? {c.YELLOW}y/n{c.RESET} ")
    check = input(">>> ")
    if check == "y":
      Ascii()
    else:
      sys.exit()
  
if __name__ == "__main__":
  main()
  
# Foxy Code Pixel
