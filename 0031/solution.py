"""
ZS the Coder has recently found an interesting concept called the Birthday Paradox. It states that given a random set of 23 people, there is around 50% chance that some two of them share the same birthday. ZS the Coder finds this very interesting, and decides to test this with the inhabitants of Udayland.

In Udayland, there are 2^{n} days in a year. ZS the Coder wants to interview k people from Udayland, each of them has birthday in one of 2^{n} days (each day with equal probability). He is interested in the probability of at least two of them have the birthday at the same day. 

ZS the Coder knows that the answer can be written as an irreducible fraction $\frac{A}{B}$. He wants to find the values of A and B (he does not like to deal with floating point numbers). Can you help him?


-----Input-----

The first and only line of the input contains two integers n and k (1 ≤ n ≤ 10^18, 2 ≤ k ≤ 10^18), meaning that there are 2^{n} days in a year and that ZS the Coder wants to interview exactly k people.


-----Output-----

If the probability of at least two k people having the same birthday in 2^{n} days long year equals $\frac{A}{B}$ (A ≥ 0, B ≥ 1, $\operatorname{gcd}(A, B) = 1$), print the A and B in a single line.

Since these numbers may be too large, print them modulo 10^6 + 3. Note that A and B must be coprime before their remainders modulo 10^6 + 3 are taken.


-----Examples-----
Input
3 2

Output
1 8
Input
1 3

Output
1 1
Input
4 3

Output
23 128


-----Note-----

In the first sample case, there are 2^3 = 8 days in Udayland. The probability that 2 people have the same birthday among 2 people is clearly $\frac{1}{8}$, so A = 1, B = 8.

In the second sample case, there are only 2^1 = 2 days in Udayland, but there are 3 people, so it is guaranteed that two of them have the same birthday. Thus, the probability is 1 and A = B = 1.
"""

def birthday_paradox_probability(n: int, k: int) -> tuple:
    """
    Calculate the probability of at least two people having the same birthday.
    
    Args:
        n: Parameter such that there are 2^n days in a year (1 ≤ n ≤ 10^18)
        k: Number of people to interview (2 ≤ k ≤ 10^18)
        
    Returns:
        Tuple (A, B) representing the probability as A/B,
        where both A and B are taken modulo 10^6 + 3
    """
    pass
