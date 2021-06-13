# test14.py

# filetest.txt 의 데이터를 역순으로 정렬하여 바꾸기

fo = open("fileTest.txt","r")

lists = fo.readlines()

fo.close()

print(lists)
lists.reverse()
print(lists)

fo2 = open("fileTest.txt","w")

for i in lists:
    fo2.write(i)

fo2.close()