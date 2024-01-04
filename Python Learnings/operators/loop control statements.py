# Loop control statements = change a loops execution rom its normal sequence #
# Break = used to terminate the loop entirely#
# continue = skips to the next iteration of the loop#
# Pass = does nothings, acts as placeholder#

while True:
    name= input("Enter your name: ")
    if name != "":
        break

#phone_number = "012-345-6789"

#for i in phone_number:
    #if i == "-":
        #continue
    #print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)


