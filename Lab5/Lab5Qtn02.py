import os
import statistics

# for output of question 2 please see a file named: output_qn02.txt

if os.path.exists('countries_data.txt'):
    output_file = open('countries_data.txt', 'w')
else:
    output_file = open('countries_data.txt', 'x')

countries_list = list()
csvfile_list = list()

with open('countries.txt', 'r') as txt_file, open('lab5Qtn2Values.csv', 'r') as csv_file:
    countries_list.append(txt_file.readlines())               # read each line and populate in a list
    csvfile_list.append(csv_file.readlines())                 # read each line and populate in a list

for i in range(117):
    output_file.write(countries_list[0][i].rstrip() + ',' + csvfile_list[0][i].rstrip() + '\n')

output_file.close()   # closing the file

# ---- end of Question 02 (c)

fhandle = open('countries_data.txt', 'r')  # opening file for next question

key = list()
value = list()

for data in fhandle:
    internal_list = []
    key.append(data.rsplit(',', 4)[0])
    for i in range(1, 4):
        internal_list.append(int(data.rsplit(',', 4)[i]))
    value.append(internal_list)

cdict = dict(zip(key, value))

print(cdict)
print("\n")

# ---- end of Question 02 (d)

january = []
february = []
march = []

for data in cdict.values():
    january.append(data[0])
    february.append(data[1])
    march.append(data[2])

print("{:<10}".format('Month'), end=' ')
print("{}".format('Min'), end=' ')
print("{}".format('Max'), end=' ')
print("{}".format('Average'), end=' ')
print("{}".format('Stdev'))

for month in ["January", "February", "March"]:
    if month == 'January':
        print("{:<10}".format(month), end=' ')
        print("{:1d}".format(min(january)), end=' ')
        print("{:5d}".format(max(january)), end=' ')
        print("{:6.2f}".format(statistics.mean(january)), end=' ')
        print("{:6.2f}".format(statistics.stdev(january)))
    elif month == 'February':
        print("{:<10}".format(month), end=' ')
        print("{:1d}".format(min(february)), end=' ')
        print("{:5d}".format(max(february)), end=' ')
        print("{:6.2f}".format(statistics.mean(february)), end=' ')
        print("{:6.2f}".format(statistics.stdev(february)))
    else:
        print("{:<10}".format(month), end=' ')
        print("{:1d}".format(min(march)), end=' ')
        print("{:5d}".format(max(march)), end=' ')
        print("{:6.2f}".format(statistics.mean(march)), end=' ')
        print("{:6.2f}".format(statistics.stdev(march)))
print("\n")

# ---- end of Question 02 (e)

for (k, v) in cdict.items():
    if v[0] == 100:
        print(k, '--->', v[0])

# ---- end of Question 02 (f)

print("\n")

select = input("Country name: ")
check = bool(False)
for k in cdict.keys():
    if k == select:
        print("January:", cdict[k][0])
        print("February:", cdict[k][1])
        print("March:", cdict[k][2])
        check = bool(True)
        break
if check is not True:
    print("This country name does not exist in the list")

print("\n")

# ---- end of Question 02 (g)

print("{:<5}".format('S/N'), end=' ')
print("{}".format('Country'), end=' ')
print("{:>20}".format('Jan Value'))

sn = 1
check = bool(False)
for (k, v) in cdict.items():
    if (v[0]>=50) and (v[0]<=70):
        print("{:<5}".format(sn), end=' ')
        print("{:<20}".format(k), end=' ')
        print("{}".format(v[0]))
        sn = sn+1
        check = bool(True)
if check is not True:
    print("There is no any country within the specified range")

# ---- end of Question 02 (h)