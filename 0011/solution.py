"""
Little Joty has got a task to do. She has a line of n tiles indexed from 1 to n. She has to paint them in a strange pattern.

An unpainted tile should be painted Red if it's index is divisible by a and an unpainted tile should be painted Blue if it's index is divisible by b. So the tile with the number divisible by a and b can be either painted Red or Blue.

After her painting is done, she will get p chocolates for each tile that is painted Red and q chocolates for each tile that is painted Blue.

Note that she can paint tiles in any order she wants.

Given the required information, find the maximum number of chocolates Joty can get.


-----Input-----

The only line contains five integers n, a, b, p and q (1 ≤ n, a, b, p, q ≤ 10^9).


-----Output-----

Print the only integer s — the maximum number of chocolates Joty can get.

Note that the answer can be too large, so you should use 64-bit integer type to store it. In C++ you can use the long long integer type and in Java you can use long integer type.


-----Examples-----
Input
5 2 3 12 15

Output
39

Input
20 2 3 3 5

Output
51
"""

def max_chocolates(n: int, a: int, b: int, p: int, q: int) -> int:
    """
    Calculate the maximum number of chocolates Joty can get.
    
    Args:
        n: Number of tiles (1 ≤ n ≤ 10^9)
        a: Divisibility condition for Red tiles (1 ≤ a ≤ 10^9)
        b: Divisibility condition for Blue tiles (1 ≤ b ≤ 10^9)
        p: Number of chocolates for each Red tile (1 ≤ p ≤ 10^9)
        q: Number of chocolates for each Blue tile (1 ≤ q ≤ 10^9)
        
    Returns:
        The maximum number of chocolates Joty can get
    """
    pass
