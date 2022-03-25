from re import M


My_list = [6,1,3,1,9,6,0,1,7,7]
li = []

for i in My_list:
    if i not in li:
        li.append(i)
    else:
        print(i,end=' ')