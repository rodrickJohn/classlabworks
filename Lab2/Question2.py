

class PersonName:

    #this code is missing an input validation, ideally names should not have special characters

    firstname = str(input("Enter First Name: \n"))
    middlename = str(input("Enter Middle Name: \n"))
    surname = str(input("Enter Surname: \n"))

    def full_name(self):
        return self.firstname+ " "+self.middlename+" "+ self.surname

    def vowel_counter(self):
        fullname = name.firstname + name.middlename + name.surname
        x= [char for char in fullname if char in ['a','e','i','o','u']]
        return len(x)

    def check_la(self):
        full_name = name.firstname + name.middlename + name.surname          #program will check for any string -la- in a full name string.
        la_var=bool(False)                                                   #create a truth holder variable
        for i in range(len(full_name)):
            if (full_name[i]=='l' and full_name[i+1]=='a'):
                la_var=bool(True)
                break
        return la_var

name = PersonName()
print("Entered name is: ", name.firstname+" "+name.middlename+" "+name.surname)
print("First name is: ", name.firstname)
print("Middle name is: ", name.middlename)
print("Last name is: ", name.surname.upper())
print("Abbreviated name: ", name.surname.upper()+', '+ name.firstname[0]+'.'+name.middlename[0])
print("Number of vowels in the name is ", name.vowel_counter())
print("Name contains substring -la- ", name.check_la())

