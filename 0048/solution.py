"""
Bizon the Champion isn't just charming, he also is very smart.

While some of us were learning the multiplication table, Bizon the Champion had fun in his own manner. Bizon the Champion painted an n × m multiplication table, where the element on the intersection of the i-th row and j-th column equals i·j (the rows and columns of the table are numbered starting from 1). Then he was asked: what number in the table is the k-th largest number? Bizon the Champion always answered correctly and immediately. Can you repeat his success?

Consider the given multiplication table. If you write out all n·m numbers from the table in the non-decreasing order, then the k-th number you write out is called the k-th largest number.


-----Input-----

The single line contains integers n, m and k (1 ≤ n, m ≤ 5·10^5; 1 ≤ k ≤ n·m).


-----Output-----

Print the k-th largest number in a n × m multiplication table.


-----Examples-----
Input
2 2 2

Output
2

Input
2 3 4

Output
3

Input
1 10 5

Output
5



-----Note-----

A 2 × 3 multiplication table looks like this:

1 2 3

2 4 6
"""

def kth_largest_in_multiplication_table(n: int, m: int, k: int) -> int:
    """
    Find the k-th largest number in an n × m multiplication table.
    
    Args:
        n: Number of rows in the multiplication table (1 ≤ n ≤ 5·10^5)
        m: Number of columns in the multiplication table (1 ≤ m ≤ 5·10^5)
        k: Position of the number to find (1 ≤ k ≤ n·m)
        
    Returns:
        The k-th largest number in the multiplication table
    """
    pass
