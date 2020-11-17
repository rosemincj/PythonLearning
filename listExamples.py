sampleList = [1,2,3,4,5]
print(sampleList[4])
print(sampleList[-4])
print(sampleList[1:3])
sampleList[4] = 10
print(sampleList)
sampleList.append(12)
print(sampleList)
sampleList.extend([6,7])
print(sampleList)
sampleList.insert(0, 'xxx')
print(sampleList)
print(sampleList.index(3))
print(sampleList)
sampleList.remove('xxx')
print(sampleList)
sampleList.pop(1)
print(sampleList)

# Sum


def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers


print(sum_list([1,2,-8]))

# Largest num


def largest_num_in_list(list1):
    largestnum = list1[0]
    for a in list1:
        if a > largestnum:
            largestnum = a
    return largestnum


print(largest_num_in_list([1, 2, -8, 0]))

# If and For loop

sampleList1 = ['a','b','c','d','e']
if 'a' in sampleList1:
    print('yay')
for i in range(100):
    print(i)

# Sorting

print(sorted(sampleList))
print(sampleList)
strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs))
print(sorted(strs, reverse=True))
strs = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs, key=len))
print(sorted(strs, key=str.lower))

# For In Loop

nums = [1, 2, 3, 4]
squares = [n * n for n in nums]
print(squares)

