#Insert User Variables
sum1 = input("Type In First Value: ")
sum2 = input("Type In Second Value: ")

#Computation
sumtotal = float(sum1) + float(sum2)

#Display
#.format is a fucntion use to add placeholder when printing a text to have a more professional print output.
print('The sum of {0} and {1} is {2}'.format(sum1, sum2, sumtotal))

#Possible Other Display Output
#print(f"The sum of {sum1} and {sum2} is {sumtotal}")

#Other Simplified Process In Doing This is:
#sum1 = 1
#sum2 = 2
#add = sum1 + sum2
#print(f"The Sum Is: {add}" )
