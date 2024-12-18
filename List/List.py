# List is a liner structre(one by one)
a=[1,2,3,4,5]
print(type(a))
a.append(12)
print(a[1])
a.pop()
print(a)
len(a)

# itration in list
for i in range(len(a)):
    print(a[i])

      

# List slicing
c=[1,2,3,4,5,6,7,8,9]
# c[Start:End:Jump] Start will not include in the outout but end will be

print(c[1:5:])
print(c[::2])


x=eval(input("enter the number"))
for i in range(len(x)):
    print(x[i])

x.append(123123)    

print(x)


# Find whether the number is present in the array or not
x=[1,2,3,4,5,6]
y=int(input("enter the number you're looking for"))


for i in range(len(x)):
    if(x[i]==y):
        print("number found at index",i)
        break
   
else:
    print("number not found")