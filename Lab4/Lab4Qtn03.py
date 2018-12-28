import sys

regions=[]   # empty list
key=[]
value=[]
fhandle = open("regions.txt", 'r')

for region in fhandle:
    key.append(region.rstrip().rsplit(',', 1)[0])           # split the string at comma and populating left
    value.append(region.rstrip().rsplit(',', 1)[1])         # and right values to key and value strings

regionsHQ = dict(zip(key, value))    # creating a dictionary from the keys and values

choice = int(input("choose between operation 1 to 6, option 7 terminates the program\n"))

if choice == 1:
    for k in sorted(regionsHQ.keys()):
        print(k, regionsHQ[k], sep='-->')
elif choice == 2:
    for value in regionsHQ.values():
        if value[0] in ['m', 'M']:
            print(value)
elif choice == 3:
    for value in regionsHQ.values():
        if 'g' in value.lower():    # changing the value to lower so we can accommodate g and G
            print(value)
elif choice == 4:
    for key, value in regionsHQ.items():
        if key != value:
            print(value)
elif choice == 5:
    ordered_keys=[]
    for k in sorted(regionsHQ.keys(), key=lambda k: len(k)):    # order the keys in ascending order of their lengths
        ordered_keys.append(k)
    print(regionsHQ[ordered_keys[-1]])                        # display last item which is also the longest in the list
elif choice == 6:
    select = input("Specify region to search for\n")
    check=bool(False)
    for k in regionsHQ.keys():
        if str(k).lower() == select.lower():
            print(k, regionsHQ[k], sep='-->')
            check=bool(True)
            break
    if check is not True:
        print("This region does not exist in the list")

elif choice == 7:
    print("Program is terminated")
    sys.exit()


# OUTPUT
# choose between operation 1 to 6, option 7 terminates the program
# 1
# Arusha-->Arusha
# Dar es Salaam-->Dar es Salaam
# Dodoma-->Dodoma
# Kagera-->Bukoba
# Katavi-->Mpanda
# Kilimanjaro-->Moshi
# Lindi-->Lindi
# Manyara-->Babati
# Mara-->Musoma
# Mbeya-->Mbeya
# Morogoro-->Morogoro
# Mtwara-->Mtwara
# Mwanza-->Mwanza
# Pwani-->Kibaha
# Rukwa-->Sumbawanga
# Ruvuma-->Songea
# Simiyu-->Bariadi
# Singida-->Singida
# Songwe-->Vwawa
# Tabora-->Tabora
# Tanga-->Tanga

# choose between operation 1 to 6, option 7 terminates the program
# 2
# Mtwara
# Musoma
# Mbeya
# Moshi
# Mwanza
# Morogoro
# Mpanda

# choose between operation 1 to 6, option 7 terminates the program
# 3
# Songea
# Sumbawanga
# Singida
# Tanga
# Morogoro

# choose between operation 1 to 6, option 7 terminates the program
# 4
# Kibaha
# Musoma
# Songea
# Sumbawanga
# Moshi
# Bukoba
# Mpanda
# Babati
# Bariadi
# Vwawa

# choose between operation 1 to 6, option 7 terminates the program
# 5
# Dar es Salaam

# choose between operation 1 to 6, option 7 terminates the program
# 6
# Specify region to search for
# arusha
# Arusha-->Arusha

# choose between operation 1 to 6, option 7 terminates the program
# 7
# Program is terminated