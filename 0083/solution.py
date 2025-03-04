"""
You are given an array of $n$ integers: $a_1, a_2, \ldots, a_n$. Your task is to find some non-zero integer $d$ ($-10^3 \leq d \leq 10^3$) such that, after each number in the array is divided by $d$, the number of positive numbers that are presented in the array is greater than or equal to half of the array size (i.e., at least $\lceil\frac{n}{2}\rceil$). Note that those positive numbers do not need to be an integer (e.g., a $2.5$ counts as a positive number). If there are multiple values of $d$ that satisfy the condition, you may print any of them. In case that there is no such $d$, print a single integer $0$.

Recall that $\lceil x \rceil$ represents the smallest integer that is not less than $x$ and that zero ($0$) is neither positive nor negative.


-----Input-----

The first line contains one integer $n$ ($1 \le n \le 100$) — the number of elements in the array.

The second line contains $n$ space-separated integers $a_1, a_2, \ldots, a_n$ ($-10^3 \le a_i \le 10^3$).


-----Output-----

Print one integer $d$ ($-10^3 \leq d \leq 10^3$ and $d \neq 0$) that satisfies the given condition. If there are multiple values of $d$ that satisfy the condition, you may print any of them. In case that there is no such $d$, print a single integer $0$.


-----Examples-----
Input
5
10 0 -7 2 6
Output
4
Input
7
0 0 1 -1 0 0 2

Output
0


-----Note-----

In the first sample, $n = 5$, so we need at least $\lceil\frac{5}{2}\rceil = 3$ positive numbers after division. If $d = 4$, the array after division is $[2.5, 0, -1.75, 0.5, 1.5]$, in which there are $3$ positive numbers (namely: $2.5$, $0.5$, and $1.5$).

In the second sample, there is no valid $d$, so $0$ should be printed.
"""

def find_divisor_for_positive_numbers(n: int, array: list) -> int:
    """
    Find a non-zero integer d such that after dividing each number in the array by d,
    at least half of the numbers are positive.
    
    Args:
        n: Number of elements in the array (1 ≤ n ≤ 100)
        array: List of n integers (-10^3 ≤ a_i ≤ 10^3)
        
    Returns:
        A non-zero integer d (-10^3 ≤ d ≤ 10^3) that satisfies the condition,
        or 0 if no such d exists
    """
    pass
