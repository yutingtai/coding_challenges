#!python3

import functools

def f(x):
   if x in "13579": return 3
   elif x in "02468": return 4
   elif x.isupper(): return 2
   else: return 1
   return 0

print(functools.reduce(lambda acc,s:acc+s,sorted(input(),key=lambda x:[f(x),x])))