# Problem: Closest Prime Numbers in Range - https://leetcode.com/problems/closest-prime-numbers-in-range/

from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [1] * (right + 1)
        primes[0] = primes[1] = 0

        # Sieve of Eratosthenes
        for i in range(2, int(right**0.5) + 1):
            if primes[i]:
                for j in range(i * i, right + 1, i):
                    primes[j] = 0

        ans = [-1, -1]
        last_prime = -1

        for num in range(left, right + 1):
            if primes[num]:
                if last_prime != -1: 
                    if ans[0] == -1 or (num - last_prime < ans[1] - ans[0]):
                        ans = [last_prime, num]
                last_prime = num

        return ans