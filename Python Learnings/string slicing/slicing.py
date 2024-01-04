#slicing = create a substring by extracting elements from another string#
#we can use either of thr operator indexing [] or slice()#
#so with slicing there are three optional arguments, depends on where and how we want to slice the string[start:stop:step]#

#indexing#
name = "Aneesha Gorantla"
first_name = name[:7]
last_name = name[8:]
middle_name = name[0:16:3]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(middle_name)
print(reversed_name)

#slice#
website = "https://docs.python.org/3/tutorial/index.html"

slice = slice(13,-22 )

print(website[slice])