"""
Polycarp has recently created a new level in this cool new game Berlio Maker 85 and uploaded it online. Now players from all over the world can try his level.

All levels in this game have two stats to them: the number of plays and the number of clears. So when a player attempts the level, the number of plays increases by $1$. If he manages to finish the level successfully then the number of clears increases by $1$ as well. Note that both of the statistics update at the same time (so if the player finishes the level successfully then the number of plays will increase at the same time as the number of clears).

Polycarp is very excited about his level, so he keeps peeking at the stats to know how hard his level turns out to be.

So he peeked at the stats $n$ times and wrote down $n$ pairs of integers — $(p_1, c_1), (p_2, c_2), \dots, (p_n, c_n)$, where $p_i$ is the number of plays at the $i$-th moment of time and $c_i$ is the number of clears at the same moment of time. The stats are given in chronological order (i.e. the order of given pairs is exactly the same as Polycarp has written down).

Between two consecutive moments of time Polycarp peeked at the stats many players (but possibly zero) could attempt the level.

Finally, Polycarp wonders if he hasn't messed up any records and all the pairs are correct. If there could exist such a sequence of plays (and clears, respectively) that the stats were exactly as Polycarp has written down, then he considers his records correct.

Help him to check the correctness of his records.

For your convenience you have to answer multiple independent test cases.


-----Input-----

The first line contains a single integer $T$ $(1 \le T \le 500)$ — the number of test cases.

The first line of each test case contains a single integer $n$ ($1 \le n \le 100$) — the number of moments of time Polycarp peeked at the stats.

Each of the next $n$ lines contains two integers $p_i$ and $c_i$ ($0 \le p_i, c_i \le 1000$) — the number of plays and the number of clears of the level at the $i$-th moment of time.

Note that the stats are given in chronological order.


-----Output-----

For each test case print a single line.

If there could exist such a sequence of plays (and clears, respectively) that the stats were exactly as Polycarp has written down, then print "YES".

Otherwise, print "NO".

You can print each letter in any case (upper or lower).


-----Example-----
Input
6
3
0 0
1 1
1 2
2
1 0
1000 3
4
10 1
15 2
10 2
15 2
1
765 432
2
4 4
4 3
5
0 0
1 0
1 0
1 0
1 0

Output
NO
YES
NO
YES
NO
YES



-----Note-----

In the first test case at the third moment of time the number of clears increased but the number of plays did not, that couldn't have happened.

The second test case is a nice example of a Super Expert level.

In the third test case the number of plays decreased, which is impossible.

The fourth test case is probably an auto level with a single jump over the spike.

In the fifth test case the number of clears decreased, which is also impossible.

Nobody wanted to play the sixth test case; Polycarp's mom attempted it to make him feel better, however, she couldn't clear it.
"""

def check_level_stats(t: int, test_cases: list) -> list:
    """
    Check whether Polycarp's records of level stats could be correct.
    
    Args:
        t: Number of test cases (1 ≤ t ≤ 500)
        test_cases: List of test cases, where each test case contains:
                   - n: Number of moments Polycarp peeked at the stats (1 ≤ n ≤ 100)
                   - n pairs of [p_i, c_i] representing the number of plays and clears
                     at the i-th moment (0 ≤ p_i, c_i ≤ 1000)
        
    Returns:
        List of strings ("YES" or "NO") for each test case
    """
    pass
