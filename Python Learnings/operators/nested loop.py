# Nested loop = The inner loop will finish all of it's iterations before finishing one ieteration of the outter loop#

rows = int(input("How many rows?: ")) # it will be incharge for outter lopp#
columns = int(input("How many columns?: ")) # it will takecare of inner loop#
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()