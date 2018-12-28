
countries=[]   # empty list
fhandle = open("countries.txt", 'r')
for country in fhandle:
    countries.append(country.rstrip())  # add country to a list remove \n at the end
# (b) display all countries which end with nia
    if (country.lower()).endswith("nia\n"):
        print(country.rstrip(), end=', ')
print('\n')  # Break line for next output

# (a) displays the number of countries in the file
print("There are {} countries in the list".format(len(countries)))
print('\n')

# (c) display all countries which contain -nga
for country in countries:
    if 'nga' in country.lower():
        print(country.rstrip(), end=', ')

# (d) display country name and its position
name = input("\n\nEnter the name of the country you wish to search for: \n")
check = bool(False)
for country in countries:
    if country.lower() == name.lower():
        print("Country name is {} and position is {}".format(name, countries.index(country)+1))
        check = bool(True)
        break
if check is not True:
    print("This country does not exist in the list")

# (e) append a new country at the end of the list
new_country = input("\nEnter the name of the new country: \n")
countries.append(new_country)

# (f) remove a specified country from the list
remove_country = input("\nEnter the name of the country you wish to remove: \n")
check = bool(False)
for country in countries:
    if country.lower() == remove_country.lower():
        countries.pop(countries.index(country))
        check = bool(True)
        break
if check is not True:
    print("This country does not exist in the list")

# (g) Display countries which have more than one word
for country in countries:
    if " " in country.lower():   # countries with more than one name basically have space as a substring.
        print("\n",country.rstrip(), end=', ')
print('\n')

# (h) Display countries in four columns
print("-Line 1- -Line 2- -Line 3- -Line 4-")
i = 0
for country in countries:
        print(country.rstrip(), end=" ")
        i=i+1
        if i % 4 == 0:
            print("\n")  # if i is a multiple of 4 break a line to start a new row.


# OUTPUT

# Lithuania, Macedonia, Mauritania, Romania, Slovenia, Tanzania,

# There are 117 countries in the list


# Hungary, Singapore, Tonga,

# Enter the name of the country you wish to search for:
# Uganda
# Country name is Uganda and position is 106

# Enter the name of the new country:
# Ulaya

# Enter the name of the country you wish to remove:
# Ulaya

# Holy See,
# Hong Kong,
# Korea, North,
# Korea, South,
# Marshall Islands,
# New Zealand,
# North Korea,
# Papua New Guinea,
# San Marino,
# Sao Tome and Principe,
# Saudi Arabia,
# Sierra Leone,
# Sint Maarten,
# Solomon Islands,
# South Africa,
# South Korea,
# South Sudan,
# Sri Lanka,
# Trinidad and Tobago,
# United Arab Emirates,
# United Kingdom,

# -Line 1- -Line 2- -Line 3- -Line 4-
# Haiti Holy See Honduras Hong Kong

# Hungary Jamaica Japan Jordan

# Kazakhstan Kenya Kiribati Korea, North

# Korea, South Kosovo Kuwait Kyrgyzstan

# Laos Latvia Lebanon Lesotho

# Liberia Libya Liechtenstein Lithuania

# Luxembourg Macau Macedonia Madagascar

# Malawi Malaysia Maldives Mali

# Malta Marshall Islands Mauritania Mauritius

# Mexico Micronesia Moldova Monaco

# Mongolia Montenegro Morocco Mozambique

# Namibia Nauru Nepal Netherlands

# New Zealand Nicaragua Niger Nigeria

# North Korea Norway Oman Pakistan

# Palau Panama Papua New Guinea Paraguay

# Peru Philippines Poland Portugal

# Qatar Romania Russia Rwanda

# Samoa San Marino Sao Tome and Principe Saudi Arabia

# Senegal Serbia Seychelles Sierra Leone

# Singapore Sint Maarten Slovakia Slovenia

# Solomon Islands Somalia South Africa South Korea

# South Sudan Spain Sri Lanka Sudan

# Suriname Swaziland Sweden Switzerland

# Syria Taiwan Tajikistan Tanzania

# Thailand Timor-Leste Togo Tonga

# Trinidad and Tobago Tunisia Turkey Turkmenistan

# Tuvalu Uganda Ukraine United Arab Emirates

# United Kingdom Uruguay Uzbekistan Vanuatu

# Venezuela Vietnam Yemen Zambia

# Zimbabwe