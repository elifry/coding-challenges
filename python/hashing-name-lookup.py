# Perfect Pair
# Topic: Hashing
# Website: hackerearth
# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/
# Result: Accepted
# Time: 0.520000 sec
# Memory: 18036 KiB

# Capture inputs
# The first line contains a single integers N denoting the number of Monk's colleagues.
numColleagues = int(input())

# Each of the next N lines contains an integer and a String denoting the roll number and name of the i th colleague of Monk.
colleagues = {}
for i in range(numColleagues):
    valuePair = input().split()
    colleagues[int(valuePair[0])] = valuePair[1]

# The next Line contains a single integer q denoting the number of queries Monk shall present to you when he starts teaching in class.
numQueries = int(input())

# Each of the next q lines contains a single integer x denoting the roll number of the student whose name Monk wants to know.
for i in range(numQueries):
    print(colleagues[int(input().strip())])
