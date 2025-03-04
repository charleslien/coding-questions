"""
You are given two arithmetic progressions: a_1k + b_1 and a_2l + b_2. Find the number of integers x such that L ≤ x ≤ R and x = a_1k' + b_1 = a_2l' + b_2, for some integers k', l' ≥ 0.


-----Input-----

The only line contains six integers a_1, b_1, a_2, b_2, L, R (0 < a_1, a_2 ≤ 2·10^9,  - 2·10^9 ≤ b_1, b_2, L, R ≤ 2·10^9, L ≤ R).


-----Output-----

Print the desired number of integers x.


-----Examples-----
Input
2 0 3 3 5 21

Output
3

Input
2 4 3 0 6 17

Output
2
"""

def count_common_integers(a1: int, b1: int, a2: int, b2: int, L: int, R: int) -> int:
    """
    Count the number of integers x in the range [L, R] that belong to both arithmetic progressions.
    
    Args:
        a1: First coefficient of the first progression (0 < a1 ≤ 2·10^9)
        b1: Second coefficient of the first progression (-2·10^9 ≤ b1 ≤ 2·10^9)
        a2: First coefficient of the second progression (0 < a2 ≤ 2·10^9)
        b2: Second coefficient of the second progression (-2·10^9 ≤ b2 ≤ 2·10^9)
        L: Lower bound of the range (-2·10^9 ≤ L ≤ 2·10^9)
        R: Upper bound of the range (L ≤ R ≤ 2·10^9)
        
    Returns:
        Number of integers x in the range [L, R] such that 
        x = a1*k + b1 = a2*l + b2 for some non-negative integers k, l
    """
    pass
