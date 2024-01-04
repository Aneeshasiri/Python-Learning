#Multi Assign#

name, age, beauty = "Aneesha", 25, True
print(name, age, beauty)
print(name)
print(age)
print(beauty)

#same value for every variable#
Aneesha = Maneesha = Mom = 25
print(Aneesha)
print(Maneesha)
print(Mom)

#String methods#
name = "aneesha"

print(len(name))# finds length of the variable given#
print(name.find("a"))#finds the letter a place in the whole word#
print(name.capitalize())# it will give you th ecapital letter for the first letter of the word#
print(name.upper())#it will change the whole word into capital letters#
print(name.lower())# it will change the wholw word to lower letter#
print(name.isdigit())# it will give boolean value, if the variable value have numbers it gives true, if there is a string it's gonna give false#
print(name.isalpha())#you can alpha method to check if the str has alphabetical letters or not#
print(name.count("e"))# we can count how many characters are in the string(var)#
print(name.replace("e" , "i"))#it replaces the letters, first letter should be the present value in the str and the second valuse should be teh desire value#
print(name*7)#it print your var as many times as you want by using *with any number#
