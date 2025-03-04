"""
Anya loves to fold and stick. Today she decided to do just that.

Anya has n cubes lying in a line and numbered from 1 to n from left to right, with natural numbers written on them. She also has k stickers with exclamation marks. We know that the number of stickers does not exceed the number of cubes.

Anya can stick an exclamation mark on the cube and get the factorial of the number written on the cube. For example, if a cube reads 5, then after the sticking it reads 5!, which equals 120.

You need to help Anya count how many ways there are to choose some of the cubes and stick on some of the chosen cubes at most k exclamation marks so that the sum of the numbers written on the chosen cubes after the sticking becomes equal to S. Anya can stick at most one exclamation mark on each cube. Can you do it?

Two ways are considered the same if they have the same set of chosen cubes and the same set of cubes with exclamation marks.


-----Input-----

The first line of the input contains three space-separated integers n, k and S (1 ≤ n ≤ 25, 0 ≤ k ≤ n, 1 ≤ S ≤ 10^16) — the number of cubes and the number of stickers that Anya has, and the sum that she needs to get. 

The second line contains n positive integers a_{i} (1 ≤ a_{i} ≤ 10^9) — the numbers, written on the cubes. The cubes in the input are described in the order from left to right, starting from the first one. 

Multiple cubes can contain the same numbers.


-----Output-----

Output the number of ways to choose some number of cubes and stick exclamation marks on some of them so that the sum of the numbers became equal to the given number S.


-----Examples-----
Input
2 2 30
4 3

Output
1

Input
2 2 7
4 3

Output
1

Input
3 1 1
1 1 1

Output
6



-----Note-----

In the first sample the only way is to choose both cubes and stick an exclamation mark on each of them.

In the second sample the only way is to choose both cubes but don't stick an exclamation mark on any of them.

In the third sample it is possible to choose any of the cubes in three ways, and also we may choose to stick or not to stick the exclamation mark on it. So, the total number of ways is six.
"""

def count_ways_to_get_sum(n: int, k: int, S: int, numbers: list) -> int:
    """
    Count the number of ways to choose cubes and stick exclamation marks to get the target sum.
    
    Args:
        n: Number of cubes (1 ≤ n ≤ 25)
        k: Number of stickers (0 ≤ k ≤ n)
        S: Target sum (1 ≤ S ≤ 10^16)
        numbers: List of n positive integers representing the numbers on the cubes (1 ≤ a_i ≤ 10^9)
        
    Returns:
        Number of ways to choose cubes and stick exclamation marks to get sum S
    """
    pass
