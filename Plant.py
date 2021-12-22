import os
os.system('cls' if os.name == 'nt' else 'clear')

total = 0
psym = "%"

print("\033[1;37;31m---[Plant Emergency Notification Identity System]---\033[1;37;0m".center(os.get_terminal_size().columns))
print(" \n \n")
print("\033[1;32;40m[Severity Determination Software]\033[1;37;0m")
print(" \n")

plant = str(input('    1)   Is the fucking plant in a disproportionately small pot?    [y= Yes , n= No]     '))
if plant == "y":
    total = (total+1)
if plant == "n":
    total = (total-1)
print(" ")

plant1 = str(input('    2)   Uhhh are the leaves Brown?    [y= Yes , n= No]     '))
if plant1 == "y":
    total = (total+1)
if plant == "n":
    total = (total-1)
print(" ")

plant2 = str(input('    3)   Weird as shit spots?    [y= Yes , n= No]     '))
if plant2 == "y":
    total = (total+1)
if plant == "n":
    total = (total-1)
print(" ")

plant3 = str(input('    4)   Are leaves falling off?    [y= Yes , n= No]     '))
if plant3 == "y":
    total = (total+1)
if plant == "n":
    total = (total-1)
print(" ")

plant4 = str(input('    5)   Have you not been fucking watering it?    [y= Yes , n= No]     '))
if plant4 == "y":
    total = (total+1)
if plant == "n":
    total = (total-1)
print(" ")

plant5 = str(input('    6)   Did the cat shit in the pot?    [y= Yes , n= No]     '))
if plant5 == "y":
    total = (total+1)
if plant == "n":
    total = (total-1)
print(" ")


plant6 = str(input('    7)   Was Eco around it?    [y= Yes , n= No]     '))
if plant6 == "y":
    total = (total+1)
if plant == "n":
    total = (total-1)
print(" ")

plant7 = str(input('    8)   Did the fucker fall over recently?    [y= Yes , n= No]     '))
if plant7 == "y":
    total = (total+1)
if plant == "n":
    total = (total-1)
print(" ")

plant8 = str(input('    9)   Did you use Vodka and not water so you can get drunk as fuck together?    [y= Yes , n= No]     '))
if plant8 == "y":
    total = (total+1)
if plant == "n":
    total = (total-1)
print(" ")

plant9 = str(input('    10)   Is the plant pissed as shit at you because you were a fucking dick last night?    [y= Yes , n= No]     '))
if plant9 == "y":
    total = (total+1)
if plant == "n":
    total = (total-1)
print(" \n \n \n")
print("---------------------------------------------------------")

percent = total/10
print("Total Score: ", total)
if total > 0:
    print("Degree of Emergency:", percent*100, psym)
    print("\033[1;37;40m[Holy shit dat plant in da danger zone]\033[1;37;0m")
    print("---------------------------------------------------------")
else:
    print("Degree of Emergency: 0%")
    print("\033[1;37;40m[Holy shit dat plant doin baller]\033[1;37;0m")
    print("---------------------------------------------------------")
print(" ")
