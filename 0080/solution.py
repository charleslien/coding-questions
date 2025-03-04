"""
Today on Informatics class Nastya learned about GCD and LCM (see links below). Nastya is very intelligent, so she solved all the tasks momentarily and now suggests you to solve one of them as well.

We define a pair of integers (a, b) good, if GCD(a, b) = x and LCM(a, b) = y, where GCD(a, b) denotes the greatest common divisor of a and b, and LCM(a, b) denotes the least common multiple of a and b.

You are given two integers x and y. You are to find the number of good pairs of integers (a, b) such that l ≤ a, b ≤ r. Note that pairs (a, b) and (b, a) are considered different if a ≠ b.


-----Input-----

The only line contains four integers l, r, x, y (1 ≤ l ≤ r ≤ 10^9, 1 ≤ x ≤ y ≤ 10^9).


-----Output-----

In the only line print the only integer — the answer for the problem.


-----Examples-----
Input
1 2 1 2

Output
2

Input
1 12 1 12

Output
4

Input
50 100 3 30

Output
0



-----Note-----

In the first example there are two suitable good pairs of integers (a, b): (1, 2) and (2, 1).

In the second example there are four suitable good pairs of integers (a, b): (1, 12), (12, 1), (3, 4) and (4, 3).

In the third example there are good pairs of integers, for example, (3, 30), but none of them fits the condition l ≤ a, b ≤ r.
"""

def count_good_pairs(l: int, r: int, x: int, y: int) -> int:
    """
    Count the number of good pairs (a, b) such that l ≤ a, b ≤ r, GCD(a, b) = x, and LCM(a, b) = y.
    
    Args:
        l: Lower bound for a and b (1 ≤ l ≤ r ≤ 10^9)
        r: Upper bound for a and b (1 ≤ l ≤ r ≤ 10^9)
        x: Required GCD value (1 ≤ x ≤ y ≤ 10^9)
        y: Required LCM value (1 ≤ x ≤ y ≤ 10^9)
        
    Returns:
        Number of good pairs (a, b)
    """
    pass
