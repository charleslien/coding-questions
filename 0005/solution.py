"""
Luba is surfing the Internet. She currently has n opened tabs in her browser, indexed from 1 to n from left to right. The mouse cursor is currently located at the pos-th tab. Luba needs to use the tabs with indices from l to r (inclusive) for her studies, and she wants to close all the tabs that don't belong to this segment as fast as possible.

Each second Luba can either try moving the cursor to the left or to the right (if the cursor is currently at the tab i, then she can move it to the tab max(i - 1, a) or to the tab min(i + 1, b)) or try closing all the tabs to the left or to the right of the cursor (if the cursor is currently at the tab i, she can close all the tabs with indices from segment [a, i - 1] or from segment [i + 1, b]). In the aforementioned expressions a and b denote the minimum and maximum index of an unclosed tab, respectively. For example, if there were 7 tabs initially and tabs 1, 2 and 7 are closed, then a = 3, b = 6.

What is the minimum number of seconds Luba has to spend in order to leave only the tabs with initial indices from l to r inclusive opened?


-----Input-----

The only line of input contains four integer numbers n, pos, l, r (1 ≤ n ≤ 100, 1 ≤ pos ≤ n, 1 ≤ l ≤ r ≤ n) — the number of the tabs, the cursor position and the segment which Luba needs to leave opened.


-----Output-----

Print one integer equal to the minimum number of seconds required to close all the tabs outside the segment [l, r].


-----Examples-----
Input
6 3 2 4

Output
5

Input
6 3 1 3

Output
1

Input
5 2 1 5

Output
0



-----Note-----

In the first test Luba can do the following operations: shift the mouse cursor to the tab 2, close all the tabs to the left of it, shift the mouse cursor to the tab 3, then to the tab 4, and then close all the tabs to the right of it.

In the second test she only needs to close all the tabs to the right of the current position of the cursor.

In the third test Luba doesn't need to do anything.
"""

def min_seconds_to_close_tabs(n: int, pos: int, l: int, r: int) -> int:
    """
    Calculate the minimum number of seconds required to close all tabs outside the segment [l, r].
    
    Args:
        n: Number of tabs (1 ≤ n ≤ 100)
        pos: Current cursor position (1 ≤ pos ≤ n)
        l: Left boundary of the segment to keep (1 ≤ l ≤ r ≤ n)
        r: Right boundary of the segment to keep (1 ≤ l ≤ r ≤ n)
        
    Returns:
        Minimum number of seconds required to close all tabs outside [l, r]
    """
    pass
