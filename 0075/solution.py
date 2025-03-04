"""
You are given a description of a depot. It is a rectangular checkered field of n × m size. Each cell in a field can be empty (".") or it can be occupied by a wall ("*"). 

You have one bomb. If you lay the bomb at the cell (x, y), then after triggering it will wipe out all walls in the row x and all walls in the column y.

You are to determine if it is possible to wipe out all walls in the depot by placing and triggering exactly one bomb. The bomb can be laid both in an empty cell or in a cell occupied by a wall.


-----Input-----

The first line contains two positive integers n and m (1 ≤ n, m ≤ 1000) — the number of rows and columns in the depot field. 

The next n lines contain m symbols "." and "*" each — the description of the field. j-th symbol in i-th of them stands for cell (i, j). If the symbol is equal to ".", then the corresponding cell is empty, otherwise it equals "*" and the corresponding cell is occupied by a wall.


-----Output-----

If it is impossible to wipe out all walls by placing and triggering exactly one bomb, then print "NO" in the first line (without quotes).

Otherwise print "YES" (without quotes) in the first line and two integers in the second line — the coordinates of the cell at which the bomb should be laid. If there are multiple answers, print any of them.


-----Examples-----
Input
3 4
.*..
....
.*..

Output
YES
1 2

Input
3 3
..*
.*.
*..

Output
NO

Input
6 5
..*..
..*..
*****
..*..
..*..
..*..

Output
YES
3 3
"""

def can_wipe_out_all_walls(n: int, m: int, depot: list) -> tuple:
    """
    Determine if it's possible to wipe out all walls with one bomb.
    
    Args:
        n: Number of rows in the depot (1 ≤ n ≤ 1000)
        m: Number of columns in the depot (1 ≤ m ≤ 1000)
        depot: List of n strings, each containing m characters ('.' or '*')
              representing the depot field
        
    Returns:
        Tuple (result, coordinates), where:
        - result: "YES" if it's possible to wipe out all walls, "NO" otherwise
        - coordinates: Tuple (x, y) representing the coordinates where the bomb should be laid
                      if result is "YES", empty tuple otherwise
    """
    pass
