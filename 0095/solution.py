"""
You are given an array a consisting of n integers. Check if there exists a segment of array a that can be rearranged to form a strictly increasing sequence.

A sequence b_1, b_2, ..., b_k is called strictly increasing if b_1 < b_2 < ... < b_k.

A segment of array a is a sequence of elements a_l, a_{l+1}, ..., a_r for some l and r (1 ≤ l ≤ r ≤ n).


-----Input-----

The first line contains a single integer n (1 ≤ n ≤ 100) — the length of array a.

The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) — the elements of array a.


-----Output-----

Print "YES" if there exists a segment of array a that can be rearranged to form a strictly increasing sequence, and "NO" otherwise.


-----Examples-----
Input
5
1 2 3 4 5

Output
YES

Input
6
1 3 2 6 5 4

Output
YES

Input
5
5 4 3 2 1

Output
YES

Input
4
1 1 1 1

Output
NO
"""

def can_form_increasing_sequence(n: int, array: list) -> str:
    """
    Check if there exists a segment of the array that can be rearranged to form a strictly increasing sequence.
    
    Args:
        n: Length of the array (1 ≤ n ≤ 100)
        array: List of n integers (1 ≤ a_i ≤ 100)
        
    Returns:
        "YES" if there exists such a segment, "NO" otherwise
    """
    pass
