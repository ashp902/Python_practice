'''
string
i = 0 to len(string)
i += 1

reversed string
j = 0 to len(string)
j += 1

Welcome Yagna!
i = 0
!angaY emocleW
j = 0



while len(output) != len(string)
if(!str[i].isalnum())
output += str[i]
else:
    while(!rstr[j].isalnum())
        j += 1
    output += str[j]
i += 1


output = ""
'''


str = "Welcome Yagna!"
rstr = str[::-1]
output = ""
i = 0
j = 0


while(len(output) != len(str)) :
    if(not (str[i].isalnum())) :
        output += str[i]
    else :
        while(not rstr[j].isalnum()) :
            j += 1
        output += rstr[j]
        j += 1
    i += 1

print(output)

'''
x = [3,2,1]
print(sorted(x)) ==> 1 2 3
print(x) ==> 3 2 1
print(x.sort()) ==> None
print(x) ==> 1 2 3
'''

l = [["U1", "U2"], ["U3", "U4"], ["U5", "U1"], ["U2", "U1"], ["U4", "U3"]]
l2 = [sorted(x) for x in l]
output = []
for i in range(len(l2)) :
    x = l2[i]
    if(x not in output) :
        if(l2.count(x) > 1) :
            print(x)
            output.append(x)
        else :
            print(l[i])
            output.append(x)