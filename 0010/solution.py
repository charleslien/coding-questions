"""
On the planet Mars a year lasts exactly n days (there are no leap years on Mars). But Martians have the same weeks as earthlings — 5 work days and then 2 days off. Your task is to determine the minimum possible and the maximum possible number of days off per year on Mars.


-----Input-----

The first line of the input contains a positive integer n (1 ≤ n ≤ 1 000 000) — the number of days in a year on Mars.


-----Output-----

Print two integers — the minimum possible and the maximum possible number of days off per year on Mars.


-----Examples-----
Input
14

Output
4 4

Input
2

Output
0 2



-----Note-----

In the first sample there are 14 days in a year on Mars, and therefore independently of the day a year starts with there will be exactly 4 days off .

In the second sample there are only 2 days in a year on Mars, and they can both be either work days or days off.
"""

def min_max_days_off(n: int) -> tuple:
    """
    Determine the minimum and maximum possible number of days off per year on Mars.
    
    Args:
        n: Number of days in a year on Mars (1 ≤ n ≤ 1,000,000)
        
    Returns:
        A tuple (min_days_off, max_days_off) representing the minimum and maximum
        possible number of days off per year on Mars
    """
    pass
