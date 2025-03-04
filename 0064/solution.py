"""
Polycarp has n balls, each of them has some color. The color of the i-th ball is c_i. Polycarp wants to distribute these balls between his k friends. He wants to distribute all n balls.

Polycarp wants to distribute balls in such a way that no friend receives two or more balls of the same color. In other words, all balls that one friend receives must be of different colors.

Help Polycarp to find out if he can distribute all balls between his k friends, following the rule above.


-----Input-----

The first line of the input contains two integers n and k (1 ≤ n, k ≤ 100) — the number of balls and the number of Polycarp's friends.

The second line of the input contains n integers c_1, c_2, ..., c_n (1 ≤ c_i ≤ 100), where c_i is the color of the i-th ball.


-----Output-----

Print "YES" (without quotes) if Polycarp can distribute all balls between his k friends, following the rule above. Otherwise, print "NO" (without quotes).


-----Examples-----
Input
5 3
1 2 1 1 3

Output
YES

Input
5 2
1 2 1 1 3

Output
NO

Input
6 2
1 1 2 2 3 3

Output
YES
"""

def can_distribute_balls(n: int, k: int, colors: list) -> str:
    """
    Determine if Polycarp can distribute all balls between his k friends.
    
    Args:
        n: Number of balls (1 ≤ n ≤ 100)
        k: Number of friends (1 ≤ k ≤ 100)
        colors: List of n integers representing the colors of the balls (1 ≤ c_i ≤ 100)
        
    Returns:
        "YES" if Polycarp can distribute all balls, "NO" otherwise
    """
    pass
