#logical operators(and,or, not) = used to check if two or more conditional statements are true#

temp = int(input("what's today's temperature outside?: "))

#if temp >= 0 and temp <= 30: #for and statements both the conditions must be true#
   # print("The temperature is alright!")
   # print("You can go outside!")#

#elif temp < 0 or temp > 30: # for or statements one the condition must be true#
    #print("The temperature is bad today!")
    #print("Stay indoors!")#
    
if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today!")
    print("Stay indoors!")

elif not(temp < 0 or temp > 30):
    print("The temperature is alright!")
    print("You can go outside!")