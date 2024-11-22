age = int(input("Enter your age\n"))
if age==18:
    print("You are an adult")
elif age==19:
    print("bhg ja")
# elif age>19 | age <21:  #logical error 
elif age>19 and age<21:
    print("best h bhai")    
else:
    print("chla ja")        

# Loops

# for i in range(10):  # This loop will execute n-1 times for this case 0 to 9
#     print(i)

# for i in range(2,20):
#     print(i+1)  # This loop will execute n-1 times for this case 2 to 19

for i in range(2,20,2):
    print(i) # this loop will start from 2 to 20-1 and increment by 2, so output will be even numbers
    