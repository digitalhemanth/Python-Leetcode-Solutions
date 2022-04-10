def ints(x,y,arry) ->int:
    sum = 0
    for i in range(arry(arry[x],arry(arry[y]))):
        sum = i+sum
    return sum

arry = [10,20,30,40,50,60]
x=2
y=4

print(ints(x,y,arry))