"""
There are n shovels in Polycarp's shop. The i-th shovel costs i burles, that is, the first shovel costs 1 burle, the second shovel costs 2 burles, the third shovel costs 3 burles, and so on. Polycarps wants to sell shovels in pairs.

Visitors are more likely to buy a pair of shovels if their total cost ends with several 9s. Because of this, Polycarp wants to choose a pair of shovels to sell in such a way that the sum of their costs ends with maximum possible number of nines. For example, if he chooses shovels with costs 12345 and 37454, their total cost is 49799, it ends with two nines.

You are to compute the number of pairs of shovels such that their total cost ends with maximum possible number of nines. Two pairs are considered different if there is a shovel presented in one pair, but not in the other.


-----Input-----

The first line contains a single integer n (2 ≤ n ≤ 10^9) — the number of shovels in Polycarp's shop.


-----Output-----

Print the number of pairs of shovels such that their total cost ends with maximum possible number of nines. 

Note that it is possible that the largest number of 9s at the end is 0, then you should count all such ways.

It is guaranteed that for every n ≤ 10^9 the answer doesn't exceed 2·10^9.


-----Examples-----
Input
7

Output
3

Input
14

Output
9

Input
50

Output
1



-----Note-----

In the first example the maximum possible number of nines at the end is one. Polycarp cah choose the following pairs of shovels for that purpose:  2 and 7;  3 and 6;  4 and 5. 

In the second example the maximum number of nines at the end of total cost of two shovels is one. The following pairs of shovels suit Polycarp:  1 and 8;  2 and 7;  3 and 6;  4 and 5;  5 and 14;  6 and 13;  7 and 12;  8 and 11;  9 and 10. 

In the third example it is necessary to choose shovels 49 and 50, because the sum of their cost is 99, that means that the total number of nines is equal to two, which is maximum possible for n = 50.
"""

def count_pairs_with_max_nines(n: int) -> int:
    """
    Count the number of pairs of shovels such that their total cost ends with 
    the maximum possible number of nines.
    
    Args:
        n: Number of shovels in Polycarp's shop (2 ≤ n ≤ 10^9)
        
    Returns:
        Number of pairs of shovels with the maximum possible number of nines at the end of their total cost
    """
    pass
