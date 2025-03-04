"""
You are given positive integer number n. You should create such strictly increasing sequence of k positive numbers a_1, a_2, ..., a_{k}, that their sum is equal to n and greatest common divisor is maximal.

Greatest common divisor of sequence is maximum of such numbers that every element of sequence is divisible by them.

If there is no possible sequence then output -1.


-----Input-----

The first line consists of two numbers n and k (1 ≤ n, k ≤ 10^10).


-----Output-----

If the answer exists then output k numbers — resulting sequence. Otherwise output -1. If there are multiple answers, print any of them.


-----Examples-----
Input
6 3

Output
1 2 3

Input
8 2

Output
2 6

Input
5 3

Output
-1
"""

def max_gcd_sequence(n: int, k: int) -> list:
    """
    Create a strictly increasing sequence of k positive numbers with sum n and maximal GCD.
    
    Args:
        n: Sum of the sequence elements (1 ≤ n ≤ 10^10)
        k: Length of the sequence (1 ≤ k ≤ 10^10)
        
    Returns:
        List of k strictly increasing positive integers with sum n and maximal GCD,
        or [-1] if no such sequence exists
    """
    pass
