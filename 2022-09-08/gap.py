def largestGap (li: list[int]):
    s, l = float('inf'), float('-inf')

    for i in li:
        if i < s:
            s = i
        if i > l:
            l = i

    return l - s

print(largestGap([3, 10, 6, 7]))
print(largestGap([-3, -1, 6, 7, 0]))

print(largestGap([1, 0]))
print(largestGap([0, 0]))
print(largestGap([-1, 0]))
print(largestGap([-1, -1]))
print(largestGap([1, 1]))
print(largestGap([3, 3, -1, -1]))
print(largestGap([3, 3, 2, 2]))
