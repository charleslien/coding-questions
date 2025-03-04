"""
Petya has a calendar for the current month. He uses the following numeration: days of week are numbered from 1 to 7, where 1 is Monday, 2 is Tuesday, ..., 7 is Sunday. For example, if the month starts from Wednesday, then the days of this month have numbers: 3, 4, 5, 6, 7, 1, 2, ...

Petya knows that the m-th day of the current month is the d-th day of the week. He wants to determine how many full weeks are there in the period from the 1st to the m-th day of the current month, inclusive.

For example, if the 15-th day of the current month is the 6-th day of the week (i.e. Saturday), then the period from the 1st to the 15-th day of the current month includes 2 full weeks.


-----Input-----

The only line contains two integers m and d (1 ≤ m ≤ 31, 1 ≤ d ≤ 7) — the number of the day of the current month and the number of the day of the week, respectively.


-----Output-----

Print one integer — the number of full weeks in the period from the 1st to the m-th day of the current month, inclusive.


-----Examples-----
Input
15 6

Output
2

Input
29 3

Output
4
"""

def count_full_weeks(m: int, d: int) -> int:
    """
    Calculate the number of full weeks in the period from the 1st to the m-th day of the month.
    
    Args:
        m: Number of the day of the current month (1 ≤ m ≤ 31)
        d: Number of the day of the week (1 ≤ d ≤ 7)
        
    Returns:
        Number of full weeks in the period
    """
    pass
