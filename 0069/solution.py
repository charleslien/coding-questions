"""
You are given a binary string s of length n. Let's denote the number of occurrences of the character '0' in s as cnt_0, and the number of occurrences of the character '1' as cnt_1.

You can perform the following operation on the string:

Choose an index i (1 ≤ i ≤ n) and replace the character at position i with the opposite character (i.e., replace '0' with '1' or '1' with '0').

After performing the operation, the balance of the string changes. The balance of the string is defined as cnt_1 - cnt_0.

You are given an integer x. Your task is to find the number of indices i such that if you perform the operation at position i, the balance of the string becomes exactly x.


-----Input-----

The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

For each test case:

The first line contains two integers n and x (1 ≤ n ≤ 2·10^5, -n ≤ x ≤ n) — the length of the string and the target balance.

The second line contains a binary string s of length n, consisting only of the characters '0' and '1'.

It is guaranteed that the sum of n over all test cases does not exceed 2·10^5.


-----Output-----

For each test case, print a single integer — the number of indices i such that if you perform the operation at position i, the balance of the string becomes exactly x.


-----Examples-----
Input
3
5 1
01010
3 -3
111
4 0
0001

Output
3
0
1
"""

def count_indices_for_target_balance(t: int, test_cases: list) -> list:
    """
    Count the number of indices where performing the operation results in the target balance.
    
    Args:
        t: Number of test cases (1 ≤ t ≤ 10^4)
        test_cases: List of t test cases, where each test case contains:
                   - n: Length of the string (1 ≤ n ≤ 2·10^5)
                   - x: Target balance (-n ≤ x ≤ n)
                   - s: Binary string of length n
        
    Returns:
        List of t integers, where each integer is the number of indices for the corresponding test case
    """
    pass
