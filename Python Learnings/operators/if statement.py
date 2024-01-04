#if statement =  block of code hat will execute if it's condition s true#

age = int(input("How old are you?:"))

if age == 100:
    print("You're a century old")

elif age >=18:
    print("You're an adult")
elif age < 0:
    print("You're not born yet")

else:
    print("You're a child")
