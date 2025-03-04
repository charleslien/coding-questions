"""
You are given the array of integer numbers a_0, a_1, ..., a_{n} - 1. For each element find the distance to the nearest zero (to the element which equals to zero). There is at least one zero element in the given array.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 2·10^5) — length of the array a. The second line contains integer elements of the array separated by single spaces ( - 10^9 ≤ a_{i} ≤ 10^9).


-----Output-----

Print the sequence d_0, d_1, ..., d_{n} - 1, where d_{i} is the difference of indices between i and nearest j such that a_{j} = 0. It is possible that i = j.


-----Examples-----
Input
9
2 1 0 3 0 0 3 2 4

Output
2 1 0 1 0 0 1 2 3 
Input
5
0 1 2 3 4

Output
0 1 2 3 4 
Input
7
5 6 0 1 -2 3 4

Output
2 1 0 1 2 3 4
"""

def distance_to_nearest_zero(n: int, array: list) -> list:
    """
    Calculate the distance from each element to the nearest zero in the array.
    
    Args:
        n: Length of the array (1 ≤ n ≤ 2·10^5)
        array: List of n integers (-10^9 ≤ a_i ≤ 10^9)
        
    Returns:
        List of n integers where d_i is the difference of indices between i and nearest j
        such that a_j = 0
    """
    pass
