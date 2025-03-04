"""
Polycarp has two integers a and b. He wants to find the number of pairs of integers (x, y) such that:

1. 1 ≤ x ≤ a
2. 1 ≤ y ≤ b
3. The value of gcd(x, y) is odd

Here gcd(x, y) denotes the greatest common divisor (GCD) of integers x and y.

Help Polycarp find this number.


-----Input-----

The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case consists of a single line containing two integers a and b (1 ≤ a, b ≤ 10^18).


-----Output-----

For each test case, print a single integer — the number of pairs (x, y) satisfying all the conditions.


-----Examples-----
Input
5 10

Output
22

Input
2015 2015

Output
1

Input
100 105

Output
0

Input
72057594000000000 72057595000000000

Output
26

Input
1 100

Output
16
"""

def count_pairs_with_odd_gcd(a: int, b: int) -> int:
    """
    Count the number of pairs (x, y) such that 1 ≤ x ≤ a, 1 ≤ y ≤ b, and gcd(x, y) is odd.
    
    Args:
        a: Upper bound for x (1 ≤ a ≤ 10^18)
        b: Upper bound for y (1 ≤ b ≤ 10^18)
        
    Returns:
        Number of pairs (x, y) satisfying all the conditions
    """
    pass
