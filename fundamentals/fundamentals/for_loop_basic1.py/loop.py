#1
for i in range (151):
    print(i)

#2
for i in range(5 , 1001, 5):
    print(i)

#3
for i in range(1, 101):
    if i % 10 == 0:
        print( i ,"Coding Dojo")
    elif i % 5 ==0:
        print(i, "Coding")
    else :
        print(i)

#4
odd_sum = sum(i for i in range(1, 500001, 2))
print("Final sum:" , odd_sum)

#5
for i in range(2018, 0 ,-4):
    print(i)

#6
lowNum = 2
highNum = 9
mult = 3

for i in range (lowNum , highNum  +1):
    if i % mult ==0:
        print(i)