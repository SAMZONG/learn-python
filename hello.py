# -*- coding: utf-8 -*-

L = ['Bart','Lisa','Adam']

for name in L:
	print('Hello %s' % name)

def power(x):
    return x*x

def power2(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
def power3(x,n=2):
    s = 1
    while n >  0:
        n = n -1
        s = s * x
    return s

print(power(5))
print(power2(5,3))
print(power3(5))

print([x * x for x in range(1,11)])

print([x * x for x in range(1,11) if x % 2 == 0])

print([m+n for m in 'ABC' for n in 'XYZ'])
print([m+n+o for m in 'ABC' for n in 'XYZ' for o in 'IJK'])

import os

print([d for d in os.listdir('.')])

L = ['Hello','Apple','IBM','DELL',18,None]


print([s.lower() if isinstance(s, str)else s for s in  L])