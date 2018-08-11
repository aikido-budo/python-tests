#user_age=int(input("wie alt bist du: "))
#user_year=int(input("welches jahr haben wir?: "))
## print(user_age, user_year)
#def birth_year(age, year):
   #birth_y = year - age#
  # return  birth_y
# print(birth_year(user_age, user_year))
#birth_ye=str((birth_year(user_age, user_year)))
#file = open ("ergebniss.txt", "w")
#file.write (birth_ye)
#file.close()


import os
import time
#ip="8.8.8.8"
ip=str(input ("Welche IP soll angepingt werden? "))
pcount=str(input ("Wie oft soll geping werden? "))
blank=" "
# windows
# os.system("ping -n " + pcount + blank + ip)
# mac
os.system("ping -c " + pcount + blank + ip)
