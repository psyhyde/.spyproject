# -*- coding: utf-8 -*-
gro = ['cereal', 'milk', 'starcrunch', 'beer', 'duck tape', 'lotion']
indexx = 0
temp = len(gro) - 1
for   indexx, temp in enumerate(gro):
    print(indexx, gro[indexx])
    indexx += 1

#!/usr/bin/python

aList = [123, 'xyz', 'zara', 'abc', 123];

print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))