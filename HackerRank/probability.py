# The input consists of three lines. The first line contains the integer N , denoting the length of the list. The next line consists of N space-separated lowercase English letters, denoting the elements of the list.

# The third and the last line of input contains the integer K , denoting the number of indices to be selected.

import math

n = int(input())
arr = input().split()
k = int(input())

# Count how many elements are not 'a'
non_a_count = sum(1 for x in arr if x != 'a')

# If k > non_a_count, choosing k without picking 'a' is impossible
if k > non_a_count:
    print(1.0)
else:
    total_ways = math.comb(n, k)
    good_ways = math.comb(non_a_count, k)
    probability = 1 - (good_ways / total_ways)
    print(round(probability, 4))
 
