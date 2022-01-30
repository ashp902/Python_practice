str = "avinash bharath bcd"
#avinash,bharath
for word in str.split() :
    i = -1
    for x in range(len(word)) :
        if(word[x] == 'a') :
            i = x
            break
    if(i % 2 == 0) :
        print(word[::-1])
    else :
        print(word)


'''
    1    row = 0, row-1 = -1 range(-1,-1,-1) = []
   12 1  row = 1  row-1 = 0 range(0,-1,-1) = [0]
  123 21  row = 2 row-1=1 range(1,-1,-1) = [1 0]
 1234 321
12345 4321
n = 5

n = 4
   1 1
  12 21
 123 321
1234 4321
'''
n = 5
'''for row in range(n) :
    for col in range(row,-1,-1) :
        print(col+1, end = "")
    print()
'''
for row in range(n) :
    print(" " * (n - row + 1), end="")
    for col in range(row + 1) :
        print(col+1, end="")
    for col in range(row-1,-1,-1) :
        print(col+1, end="")
    print()

