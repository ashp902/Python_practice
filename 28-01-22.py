'''def permutations(list, perm='') :
    if(len(l) == 0) :
        print(perm)
    else :
        for i in range(len(l)) :
            permutations(l[:i] + l[i+1:], perm + l[i])


permutations(['1','2','3'])
	       0   1   2
1 2 3
1 3 2

1 - (2,3)'''

'''
permutation(['1','2','3'])
(i = 0) - (l[0:0] + l[1:3] = [] + ['2','3'] = ['2','3']), (perm + l[i] = '' + '1' = '1')

		permutations([2,3], '1')
		(i = 0) - (l[0:0] + l[1:2] = [] + [
		


l= [1,2,3,4,5]
    0,1,2,3,4
l[2:4]
2,3
'''










































from lib2to3.refactor import get_fixers_from_package
import string

'''
string starting char - 1 char - 1 length substring
string[:1]


1 - 
2 - strating char - 2 char - 2 length substring
string[:2]

3 - string[:3]
4
...
len(str)

g
gf
gfg
gfgg
gfggf

'''




'''def rep(str) :
    for i in range(1, len(str)) :
        substr = str[:i]
        n = len(str) // len(substr)
        if(substr*n == str) :
            return [substr] * n


print(rep('gfggfggfggfggfggfggfg'))'''


n = 5

# row - 0 1 2 3 4
for row in range(n) :
    print(" " * (n - (row + 1)), end = '')
    print("* " * (row + 1), end = '')
    print()

#row - 4 3 2 1 0
for row in range(n-1, -1, -1) :
    print(" " * (n - (row + 1)), end = "")
    print("* " * (row + 1), end= '')
    print()


'''
    # 0 1
   ## 1 2
  ### 2 3
 ####
#####
input = 5
'''

n = 5
for row in range(n) :
    print(" " * (n - row + 1), end = '')
    print('*' * (row + 1), end = '')
    print()

'''
range(5) - 0 1 2 3 4
    1 0 range(1) = [0] => 
   12 1 range(2) = [0 1]
  123 2 range(3) = [0 1 2]
 1234 3 
12345

input 5
'''

n = 5
for row in range(n) :
    print(" " * (n - row + 1), end = '')
    for column in range(row + 1) :
        print((column + 1), end= '')
    print()

'''
1
12
123
1234
12345

12 34 56 78 ...
row 1 - group1 - [1 2]
row 2 - group2 - [1 2 3 4]

1 row0 range((row + 1) * 2) = range(2) [0 1] start from 1, end at last element of range, step = 2
13 row1 range((row + 1) * 2) = range(4) [0 1 2 3] start from 1, end at 3, step = 2
135
1357
13579
input 5
'''

for row in range(n) :
    for col in range(1,(row + 1) * 2,2) :
        print(col,end='')
    print()

'''
    1
   121
  12321
 1234321
123454321

n = 5
'''





'''

x = 5

for i in range(x) :
    print(' ' * (x - i - 1), end ='')
    print('* ' * (i + 1), end = '')
    print()
for i in range(x-1, -1, -1) :
    print(' ' * (x - i - 1), end ='')
    print('* ' * (i + 1), end = '')
    print()

'''
'''

  *
 * *
* * *

'''