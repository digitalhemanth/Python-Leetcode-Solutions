def find_twosum(Array, target):
    for i in range(len(Array)):
        for j in range(i + 1, len(Array)):
            if Array[i] + Array[j] == target:
                print(f'{Array[i]} + {Array[j]} = {target}')

find_twosum([1, 5, 3, 4, 7, 2, 9, 8], 12)
