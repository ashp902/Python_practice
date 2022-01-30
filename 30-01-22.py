'''

2n + 1
1st 2(0) + 1
2nd 2(1) + 1
3rd 2(2) + 1

n = 7

      #             0 row=0 2*(-1) + 1 = -1
     # #            1 row=1 2(1-1) + 1 = 1
    #   #           3 row=2 2(2-1) + 1= 3
   #     #          5
  #       #         7
 #         #        9
#############       13

spaces --> n - (row + 1)
print one char
spaces --> 2 * (row - 1) + 1
if row != 0 print one char

print char --> 2 * n -1

n = 6

     #
    # #
   #   #
  #     #
 #       #
###########         11




















'''

n=7
for i in range(n-1) :
    print(" " * (n-(i+1)),end='')
    print("#",end='')
    print(" "*((i-1)*2 + 1),end='')
    print("#" if i else "",end='')
    print()
print('#'*(2*n-1))

'''
n = 6

     #          0
    # #         1
   #   #        2
  #     #       3
 #       #      4
#         #     5
 #       #      4
  #     #       3
   #   #        2
    # #         1
     #          0

row (0,n-1) range(0,n)
spaces --> n - (row + 1)
print one char
spaces --> 2 * (row - 1) + 1
if row!=0 print one char

row (n-2,0,-1) range(n-2,-1,-1)



















     
'''

for i in range(n) :
    print(" "*(n-(i+1)),end='')
    print("#",end='')
    print(" "*((i-1)*2 + 1),end='')
    print("#" if i else "",end='')
    print()
for i in range(n-2,-1,-1):
    print(" "*(n-(i+1)),end='')
    print("#",end='')
    print(" "*((i-1)*2 + 1),end='')
    print("#" if i else "",end='')
    print()