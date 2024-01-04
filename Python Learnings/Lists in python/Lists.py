# List = used to store multiple items in a single variable #

food = ["pizza", "biriyani", "sandwich", "Thai wings"]
food[0] = "Dosa" # you can update the element anytime#
print(food[0])

food.append("idly")#use append to add the element at the end of the list#
food.remove("sandwich")
food.pop()# it automatically removes the last element#
food.insert(0,"cake")
food.sort()# this will sort a food alphabatically#
food.clear()
for x in food:
    print(x)