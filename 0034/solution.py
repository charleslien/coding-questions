"""
It's New Year's Eve soon, so Ivan decided it's high time he started setting the table. Ivan has bought two cakes and cut them into pieces: the first cake has been cut into a pieces, and the second one — into b pieces.

Ivan knows that there will be n people at the celebration (including himself), so Ivan has set n plates for the cakes. Now he is thinking about how to distribute the cakes between the plates. Ivan wants to do it in such a way that all following conditions are met:  Each piece of each cake is put on some plate;  Each plate contains at least one piece of cake;  No plate contains pieces of both cakes. 

To make his guests happy, Ivan wants to distribute the cakes in such a way that the minimum number of pieces on the plate is maximized. Formally, Ivan wants to know the maximum possible number x such that he can distribute the cakes according to the aforementioned conditions, and each plate will contain at least x pieces of cake.

Help Ivan to calculate this number x!


-----Input-----

The first line contains three integers n, a and b (1 ≤ a, b ≤ 100, 2 ≤ n ≤ a + b) — the number of plates, the number of pieces of the first cake, and the number of pieces of the second cake, respectively.


-----Output-----

Print the maximum possible number x such that Ivan can distribute the cake in such a way that each plate will contain at least x pieces of cake.


-----Examples-----
Input
5 2 3

Output
1

Input
4 7 10

Output
3



-----Note-----

In the first example there is only one way to distribute cakes to plates, all of them will have 1 cake on it.

In the second example you can have two plates with 3 and 4 pieces of the first cake and two plates both with 5 pieces of the second cake. Minimal number of pieces is 3.
"""

def max_min_pieces_on_plate(n: int, a: int, b: int) -> int:
    """
    Calculate the maximum possible minimum number of pieces on a plate.
    
    Args:
        n: Number of plates (2 ≤ n ≤ a + b)
        a: Number of pieces of the first cake (1 ≤ a ≤ 100)
        b: Number of pieces of the second cake (1 ≤ b ≤ 100)
        
    Returns:
        Maximum possible value x such that each plate will contain at least x pieces of cake
    """
    pass
