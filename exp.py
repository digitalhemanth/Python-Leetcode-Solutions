def ints(x,y,arry) ->int:
    sum = 0
    for i,j in enumerate(arry):
        if i>=x and i<=y:
            print(j)
            sum = j+sum
    return sum

arry = [10,20,30,40,50,60]
x=2
y=4

print(ints(x,y,arry))
