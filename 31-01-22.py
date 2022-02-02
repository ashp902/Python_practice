'''

10-99

'''

n = input()
l = []
#for loop - numbers generated as strings
for i in range(10) :
    l.append(n + str(i))
    if(i != 0) :
        l.append(str(i) + n)
l = list(set(l)) # remove duplicates
m = [int(x) for x in l] # convert string to int
m.sort() #sorting
print(m)

n = 2
l=[]
for i in range(10,100) :
    if(str(n) in str(i)) :
        l.append(i)
print(l)

'''

filter words that are not same length
check by each char if char is not '_'
if all chars match, print word
else nothing


'''
list = ["geeks", "best", "peeks", "abcde"]
mesh = "_ee_s"

for word in list:
    if(len(word) != len(mesh)) :
        continue
    else :
        for j in range(len(word)):
            if(mesh[j] != "_") :
                if(mesh[j] != word[j]) :
                    break
        else :
            print(word, end = " ")

'''

int -> str -> list
matching removing
list -> str -> int

'''