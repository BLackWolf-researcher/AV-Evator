import os
import time
from colorama import *

init(convert=True)

try:
  time.sleep(30)
  
  if os.path.isfile("doc.exe"):
     print(Fore.GREEN + "av-not found!" + Fore.RESET) 
  else:
     print(Fore.RED + "warning av detected!" + Fore.RESET)
except:
  pass
