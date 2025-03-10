"""
Apart from having lots of holidays throughout the year, residents of Berland also have whole lucky years. Year is considered lucky if it has no more than 1 non-zero digit in its number. So years 100, 40000, 5 are lucky and 12, 3001 and 12345 are not.

You are given current year in Berland. Your task is to find how long will residents of Berland wait till the next lucky year.


-----Input-----

The first line contains integer number n (1 ≤ n ≤ 10^9) — current year in Berland.


-----Output-----

Output amount of years from the current year to the next lucky one.


-----Examples-----
Input
4

Output
1

Input
201

Output
99

Input
4000

Output
1000



-----Note-----

In the first example next lucky year is 5. In the second one — 300. In the third — 5000.
"""

def years_until_lucky(n: int) -> int:
    """
    Calculate how many years until the next lucky year in Berland.
    A lucky year has no more than 1 non-zero digit in its number.
    
    Args:
        n: Current year in Berland (1 ≤ n ≤ 10^9)
        
    Returns:
        Number of years until the next lucky year
    """
    pass
