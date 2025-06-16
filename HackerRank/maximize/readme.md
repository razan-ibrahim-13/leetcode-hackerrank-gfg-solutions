# Maximize It! - HackerRank

**Platform:** HackerRank  
**Difficulty:** Medium  
**Topic:** Mathematics, Optimization  
**Date Solved:** 2025-06-16

## Problem Link
[Maximize It! - HackerRank](https://www.hackerrank.com/challenges/maximize-it/problem)

## Problem Statement

You are given K lists, each of size N. You have to pick one element from each list such that the value from the equation below is maximized:

S = (a₁² + a₂² + ... + aₖ²) % M

Where aᵢ is the element picked from the i-th list.

## Input Format

- The first line contains 2 space separated integers K and M.
- The next K lines each contains an integer Nᵢ, denoting the number of elements in the i-th list, followed by Nᵢ space separated integers denoting the elements in the list.

## Constraints

- 1 ≤ K ≤ 7
- 1 ≤ M ≤ 1000
- 1 ≤ Nᵢ ≤ 7
- 1 ≤ Magnitude of elements in list ≤ 10⁹

## Output Format

Output a single integer denoting the value Sₘₐₓ.

## Sample Input
```
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
```

## Sample Output
```
206
```

## Explanation

Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list gives the maximum S value equal to (5² + 9² + 10²) % 1000 = 206.

## Approach

Since we want to maximize the sum of squares, and squaring preserves order for positive numbers, we should pick the largest element from each list.

## Time Complexity
- O(K × max(Nᵢ)) where K is number of lists and max(Nᵢ) is the size of largest list

## Space Complexity
- O(max(Nᵢ)) for storing each list

## Tags
- Mathematics
- Greedy
- Array Processing