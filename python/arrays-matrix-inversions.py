t = int(input()) # number of cases
m = [] # "matrix" setup
p1 = 0 # pointer for x
p2 = 0 # pointer for y

# loop for each test case
for case in range(t):
    n = int(input()) # matrices are N x N
    # maxN = n*n
    inv = 0 # How many inversions there are
    m = [None]*n*n

    # Process each line as an array of integers, linearly
    lineNums = []
    for line in range(n):
        lineNums += [int(i) for i in input().split()]

    # insert each number in order into the "matrix"
    for num in lineNums:
        current = p1+(n*p2)
        print(current)
        # print(m)

        # If the current space is empty, its the first one so insert it
        if m[current] == None:
            m[current] = num
            continue

        # If current is less than the number we are inserting, continue on
        if m[current] < num:
            # print('YES')
            if (p1>0) and (p1%n == 0):
                print('Divides evenly')
                # p2 += 1
                # p1 = 0
                # p1 += 1
            else:
                # p1 += 1
                # p2 += 1
                # p1 = 0
                print('Divides evenly')


    # print(inv)
    print(m)
    # print(lineNums)






            # stillInserting = True
            #
            # while(stillInserting):
            #     # If the current space is empty, its the first one so insert it
            #     if m[current] == None:
            #         m[current] = num
            #         stillInserting = False
            #
            #     # If current is less than the number we are inserting, continue on
            #     if m[current] < num:
            #         if p1%n == 0:
            #             p2 += 1
            #             p1 == 0
            #         else:
            #             p1 += 1
