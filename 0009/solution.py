"""
Yet another round on DecoForces is coming! Grandpa Maks wanted to participate in it but someone has stolen his precious sofa! And how can one perform well with such a major loss?

Fortunately, the thief had left a note for Grandpa Maks. This note got Maks to the sofa storehouse. Still he had no idea which sofa belongs to him as they all looked the same!

The storehouse is represented as matrix n × m. Every sofa takes two neighbouring by some side cells. No cell is covered by more than one sofa. There can be empty cells.

Sofa A is standing to the left of sofa B if there exist two such cells a and b that x_{a} < x_{b}, a is covered by A and b is covered by B. Sofa A is standing to the top of sofa B if there exist two such cells a and b that y_{a} < y_{b}, a is covered by A and b is covered by B. Right and bottom conditions are declared the same way. 

Note that in all conditions A ≠ B. Also some sofa A can be both to the top of another sofa B and to the bottom of it. The same is for left and right conditions.

The note also stated that there are cnt_{l} sofas to the left of Grandpa Maks's sofa, cnt_{r} — to the right, cnt_{t} — to the top and cnt_{b} — to the bottom.

Grandpa Maks asks you to help him to identify his sofa. It is guaranteed that there is no more than one sofa of given conditions.

Output the number of Grandpa Maks's sofa. If there is no such sofa that all the conditions are met for it then output -1.


-----Input-----

The first line contains one integer number d (1 ≤ d ≤ 10^5) — the number of sofas in the storehouse.

The second line contains two integer numbers n, m (1 ≤ n, m ≤ 10^5) — the size of the storehouse.

Next d lines contains four integer numbers x_1, y_1, x_2, y_2 (1 ≤ x_1, x_2 ≤ n, 1 ≤ y_1, y_2 ≤ m) — coordinates of the i-th sofa. It is guaranteed that cells (x_1, y_1) and (x_2, y_2) have common side, (x_1, y_1)  ≠  (x_2, y_2) and no cell is covered by more than one sofa.

The last line contains four integer numbers cnt_{l}, cnt_{r}, cnt_{t}, cnt_{b} (0 ≤ cnt_{l}, cnt_{r}, cnt_{t}, cnt_{b} ≤ d - 1).


-----Output-----

Print the number of the sofa for which all the conditions are met. Sofas are numbered 1 through d as given in input. If there is no such sofa then print -1.


-----Examples-----
Input
2
3 2
3 1 3 2
1 2 2 2
1 0 0 1

Output
1

Input
3
10 10
1 2 1 1
5 5 6 5
6 4 5 4
2 1 2 0

Output
2

Input
2
2 2
2 1 1 1
1 2 2 2
1 0 0 0

Output
-1



-----Note-----

Let's consider the second example.   The first sofa has 0 to its left, 2 sofas to its right ((1, 1) is to the left of both (5, 5) and (5, 4)), 0 to its top and 2 to its bottom (both 2nd and 3rd sofas are below).  The second sofa has cnt_{l} = 2, cnt_{r} = 1, cnt_{t} = 2 and cnt_{b} = 0.  The third sofa has cnt_{l} = 2, cnt_{r} = 1, cnt_{t} = 1 and cnt_{b} = 1. 

So the second one corresponds to the given conditions.

In the third example   The first sofa has cnt_{l} = 1, cnt_{r} = 1, cnt_{t} = 0 and cnt_{b} = 1.  The second sofa has cnt_{l} = 1, cnt_{r} = 1, cnt_{t} = 1 and cnt_{b} = 0. 

And there is no sofa with the set (1, 0, 0, 0) so the answer is -1.
"""

def find_grandpa_maks_sofa(d: int, n: int, m: int, sofas: list, counts: list) -> int:
    """
    Identify which sofa belongs to Grandpa Maks based on the given conditions.
    
    Args:
        d: Number of sofas in the storehouse (1 ≤ d ≤ 10^5)
        n: Number of rows in the storehouse (1 ≤ n ≤ 10^5)
        m: Number of columns in the storehouse (1 ≤ m ≤ 10^5)
        sofas: List of d sofas, where each sofa is represented by [x_1, y_1, x_2, y_2]
               indicating the coordinates of the two cells it covers
        counts: List [cnt_l, cnt_r, cnt_t, cnt_b] indicating the number of sofas
                to the left, right, top, and bottom of Grandpa Maks's sofa
        
    Returns:
        The number of Grandpa Maks's sofa (1-indexed), or -1 if no such sofa exists
    """
    pass
