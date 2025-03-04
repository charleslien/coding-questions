"""
Polycarp has a number n. He wants to find the number of ways to represent n as 2^a·3^b, where a and b are non-negative integers.

For example, if n = 12, then there are two ways to represent n as 2^a·3^b:
- 12 = 2^2·3^1
- 12 = 2^0·3^2·2^2 = 2^2·3^2/3^1 = 2^2·3^1

Help Polycarp find the number of ways to represent n as 2^a·3^b, where a and b are non-negative integers.


-----Input-----

The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases.

Each test case consists of a single line containing a single integer n (1 ≤ n ≤ 10^9).


-----Output-----

For each test case, print a single integer — the number of ways to represent n as 2^a·3^b, where a and b are non-negative integers.


-----Examples-----
Input
11 3

Output
5

Input
11 6

Output
4

Input
20 20

Output
1

Input
14 5

Output
6
"""

def count_ways_to_represent_with_powers(n: int, m: int) -> int:
    """
    Count the number of ways to represent n as a sum of powers of m.
    
    Args:
        n: Integer to represent (1 ≤ n ≤ 10^9)
        m: Base for the powers (1 ≤ m ≤ 10^9)
        
    Returns:
        Number of ways to represent n
    """
    pass
