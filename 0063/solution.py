"""
You are given an array a of n integers and an integer k. Let's define the following function:

f(l, r) = (a_l · a_{l+1} · ... · a_r) mod k

Your task is to find the number of pairs (l, r) such that 1 ≤ l ≤ r ≤ n and f(l, r) = 0.


-----Input-----

The first line contains two integers n and k (1 ≤ n ≤ 10^5, 2 ≤ k ≤ 10^5) — the length of the array and the modulo.

The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^5) — the elements of the array.


-----Output-----

Print one integer — the number of pairs (l, r) such that 1 ≤ l ≤ r ≤ n and f(l, r) = 0.


-----Examples-----
Input
5 10
1 2 3 4 5

Output
4

Input
3 6
3 2 1

Output
3

Input
5 7
1 10 7 2 4

Output
2
"""

def count_zero_product_pairs(n: int, k: int, array: list) -> int:
    """
    Count the number of pairs (l, r) such that the product of elements from l to r is divisible by k.
    
    Args:
        n: Length of the array (1 ≤ n ≤ 10^5)
        k: Modulo (2 ≤ k ≤ 10^5)
        array: List of n integers (1 ≤ a_i ≤ 10^5)
        
    Returns:
        Number of pairs (l, r) such that f(l, r) = 0
    """
    pass
