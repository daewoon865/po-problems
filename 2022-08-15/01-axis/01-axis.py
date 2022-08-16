import sys

input = sys.stdin.readlines()
inputn = [int(i) for i in input]

T = inputn [0]
inputn = inputn[1:]


"""
1 -> 2
2 -> 2 + 2 + 1
3 -> 3 + 3 + 2 + 1
4 -> 4 + 4 + 3 + 2 + 1 
5 -> 5 + 5 + 4 + 3 + 2 + 1
index+index-(index-1) + prev
=> index+1 + prev
""" 

memo = dict()
memo[1] = 2

for i in range (2, 10000+1):
    memo[i] = i + 1 + memo[i-1]

for n in inputn:
    print (memo[n])
