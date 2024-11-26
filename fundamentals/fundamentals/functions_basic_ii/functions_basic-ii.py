#1 count down

def countdown(x):
    while x >= 0 :
        print (x)
        x=x-1

countdown(2)

#2 print and return
def print_and_return(list):
    print(list[0])
    return print(list[1])
print_and_return([5,3])

#3 first plus length
def first_plus_length(lst):
    print(lst[0]+ len(lst))
first_plus_length([1,2,3])

#4 greater
def greater(lt):
    result = []
    for i in range (0, len(lt)):
        if lt[i]> lt[1]:
            result.append(lt[i])
    if len(result)<2 :
        return False
    print(result)
greater([5,2,3,2,1,4])

#5 this length that value
def size(llt):
    result2 = []
    for i in range(1 , llt[0]+1):
        result2.append(llt[1])
    print(result2)
size([4,3])