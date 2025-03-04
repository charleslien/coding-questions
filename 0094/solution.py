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
13
12

Output
12

Input
16
11311

Output
475

Input
20
999

Output
3789

Input
17
2016

Output
594
"""

def count_ways_to_represent(n: int) -> int:
    """
    Count the number of ways to represent n as 2^a·3^b, where a and b are non-negative integers.
    
    Args:
        n: Integer to represent (1 ≤ n ≤ 10^9)
        
    Returns:
        Number of ways to represent n as 2^a·3^b
    """
    pass
