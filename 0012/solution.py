"""
Vova has won $n$ trophies in different competitions. Each trophy is either golden or silver. The trophies are arranged in a row.

The beauty of the arrangement is the length of the longest subsegment consisting of golden trophies. Vova wants to swap two trophies (not necessarily adjacent ones) to make the arrangement as beautiful as possible — that means, to maximize the length of the longest such subsegment.

Help Vova! Tell him the maximum possible beauty of the arrangement if he is allowed to do at most one swap.


-----Input-----

The first line contains one integer $n$ ($2 \le n \le 10^5$) — the number of trophies.

The second line contains $n$ characters, each of them is either G or S. If the $i$-th character is G, then the $i$-th trophy is a golden one, otherwise it's a silver trophy. 


-----Output-----

Print the maximum possible length of a subsegment of golden trophies, if Vova is allowed to do at most one swap.


-----Examples-----
Input
10
GGGSGGGSGG

Output
7

Input
4
GGGG

Output
4

Input
3
SSS

Output
0



-----Note-----

In the first example Vova has to swap trophies with indices $4$ and $10$. Thus he will obtain the sequence "GGGGGGGSGS", the length of the longest subsegment of golden trophies is $7$. 

In the second example Vova can make no swaps at all. The length of the longest subsegment of golden trophies in the sequence is $4$. 

In the third example Vova cannot do anything to make the length of the longest subsegment of golden trophies in the sequence greater than $0$.
"""

def max_beauty_after_swap(n: int, trophies: str) -> int:
    """
    Calculate the maximum possible length of a subsegment of golden trophies
    after at most one swap.
    
    Args:
        n: Number of trophies (2 ≤ n ≤ 10^5)
        trophies: String of length n consisting of 'G' and 'S' characters,
                 where 'G' represents a golden trophy and 'S' represents a silver trophy
        
    Returns:
        The maximum possible length of a subsegment of golden trophies
    """
    pass
