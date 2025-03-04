"""
Vasya has a robot which is situated on an infinite Cartesian plane, initially in the cell (0, 0). Robot can perform the following four kinds of operations:   U — move from (x, y) to (x, y + 1);  D — move from (x, y) to (x, y - 1);  L — move from (x, y) to (x - 1, y);  R — move from (x, y) to (x + 1, y). 

Vasya also has got a sequence of n operations. Vasya wants to modify this sequence so after performing it the robot will end up in (x, y).

Vasya wants to change the sequence so the length of changed subsegment is minimum possible. This length can be calculated as follows: maxID - minID + 1, where maxID is the maximum index of a changed operation, and minID is the minimum index of a changed operation. For example, if Vasya changes RRRRRRR to RLRRLRL, then the operations with indices 2, 5 and 7 are changed, so the length of changed subsegment is 7 - 2 + 1 = 6. Another example: if Vasya changes DDDD to DDRD, then the length of changed subsegment is 1. 

If there are no changes, then the length of changed subsegment is 0. Changing an operation means replacing it with some operation (possibly the same); Vasya can't insert new operations into the sequence or remove them.

Help Vasya! Tell him the minimum length of subsegment that he needs to change so that the robot will go from (0, 0) to (x, y), or tell him that it's impossible.


-----Input-----

The first line contains one integer number n (1 ≤ n ≤ 2·10^5) — the number of operations.

The second line contains the sequence of operations — a string of n characters. Each character is either U, D, L or R.

The third line contains two integers x, y (-10^9 ≤ x, y ≤ 10^9) — the coordinates of the cell where the robot should end its path.


-----Output-----

Print one integer — the minimum possible length of subsegment that can be changed so the resulting sequence of operations moves the robot from (0, 0) to (x, y). If this change is impossible, print -1.


-----Examples-----
Input
5
RURUU
-2 3

Output
3

Input
4
RULR
1 1

Output
0

Input
3
UUU
100 100

Output
-1
"""

def min_subsegment_length_to_change(n: int, operations: str, x: int, y: int) -> int:
    """
    Calculate the minimum length of subsegment that needs to be changed.
    
    Args:
        n: Number of operations (1 ≤ n ≤ 2·10^5)
        operations: String of n characters, each is either 'U', 'D', 'L', or 'R'
        x: x-coordinate of the target cell (-10^9 ≤ x ≤ 10^9)
        y: y-coordinate of the target cell (-10^9 ≤ y ≤ 10^9)
        
    Returns:
        Minimum possible length of subsegment that can be changed,
        or -1 if the change is impossible
    """
    pass
