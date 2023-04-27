import numpy

N,M = input().split()
a = [[int(x) for x in input().split()] for _ in range(int(N))]
b = [[int(x) for x in input().split()] for _ in range(int(N))]

A = [list(map(int,input().split())) for i in range(int(N))]
B = [list(map(int,input().split())) for i in range (int(N))]

print(a,b,A,B,sep='\n')