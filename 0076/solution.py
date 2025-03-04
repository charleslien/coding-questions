"""
Berland Football Cup starts really soon! Commentators from all over the world come to the event.

Organizers have already built $n$ commentary boxes. $m$ regional delegations will come to the Cup. Every delegation should get the same number of the commentary boxes. If any box is left unoccupied then the delegations will be upset. So each box should be occupied by exactly one delegation.

If $n$ is not divisible by $m$, it is impossible to distribute the boxes to the delegations at the moment.

Organizers can build a new commentary box paying $a$ burles and demolish a commentary box paying $b$ burles. They can both build and demolish boxes arbitrary number of times (each time paying a corresponding fee). It is allowed to demolish all the existing boxes.

What is the minimal amount of burles organizers should pay to satisfy all the delegations (i.e. to make the number of the boxes be divisible by $m$)?


-----Input-----

The only line contains four integer numbers $n$, $m$, $a$ and $b$ ($1 \le n, m \le 10^{12}$, $1 \le a, b \le 100$), where $n$ is the initial number of the commentary boxes, $m$ is the number of delegations to come, $a$ is the fee to build a box and $b$ is the fee to demolish a box.


-----Output-----

Output the minimal amount of burles organizers should pay to satisfy all the delegations (i.e. to make the number of the boxes be divisible by $m$). It is allowed that the final number of the boxes is equal to $0$.


-----Examples-----
Input
9 7 3 8

Output
15

Input
2 7 3 7

Output
14

Input
30 6 17 19

Output
0



-----Note-----

In the first example organizers can build $5$ boxes to make the total of $14$ paying $3$ burles for the each of them.

In the second example organizers can demolish $2$ boxes to make the total of $0$ paying $7$ burles for the each of them.

In the third example organizers are already able to distribute all the boxes equally among the delegations, each one get $5$ boxes.
"""

def min_cost_to_satisfy_delegations(n: int, m: int, a: int, b: int) -> int:
    """
    Calculate the minimal amount of burles organizers should pay to satisfy all delegations.
    
    Args:
        n: Initial number of commentary boxes (1 ≤ n ≤ 10^12)
        m: Number of delegations (1 ≤ m ≤ 10^12)
        a: Fee to build a box (1 ≤ a ≤ 100)
        b: Fee to demolish a box (1 ≤ b ≤ 100)
        
    Returns:
        Minimal amount of burles to pay
    """
    pass
