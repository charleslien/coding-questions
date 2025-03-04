"""
You are given two numbers in different numeral systems. The first number a is given in base x numeral system, the second number b is given in base y numeral system. You need to compare these two numbers and output "<", ">" or "=" correspondingly.


-----Input-----

The first line contains two integers x and y (2 ≤ x, y ≤ 10^9) — the bases of the first and the second numeral systems correspondingly.

The second line contains a string a — the first number in base x numeral system.

The third line contains a string b — the second number in base y numeral system.

Both a and b consist of digits from 0 to 9. It is guaranteed that these numbers are correct numbers in the corresponding numeral systems. In other words, all digits of a are less than x, and all digits of b are less than y. Both a and b don't have leading zeroes. The lengths of a and b don't exceed 10^6.


-----Output-----

Output "<" if a < b, ">" if a > b and "=" if a = b.


-----Examples-----
Input
4 7
12
10

Output
<

Input
10 10
2
10

Output
<

Input
7 7
42
42

Output
=
"""

def compare_numbers_in_different_bases(x: int, y: int, a: str, b: str) -> str:
    """
    Compare two numbers in different numeral systems.
    
    Args:
        x: Base of the first numeral system (2 ≤ x ≤ 10^9)
        y: Base of the second numeral system (2 ≤ y ≤ 10^9)
        a: First number in base x numeral system (string of digits)
        b: Second number in base y numeral system (string of digits)
        
    Returns:
        "<" if a < b, ">" if a > b, "=" if a = b
    """
    pass
