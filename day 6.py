#1 Done

#2

print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)

a=20
a+=30
a%=3
print(a)

print(True * False)
print(True and False)
print(True & False)

print((6>3) and (7>4) or (18==3)) and (9>3)

print(True is False)
#print(False in 'False')

print((True==False) or (False > True)) and (False <=True)

#3

s1 = "Nice to have it"
s2 = "here"

print(" ".join([s1,s2]))

#4 
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

#5
print([s1] + a + [s2])

#6
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1 - color_list_2)

#7
from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
strng=input("Enter string:")
if(check(strng)==True):
      print("The string is a pangram")
else:
      print("The string isn't a pangram")



#8

print(eval('{0} + {0}{0} + {0}{0}{0}'.format(input())))

#9

print(','.join(sorted(input().split(','))))

#10

d =  {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
print(d['Student'][d['Marks'].index(max(d['Marks']))])