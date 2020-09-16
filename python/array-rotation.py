# Monk and Rotation
# Topic: Arrays & Strings
# Website: hackerearth
# https://www.hackerearth.com/challenges/competitive/codemonk-arrays-strings/algorithm/monk-and-rotation-3/
# Result: Accepted
# Time Limit: 1.0 sec(s) for each input file.
# Memory Limit:	256 MB

import collections

# The first line will consists of one integer T denoting the number of test cases.
t = int(input())

for i in range(t):
    # For each test case:
    # 1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
    nk = [int(i) for i in input().split()]
    n = nk[0]
    k = nk[1]

    # 2) The next line consists of N space separated integers , denoting the elements of the array A.
    # By setting max length, it will automatically cut off the opposite end when you add to one end.
    a = collections.deque([int(i) for i in input().split()], maxlen=n)

    # Do the rotates to the array
    for j in range(k):
        a.appendleft(a[n-1])

    print(*a)
