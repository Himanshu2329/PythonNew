# age = int(input("Enter your age\n"))
# if age==18:
#     print("You are an adult")
# elif age==19:
#     print("bhg ja")
# # elif age>19 | age <21:  #logical error 
# elif age>19 and age<21:
#     print("best h bhai")    
# else:
#     print("chla ja")        

# Loops

# for i in range(10):  # This loop will execute n-1 times for this case 0 to 9
#     print(i)

# for i in range(2,20):
#     print(i+1)  # This loop will execute n-1 times for this case 2 to 19

# for i in range(2,20,2):
#     print(i) # this loop will start from 2 to 20-1 and increment by 2, so output will be even numbers

# number  = int(input("Enter your number"))

# for i in range(1,11):
#     # print(str(number) + " X " + str(i) + " = " + str(i * number))
#     print(f"{number} X {i} = {i * number}")

for i in range(100,0,-1):
    print(i)    

# for i in range(1,101):
#     if i%3==0 :
#         print(f"{i} foo")
#     elif i%5==0:
#         print(f"{i} bar")        

for i in range(0,100):
    if not i%3 and not i%5:
        print(f"{i} foo bar")
    elif not i%3:
        print(f"{i} foo")
    elif not i%5:
        print(f"{i} barr")    


# while loop
start = 1
end = 10
while(start<=end):
    print(start)
    start+=1