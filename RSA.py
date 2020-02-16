#from time import time
def powermod1(a, b, n):
    return a**b%n

list1=[10,7,58,30,23,62 ,7,64,62,23,62,61,7,41,62,21,7,49,75,7,69,53,58,37,37,41,10,64,50,7,10,64,21,62,61,35,62,61,62,7,52,10,21,58,7,49,75,7,62,26,22,53,30,21,10,37,64]
list2=[]

for elem in list1:
    list2.append(elem**37%77)
print(list2)

for elem in list2:
    if (elem+63)==91:
        print(" ",end = "")
    else:
        print(chr(elem+63),end ="")
