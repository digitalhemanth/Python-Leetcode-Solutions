for i in range(1,100):
    if i%15==0:
        print('FizBuz',end=' ')
    if i%3==0:
        print('Fiz', end=' ')
        continue
    if i%5==0:
        print('Buz',end=' ')
    else:
        print(i,end=' ')
        
        
'''
PS D:\Code_Place\2_test> python .\FizBuz.py   
1 2 Fiz 3 4 5 Fiz 6 7 8 Fiz 9 10 11 Fiz 12 13 14 Fiz 15 16 17 Fiz 18 19 20 Fiz 21 22 23 Fiz 24 25 26 Fiz 27 28 29 Fiz 30 31 32 Fiz 33 34 35 Fiz 36 37 38 Fiz 39 40 41 Fiz 42 43 44 Fiz 45 46 47 Fiz 48 49 50 Fiz 51 52 53 Fiz 54 55 56 Fiz 57 58 59 Fiz 60 61 62 Fiz 63 64 65 Fiz 66 67 68 Fiz 69 70 71 Fiz 72 73 74 Fiz 75 76 77 Fiz 78 79 80 Fiz 81 82 83 Fiz 84 85 86 Fiz 87 88 89 Fiz 90 91 92 Fiz 93 94 95 Fiz 96 97 98 Fiz 99 
PS D:\Code_Place\2_test> python .\FizBuz.py
1 2 Fiz 4 5 Fiz 7 8 Fiz 10 11 Fiz 13 14 Fiz 16 17 Fiz 19 20 Fiz 22 23 Fiz 25 26 Fiz 28 29 Fiz 31 32 Fiz 34 35 Fiz 37 38 Fiz 40 41 Fiz 43 44 Fiz 46 47 Fiz 49 50 Fiz 52 53 Fiz 55 56 Fiz 58 59 Fiz 61 62 Fiz 64 65 Fiz 67 68 Fiz 70 71 Fiz 73 74 Fiz 76 77 Fiz 79 80 Fiz 82 83 Fiz 85 86 Fiz 88 89 Fiz 91 92 Fiz 94 95 Fiz 97 98 Fiz 
PS D:\Code_Place\2_test> python .\FizBuz.py
1 2 Fiz 4 Buz Fiz 7 8 Fiz Buz 11 Fiz 13 14 Fiz 16 17 Fiz 19 Buz Fiz 22 23 Fiz Buz 26 Fiz 28 29 Fiz 31 32 Fiz 34 Buz Fiz 37 38 Fiz Buz 41 Fiz 43 44 Fiz 46 47 Fiz 49 Buz Fiz 52 53 Fiz Buz 56 Fiz 58 59 Fiz 61 62 Fiz 64 Buz Fiz 67 68 Fiz Buz 71 Fiz 73 74 Fiz 76 77 Fiz 79 Buz Fiz 82 83 Fiz Buz 86 Fiz 88 89 Fiz 91 92 Fiz 94 Buz Fiz 97 98 Fiz 
PS D:\Code_Place\2_test> python .\FizBuz.py
1 2 Fiz 4 Buz Fiz 7 8 Fiz Buz 11 Fiz 13 14 FizBuz Fiz 16 17 Fiz 19 Buz Fiz 22 23 Fiz Buz 26 Fiz 28 29 FizBuz Fiz 31 32 Fiz 34 Buz Fiz 37 38 Fiz Buz 41 Fiz 43 44 FizBuz Fiz 46 47 Fiz 49 Buz Fiz 52 53 Fiz Buz 56 Fiz 58 59 FizBuz Fiz 61 62 Fiz 64 Buz Fiz 67 68 Fiz Buz 71 Fiz 73 74 FizBuz Fiz 76 77 Fiz 79 Buz Fiz 82 83 Fiz Buz 86 Fiz 88 89 FizBuz Fiz 91 92 Fiz 94 Buz Fiz 97 98 Fiz 
PS D:\Code_Place\2_test> 
'''