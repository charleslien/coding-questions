"""
You have a long fence which consists of $n$ sections. Unfortunately, it is not painted, so you decided to hire $q$ painters to paint it. $i$-th painter will paint all sections $x$ such that $l_i \le x \le r_i$.

Unfortunately, you are on a tight budget, so you may hire only $q - 2$ painters. Obviously, only painters you hire will do their work.

You want to maximize the number of painted sections if you choose $q - 2$ painters optimally. A section is considered painted if at least one painter paints it.


-----Input-----

The first line contains two integers $n$ and $q$ ($3 \le n, q \le 5000$) — the number of sections and the number of painters availible for hire, respectively.

Then $q$ lines follow, each describing one of the painters: $i$-th line contains two integers $l_i$ and $r_i$ ($1 \le l_i \le r_i \le n$).


-----Output-----

Print one integer — maximum number of painted sections if you hire $q - 2$ painters.


-----Examples-----
Input
7 5
1 4
4 5
5 6
6 7
3 5

Output
7

Input
4 3
1 1
2 2
3 4

Output
2

Input
4 4
1 1
2 2
2 3
3 4

Output
3
"""

def max_painted_sections(n: int, q: int, painters: list) -> int:
    """
    Calculate the maximum number of painted sections if you choose q-2 painters optimally.
    
    Args:
        n: Number of sections in the fence
        q: Number of painters available for hire
        painters: List of q painters, where each painter is represented by [l_i, r_i]
                 indicating they will paint sections from l_i to r_i inclusive
        
    Returns:
        Maximum number of painted sections if you hire q-2 painters
    """
    pass
