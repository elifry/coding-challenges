# Perfect Pair
# Topic: Hashing
# Website: hackerearth
# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/perfect-pair-df920e90/description/
# Result: Accepted
# Time: 1.800000 sec
# Memory: 16068 KiB

import math

def getPerfectPairCount(numbers: list, n: int) -> int:
    # print('There are {} numbers in this case and the numbers are {}'.format(n, numbers))

    # Make a list of all the possible squares and cubes
    # A(N) max is 1000, sum max is 2000, so smallest values 45^2 > 2000 and 13^3 > 2000
    possibleSquaresAndCubes = {
        *[i**2 for i in range(1, 45)],
        *[i**3 for i in range(1, 13)]
    }
    # print('The list of possible squares and cubes: {}'.format(possibleSquaresAndCubes))

    # Make a dictionary for the number of times each number shows up
    numberFrequencies = {}
    for i in numbers:
        if i in numberFrequencies:
            numberFrequencies[i]+=1
            continue
        numberFrequencies[i]=1
    # print('Frequency of numbers: {}'.format(numberFrequencies))

    # keep tally of each perfect number, this number is double the amount of perfect pairs since it increments for each of the numbers in the pair
    numPerfectPairsDoubled = 0

    # Go through whole list of possible squares and cubes
    for squareOrCube in possibleSquaresAndCubes:
        # For each number, see if it is a component in a square or cube
        for number, count in numberFrequencies.items():
            # Find the complement of the number we are looking at
            complement = squareOrCube - number

            # Negative: not valid, the square or cube we are looking up is too low
            if complement < 0:
                continue

            # Positive but the other half is not found so cant be a square or cube
            if complement not in numberFrequencies:
                continue

            # Equal: we got a double number, but we need to handle this
            # separately since we would count it twice otherwise
            if complement == number:
                # Count will be one higher than normal, since we have two of them
                numPerfectPairsDoubled += (count-1) * count
                continue

            # Finally, Positive, and in numberFrequencies. This is a perfect number
            # that is not a double
            numPerfectPairsDoubled += count * numberFrequencies[complement]

    # Get back down to the number of perfect pairs
    return numPerfectPairsDoubled//2

if __name__ == "__main__":
    cases = int(input())
    # print("Total Cases {}".format(cases))
    for case in range(cases):
        n = int(input())
        # print("{} Case has {} numbers".format(case+1, n))
        numbers = [int(i) for i in input().split()]
        print(getPerfectPairCount(numbers, n))
