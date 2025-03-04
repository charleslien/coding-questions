"""
Polycarp is crazy about round numbers. He especially likes the numbers divisible by 10^{k}.

In the given number of n Polycarp wants to remove the least number of digits to get a number that is divisible by 10^{k}. For example, if k = 3, in the number 30020 it is enough to delete a single digit (2). In this case, the result is 3000 that is divisible by 10^3 = 1000.

Write a program that prints the minimum number of digits to be deleted from the given integer number n, so that the result is divisible by 10^{k}. The result should not start with the unnecessary leading zero (i.e., zero can start only the number 0, which is required to be written as exactly one digit).

It is guaranteed that the answer exists.


-----Input-----

The only line of the input contains two integer numbers n and k (0 ≤ n ≤ 2 000 000 000, 1 ≤ k ≤ 9).

It is guaranteed that the answer exists. All numbers in the input are written in traditional notation of integers, that is, without any extra leading zeros.


-----Output-----

Print w — the required minimal number of digits to erase. After removing the appropriate w digits from the number n, the result should have a value that is divisible by 10^{k}. The result can start with digit 0 in the single case (the result is zero and written by exactly the only digit 0).


-----Examples-----
Input
30020 3

Output
1

Input
100 9

Output
2

Input
10203049 2

Output
3



-----Note-----

In the example 2 you can remove two digits: 1 and any 0. The result is number 0 which is divisible by any number.
"""

def min_digits_to_remove(n: int, k: int) -> int:
    """
    Calculate the minimum number of digits to be deleted from n to make it divisible by 10^k.
    
    Args:
        n: The integer number (0 ≤ n ≤ 2,000,000,000)
        k: The power of 10 (1 ≤ k ≤ 9)
        
    Returns:
        The minimum number of digits to be deleted
    """
    pass
